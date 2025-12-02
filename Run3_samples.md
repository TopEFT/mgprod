# Making Run3 Samples
These are instructions for setting up and producing run3 (2022+2023) MC samples.

## Some prerequisites
There's a number of things we need to set up before we can start generating MC events. These steps should only need to be done the first time setting things up.

### Setting up Lobster
In order to produce run3 samples, you need to make sure you're using the python3 compatible version of lobster. To install lobster from scratch we will follow a modified version of lobster install instructions located [here](https://github.com/NDCMS/lobster/blob/lobster-python3/hackathon_instructions.md).

<details open>
<summary>bash commands</summary>

```
# If you wish to place the git repos in a different location, you can change $HOME to your preferred area
cd $HOME

unset PYTHONPATH
mkdir lobster-python3
cd lobster-python3

# NOTE: Once lobster PR#693 is merged, this should be changed to point to the official lobster repo
git clone https://github.com/anpicci/lobster.git
cd lobster
git checkout lobster-python3-run3

# back to lobster-python3
cd ..

git clone git@github.com:dmwm/WMCore.git --branch 2.3.5
cd WMCore
sed -i -E '/^(gfal2|htcondor|kkmysqlclient|rucio-clients|Sphinx|coverage|memory-profiler|mox3|nose|nose2|pycodestyle|pylint|pymongo)/d' requirements.txt
pip install -r requirements.txt .

# to lobster-python3/lobster
cd ../lobster
pip install -e .
```

</details>

At this point, the `lobster` environment should be installed. In the future, all that's needed to activate the lobster environment is:
```
unset PYTHONPATH
unset PERL5LIB
conda activate lobster
# Needed to use parrot_run when sandboxing CMSSW
cp /afs/crc.nd.edu/group/ccl/software/x86_64/redhat7/cctools/lobster-171-cd5e3e2c-cvmfs-70dfa0d6/bin/parrot_cvmfs_static_run $CONDA_PREFIX/bin/parrot_run
```

> [!TIP]
> It can be tedious always having to remember to run the `unset` commands, so you can automate this by creating an alias for activating the lobster environment by adding `alias actcondalobs="unset PYTHONPATH ; unset PERL5LIB ; conda activate lobster"` to your `.bashrc` file.

### Actually cloning the repo
Up to this point we haven't even had to deal with the `mgprod` repo itself! If you haven't done so yet, make sure to clone and checkout the repo before proceeding. The code for setting up and producing the run3 samples is currently on a separte branch, so we will need to switch to that branch in order to proceed:
```
# Again, if you wish to create the repo somewhere other than the top level of your $HOME directory, feel free to change it here
cd $HOME

git clone https://github.com/TopEFT/mgprod.git
cd mgprod/lobster_workflow
git checkout Run3
```
### Creating the python configs
The python configs used to direct the `cmsRun` job for the run3 samples will be located in the `run3_cfgs` directory. Initially, this directory will only have the `make_run3_cfgs.sh` script in it. This script should have all the necessary information to generate the LHE, GEN, SIM, DIGI, RECO, MAOD, and NAOD configs for 2022, 2022EE, 2023, and 2023BPix run eras.

> [!IMPORTANT]
> Make sure to activate an `el8` singularity container before running the `make_run3_cfgs.sh` script.

```
# If you are still in the lobster environment, deactivate it for now
conda deactivate

WFDIR=$(git rev-parse --show-toplevel)/lobster_workflow
cd $WFDIR/run3_cfgs

# glados provides a number of singularity images for various CMSSW releases, so no extra work is needed here
cmssw-el8
./make_run3_cfgs.sh

cd $WFDIR

# We no longer need to be in a singularity container for actually running lobster
exit
```
The `make_run3_cfgs.sh` script will do two things. First, it will source and build the necessary CMSSW releases needed to run each of the MC production steps. Second, it will execute a number of `cmsDriver` commands to produce the python configuration files that we need to run each step of the MC chain. The CMSSW releases will be located in `$WFDIR` and the python configs will be located in `$WFDIR/run3_cfgs`.

> [!IMPORTANT]
> The lobster configs are written assuming the CMSSW releases and python config files are in these locations. If you've changed where they get made or otherwise moved them to a different location, you will need to make sure you update the paths in the lobster configs accordingly.

## Running Lobster
We are finally ready to start running some lobster jobs and produce MC outputs. MC production is typically broken up into a number of steps, where the output for one step becomes the input for the next step. CMSSW can run multiple steps in a single go, so the specific number of steps (i.e. `lobster` workflows) can be different depending on how the python configuration files were created.

For the Run3 samples, the steps are broken up into: LHE -> GEN -> SIM -> DIGI -> RECO -> MAOD -> NAOD. Each step will correspond to a particular `lobster.core.Workflow` within a lobster configuration. A lobster configuration itself can chain together multiple workflows in order to process multiple steps all in one go. For our MC samples we split the production into the "LHE step" and the "post-LHE step". The LHE step, as the name implies, consists of running just the LHE part of the production chain, while the post-LHE step runs all the remaining steps in a single lobster configuration.

