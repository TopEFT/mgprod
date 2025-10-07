# Making Run3 Samples
These are instructions for setting up and producing run3 (2022+2023) MC samples.

## Some prerequisites
There's a number of things we need to set up before we can start generating MC events. These steps should only need to be done the first time setting things up.

### Setting up Lobster
In order to produce run3 samples, you need to make sure you're using the python3 compatible version of lobster. To install lobster from scratch we will follow a modified version of lobster install instructions located [here](https://github.com/NDCMS/lobster/blob/lobster-python3/hackathon_instructions.md).

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
# There is a small typo in the latest commit (f7f585b) that we need to fix
cd lobster/core/data
sed -i -e 's|int(major) >= 7 int(major) < 12|int(major) >= 7 and int(major) < 12|g' task.py
cd -

conda env create -f lobster_env.yaml -n lobster
conda activate lobster

# The version of ndcctools needs to be updated to v7.15.9 or newer
conda install -y -c conda-forge ndcctools

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
At this point, the `lobster` environment should be installed. In the future, all that's needed to activate the lobster environment is:
```
unset PYTHONPATH
unset PERL5LIB
conda activate lobster
# Needed to use parrot_run when sandboxing CMSSW
export PATH=/afs/crc.nd.edu/group/ccl/software/x86_64/RedHat9/cctools/7.11.1/bin:$PATH
```

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
```
The `make_run3_cfgs.sh` script will do two things. First, it will source and build the necessary CMSSW releases needed to run each of the MC production steps. Second, it will execute a number of `cmsDriver` commands to produce the python configuration files that we need to run each step of the MC chain. The CMSSW releases will be located in `$WFDIR` and the python configs will be located in `$WFDIR/run3_cfgs`.

> [!IMPORTANT]
> The lobster configs are written assuming the CMSSW releases and python config files are in these locations. If you've changed where they get made or otherwise moved them to a different location, you will need to make sure you update the paths in the lobster configs accordingly.

## Running Lobster
We are finally ready to start running some lobster jobs and produce MC outputs. MC production is typically broken up into a number of steps, where the output for one step becomes the input for the next step. CMSSW can run multiple steps in a single go, so the specific number of steps (i.e. `lobster` workflows) can be different depending on how the python configuration files were created.

For the Run3 samples, the steps are broken up into: LHE -> GEN -> SIM -> DIGI -> RECO -> MAOD -> NAOD. Each step will correspond to a particular `lobster.core.Workflow` within a lobster configuration. A lobster configuration itself can chain together multiple workflows in order to process multiple steps all in one go. For our MC samples we split the production into the "LHE step" and the "post-LHE step". The LHE step, as the name implies, consists of running just the LHE part of the production chain, while the post-LHE step runs all the remaining steps in a single lobster configuration.

> [!CAUTION]
> Any lobster configuration that includes the LHE step as a component MUST NOT have access to batch computing resources that utilize individual process monitoring (such as those coming from the ND opportunistic pool). This is because of the way Madgraph operates internally. When MG executes, it produces thousands of small short lived sub-processes that each need to be individually wrapped and tracked for resource usage. This causes a massive performance bottlekneck that will grind the machine to halt and likely result in failed jobs or jobs that are unable to finish (and that's in the best case scenario).