> [!CAUTION]
> Any lobster configuration that includes the LHE step as a component MUST NOT have access to batch computing resources that utilize individual process monitoring (such as those coming from the ND opportunistic pool). This is because of the way Madgraph operates internally. When MG executes, it produces thousands of small short lived sub-processes that each need to be individually wrapped and tracked for resource usage. This causes a massive performance bottlekneck that will grind the machine to halt and likely result in failed jobs or jobs that are unable to finish (and that's in the best case scenario).

The remainder of these instructions will assume that you run everything from the `lobster_workflow` directory.

### The LHE Step
The lobster config for this step is called `lobster_run3_LHE_config.py` and is located in `lobster_cfgs/run3`. Below is an explanation of a number of the configurable options within the lobster config:

<details open>
<summary>Variable descriptions</summary>

- `events_per_gridpack`: This is the total number of events you want to produce for each gridpack specified. Typically we want each gridpack sample to roughly have the same amount of statistics, so gridpack specific event counts isn't really supported.
- `events_per_lumi`: This is the number events each job/task will produce. So if you want to generate 100,000 events, then setting this value to 500 will result in 200 jobs/tasks. You should be careful about setting this to a large number as it represents the smallest amount of work any workflow task can process. So if this value is too large, some of the later MC steps might end up taking a very long time to run.
- `run_setup`: This essentially changes a number of variables that define output directories. There are three configurations: `'full_production'`, `'mg_studies'`, and `'lobster_test'`. The `'lobster_test'` setup is useful if you just want to check to see if lobster can successfully run your tasks, but you don't care about the outputs. `'mg_studies'` should be used if you want to produce a sample with specific settings and you'd like to give the output directory a recognizable/memorable name. Lastly, the `'full_production'` option is similar to `'mg_studies'`, but places the directories separate from where `'mg_studies'` puts things as a way to make it easier to find the main samples we intend to use for the analysis.
- `year`: The LHE step is designed to only produce outputs for a single year at a time. If you want to produce MC for all of run3, you will need to run the LHE step multiple times, switching the `year` for each run.
- `version`: A string used in the paths construction. It should mainly be used when you've configured a lobster run, started it, but realized something went wrong and you would like to restart the run from scratch.
- `grp_tag`: Also used in the paths construction. This is the variable you can use to give your lobster runs a recognizable name that should hopefully be indicative of how the samples were made
- `prod_tag`: This is only used by the 'full_production' setup. "Round" should represent an entire collection of MC samples that we want to use in the analysis and should only be incremented if we find out some fatal flaw in our samples that results in us needing to regenerate the samples from scratch. The "Batch" part simply represents the output from some large scale MC production done in one go. We can generate multiple 'batches' of MC as needed.
- `master_label`: This will be the name advertised by the lobster manager/master once it gets started. It's used by the `work_queue_factory` (explained later) to identify which lobster processes it should talk to in order to figure out how many workers it should request.
- `event_multiplier`: This is a dictionary that multiplies the requested MC events by the specified factor for the corresponding MC process. This is used to try and ensure that each of our MC processes end up with roughly equal statistics. It's needed because the processes with +1 parton undergo `pythia` jet matching and thus will have some fraction of their events vetoed. This multiplier is meant to compensate for that fraction.
- `gridpacks`: This is where you specify the locations of all the gridpacks you want to make samples for. The code assumes that all gridpacks are located on `/cephfs` and are in someone's user area. So we omit the `/cms/cephfs/data/store/user/` portion of the path when listing the gridpacks here.

</details>

Once you are done modifying the `lobster_run3_LHE_config.py` script, return to the `lobster_workflow` directory, as we are now ready to run lobster:
```
lobster process lobster_cfgs/run3/lobster_run3_LHE_config.py
```
After running this command you should see a print out that looks something like the following:
```
(lobster) [glados:lobster_workflow]$ lobster process lobster_cfgs/run3/lobster_run3_LHE_config.py 
Generating Workflows
    [1/1] Gridpack: ttHJet_ctWReTest13p6AxisScan_run0_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz (nevts 50000)
merging disabled due to malformed size -1
2025-10-14 17:12:51 [INFO] lobster: saving log to /tmpscratch/users/$USER/SOMETHING/process.log
2025-10-14 17:12:51 [INFO] lobster: saving debug log to /tmpscratch/users/$USER/SOMETHING/process_debug.log
```
Where `$USER` will be your `glados` username and `SOMETHING` will depend on the `run_setup` you used. For example, if you used `lobster_test` it might be `LHE_step/tests/lobster_20251014_1712`. The `process.log` is where you can check the status of the lobster jobs and should be monitored, especially if you're running an untested setup to ensure jobs are completing. Below is an example printout of the start of the `process.log`:

<details>
<summary>Example log</summary>

```
2025-10-14 15:10:34 [INFO] lobster: saving debug log to /tmpscratch/users/ywan2/LHE_step/tests/lobster_20251014_1510/process_debug.log
2025-10-14 15:10:34 [INFO] lobster: saving additional log for configure to /tmpscratch/users/ywan2/LHE_step/tests/lobster_20251014_1510/configure.log
2025-10-14 15:10:34 [INFO] lobster: saving additional log for plotting to /tmpscratch/users/ywan2/LHE_step/tests/lobster_20251014_1510/plotting.log
2025-10-14 15:10:34 [INFO] lobster.core: saving stderr and stdout to /tmpscratch/users/ywan2/LHE_step/tests/lobster_20251014_1510/process.err
2025-10-14 15:10:34 [INFO] lobster.sandbox: packing sandbox into /tmpscratch/users/ywan2/LHE_step/tests/lobster_20251014_1510/sandbox-CMSSW_12_4_14_patch3-el8_amd64_gcc10-26740c8.tar.bz2
2025-10-14 15:10:34 [INFO] lobster.source: querying backend for lhe_step_tllq4fNoSchanWNoHiggs0p_ExampleTag_run0
2025-10-14 15:10:34 [INFO] lobster.source: registering lhe_step_tllq4fNoSchanWNoHiggs0p_ExampleTag_run0 in database
2025-10-14 15:10:34 [INFO] lobster.actions: plots in /users/ywan2/afs/www/lobster/LHE_step/tests/lobster_20251014_1510 will be updated automatically
2025-10-14 15:10:34 [INFO] lobster.core: using wq from /users/ywan2/miniconda3/envs/lobster-mamba/lib/python3.10/site-packages/ndcctools/work_queue.py
2025-10-14 15:10:34 [INFO] lobster.core: running Lobster version 2.0a1+41d9fd5
2025-10-14 15:10:34 [INFO] lobster.core: current PID is 2748991
2025-10-14 19:10:34 [INFO] lobster.core: starting queue as lobster_ywan2_EFT_T3_20251014_1510
2025-10-14 19:10:34 [INFO] lobster.source: creating task(s) 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
2025-10-14 19:10:35 [INFO] lobster.core: 0 out of 0 workers busy; 0 tasks running, 10 waiting; 30 units left
2025-10-14 19:10:35 [INFO] lobster.actions: starting plotting process
```

</details>

You will also see an `IndexError` relating to the lobster plotting machinery. This is a known issue and can be safely ignored for now.

<details>
<summary>IndexError Example</summary>

```
2025-10-14 19:10:35 [ERROR] lobster.actions: plotting failed with: too many indices for array: array is 1-dimensional, but 2 were indexed. Trace: Traceback (most recent call last):
  File "/users/ywan2/lobster-python3/lobster/lobster/actions.py", line 17, in runplots
    plotter.make_plots(foremen=foremen)
  File "/users/ywan2/lobster-python3/lobster/lobster/commands/plot.py", line 1300, in make_plots
    self.__category_stats = {'all': self.readlog()}
  File "/users/ywan2/lobster-python3/lobster/lobster/commands/plot.py", line 526, in readlog
    stats[:, 0] /= 1e6
IndexError: too many indices for array: array is 1-dimensional, but 2 were indexed

```

</details>

### Starting a Work Queue Factory
In order for the lobster tasks to get processed, we need to provide the lobster master with workers. This is done by starting a Work Queue Factory.

> [!IMPORTANT]
> In order to ensure the Work Queue Factory version is compatible with your lobster master, you need to make sure you start the factory from the same `conda` environment you used to start your lobster master.

The command to start a factory is `work_queue_factory`. We will need to specify a number of command-line options when executing this command. Below is an example of a fully specified command:
```bash
nohup work_queue_factory -T condor -M lobster_$USER_.* --runos al8-wa-7.15.9 \
--scratch-dir /tmp/wq-$USER-factory -d all -o /tmp/$USER_lobster_factory_T3.debug \
-C wq_factories/factory_EFT_T3_12c.json &
```
Below is a description of the options used in the above command:
- The `-T` option specifies what type of batch system you are using. For the ND T3, this should always be `condor`.
- The `-M` option specifies an expression that the factory uses to identify which lobster masters it should provide workers for. This expression should be able to match to whatever you had set your `master_label` to in the lobster config.
- The `--runos` option specifies a particular singularity image that should be used by the workers. For Run3 samples this should always be `al8-wa-7.15.9`.
- The `--scratch-dir` option specifies a directory for the factory to store the condor submit files and logs. Typically you won't need to care about anything in this directory unless you're trying to debug issues with the factory
- The `-d` option specifies what debug info to print out.
- The `-o` option specifies the file to send debugging info to. Again, you typically don't need to check this file, unless you're trying to figure out problems with the factory.
- The `-C` option specifies a path to `json` file that contains requirements that the requested workers need to satisfy. You can find examples of various factory configs in the `wq_factories` folder.

> [!IMPORTANT]
> Note that this command is executed with `nohup`, which means it will continue to execute even after you logout from `glados`. The command is also ended with a `&`, which means the process will be moved to the background. It is your responsibility to keep track of your running factories and kill/restart them when needed. You can check the list of running processes associated with your username by running the following command: `ps aux | grep $USER`
