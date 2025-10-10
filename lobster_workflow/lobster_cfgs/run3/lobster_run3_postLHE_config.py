import datetime
import os
import sys
import shutil

from lobster import cmssw
from lobster.core import AdvancedOptions, Category, Config, Dataset,ParentDataset, StorageConfiguration, Workflow

sys.path.append(os.getcwd())
from helpers.utils import regex_match, run_process

tstamp = datetime.datetime.now().strftime('%Y%m%d_%H%M')

input_path = "/store/user/"
input_path_full = "/cms/cephfs/data/" + input_path

# master_label = f'EFT_CRC_postLHE_crc_{tstamp}'
master_label = f'EFT_T3_postLHE_{tstamp}'

# Need to find a better solution for this
PATH_TO_NAOD_CMSSW = f"{os.getcwd()}/CMSSW_13_0_13"

# Specfy the run setup
# run_setup = 'full_production'
# run_setup = 'mg_studies'
run_setup = 'testing'

year = "2022"

version = "v1"
grp_tag = "test" + year
prod_tag = "Round/Batch1"

# Only run over lhe steps from specific processes/coeffs/runs
process_whitelist = []
coeff_whitelist   = []
runs_whitelist    = []  # (i.e. MG starting points)

# Specify the input directories. Note: The workflows in each of the input directories should all be uniquely named w.r.t each other
input_dirs = [
    # os.path.join(input_path_full,"awightma/LHE_step/tests/lobster_20251008_1916/")
    # os.path.join(input_path_full,"awightma/LHE_step/tests/lobster_20251009_1354")

]

########## Select input directories according to whitelists ##########
lhe_dirs = []
for path in input_dirs:
    for fd in os.listdir(path):
        if fd.find('lhe_step_') < 0:
            continue
        print(fd)
        arr = fd.split('_')
        print(arr)
        p,c,r = arr[2],arr[3],arr[4]
        print(p,c,r)
        # Skip any inputs that don't match any of our lists
        if len(regex_match([p],process_whitelist)) == 0:
            continue
        elif len(regex_match([c],coeff_whitelist)) == 0:
            continue
        elif len(regex_match([r],runs_whitelist)) == 0:
            continue
        relpath = os.path.relpath(path,input_path_full)
        print(relpath)
        lhe_dirs.append(os.path.join(relpath,fd))

########## Set up output based on run setup ##########
if run_setup == "mg_studies":
    # For MadGraph test studies
    output_path  = f"/store/user/$USER/postLHE_step/{grp_tag}/{version}"
    workdir_path = f"/tmpscratch/users/$USER/postLHE_step/{grp_tag}/{version}"
    plotdir_path = f"~/www/lobster/postLHE_step/{grp_tag}/{version}"
elif run_setup == "full_production":
    # For Large MC production
    output_path  = f"/store/user/$USER/FullProduction/Run3/{year}/{prod_tag}/postLHE_step/{version}"
    workdir_path = f"/tmpscratch/users/$USER/FullProduction/Run3/{year}/{prod_tag}/postLHE_step/{version}"
    plotdir_path = f"~/www/lobster/FullProduction/Run3/{year}/{prod_tag}/postLHE_step/{version}"
elif run_setup == "testing":
    # For lobster workflow tests
    grp_tag = f"lobster_{tstamp}"
    output_path  = f"/store/user/$USER/postLHE_step/tests/{grp_tag}"
    workdir_path = f"/tmpscratch/users/$USER/postLHE_step/tests/{grp_tag}"
    plotdir_path = f"~/www/lobster/postLHE_step/tests/{grp_tag}"
else:
    raise ValueError(f"Unknown run setup, {run_setup}")

storage = StorageConfiguration(
    input = [
        "file:///cms/cephfs/data" + input_path,
        "root://skynet013.crc.nd.edu:1094/" + input_path,
        # "root://skynet013.crc.nd.edu:1096/" + input_path, # For outside-of-ND file access
    ],
    output = [
        "file:///cms/cephfs/data" + output_path,
        "root://skynet013.crc.nd.edu:1094/" + output_path,
    ],
    disable_input_streaming=True
)

########## Resources for each step ##########

# Worker Res.:
#   Cores:  12    | 4
#   Memory: 16000 | 8000
#   Disk:   13000 | 6500

gen_resources = Category(
    name='gen',
    cores=1,
    memory=2000,
    disk=3000,
    tasks_min=12,
    tasks_max=3000,
    # mode='fixed'
)
sim_resources = Category(
    name='sim',
    cores=6,
    memory=3000,
    disk=3000,
    tasks_min=12,
    # mode='fixed'
)
digi_resources = Category(
    name='digi',
    cores=6,
    memory=7800,
    disk=6000,
    # mode='fixed'
)
reco_resources = Category(
    name='reco',
    cores=3,
    memory=5000,
    disk=3000,
    # mode='fixed'
)
maod_resources = Category(
    name='maod',
    cores=2,
    memory=3500,
    disk=2000,
    # mode='fixed'
)
naod_resources = Category(
    name='naod',
    cores=2,
    memory=3500,
    disk=2000,
    # mode='fixed'
)

########## Set up dictionary for cfg files ##########
wf_steps = ['gen','sim','digi','reco','maod','naod']
run3_base = "run3_cfgs"

cfg_map = {
    "2022": {
        'all_procs': {
            'sim' : os.path.join(run3_base,'2022_SIM_cfg.py'),
            'digi': os.path.join(run3_base,'2022_DIGI_cfg.py'),
            'reco': os.path.join(run3_base,'2022_RECO_cfg.py'),
            'maod': os.path.join(run3_base,'2022_MAODv4_cfg.py'),
            'naod': os.path.join(run3_base,'2022_NAODv12_cfg.py'),
        },
    },
    "2022EE": {
        'all_procs': {
            'sim' : os.path.join(run3_base,'2022EE_SIM_cfg.py'),
            'digi': os.path.join(run3_base,'2022EE_DIGI_cfg.py'),
            'reco': os.path.join(run3_base,'2022EE_RECO_cfg.py'),
            'maod': os.path.join(run3_base,'2022EE_MAODv4_cfg.py'),
            'naod': os.path.join(run3_base,'2022EE_NAODv12_cfg.py'),
        },
    },
    "2023": {
        'all_procs': {
            'sim' : os.path.join(run3_base,'2023_SIM_cfg.py'),
            'digi': os.path.join(run3_base,'2023_DIGI_cfg.py'),
            'reco': os.path.join(run3_base,'2023_RECO_cfg.py'),
            'maod': os.path.join(run3_base,'2023_MAODv4_cfg.py'),
            'naod': os.path.join(run3_base,'2023_NAODv12_cfg.py'),
        },
    },
    "2023BPix": {
        'all_procs': {
            'sim' : os.path.join(run3_base,'2023BPix_SIM_cfg.py'),
            'digi': os.path.join(run3_base,'2023BPix_DIGI_cfg.py'),
            'reco': os.path.join(run3_base,'2023BPix_RECO_cfg.py'),
            'maod': os.path.join(run3_base,'2023BPix_MAODv4_cfg.py'),
            'naod': os.path.join(run3_base,'2023BPix_NAODv12_cfg.py'),
        },
    },
}

gen_cfg_map = {
    '2022': {
        'ttHJet':                  {'gen': os.path.join(run3_base,'2022_GEN-ttHJet_cfg.py')},
        'ttlnuJet':                {'gen': os.path.join(run3_base,'2022_GEN-ttlnuJet_cfg.py')},
        'ttllNuNuJetNoHiggs':      {'gen': os.path.join(run3_base,'2022_GEN-ttlnuJet_cfg.py')},
        'tllq4fNoSchanWNoHiggs0p': {'gen': os.path.join(run3_base,'2022_GEN-ttlnu_cfg.py')},
        'tHq4f':                   {'gen': os.path.join(run3_base,'2022_GEN-ttlnu_cfg.py')},
        'tttt':                    {'gen': os.path.join(run3_base,'2022_GEN-ttlnu_cfg.py')},
    },
    '2022EE': {
        'ttHJet':                  {'gen': os.path.join(run3_base,'2022EE_GEN-ttHJet_cfg.py')},
        'ttlnuJet':                {'gen': os.path.join(run3_base,'2022EE_GEN-ttlnuJet_cfg.py')},
        'ttllNuNuJetNoHiggs':      {'gen': os.path.join(run3_base,'2022EE_GEN-ttlnuJet_cfg.py')},
        'tllq4fNoSchanWNoHiggs0p': {'gen': os.path.join(run3_base,'2022EE_GEN-ttlnu_cfg.py')},
        'tHq4f':                   {'gen': os.path.join(run3_base,'2022EE_GEN-ttlnu_cfg.py')},
        'tttt':                    {'gen': os.path.join(run3_base,'2022EE_GEN-ttlnu_cfg.py')},
    },
    '2023': {
        'ttHJet':                  {'gen': os.path.join(run3_base,'2023_GEN-ttHJet_cfg.py')},
        'ttlnuJet':                {'gen': os.path.join(run3_base,'2023_GEN-ttlnuJet_cfg.py')},
        'ttllNuNuJetNoHiggs':      {'gen': os.path.join(run3_base,'2023_GEN-ttlnuJet_cfg.py')},
        'tllq4fNoSchanWNoHiggs0p': {'gen': os.path.join(run3_base,'2023_GEN-ttlnu_cfg.py')},
        'tHq4f':                   {'gen': os.path.join(run3_base,'2023_GEN-ttlnu_cfg.py')},
        'tttt':                    {'gen': os.path.join(run3_base,'2023_GEN-ttlnu_cfg.py')},
    },
    '2023BPix': {
        'ttHJet':                  {'gen': os.path.join(run3_base,'2023BPix_GEN-ttHJet_cfg.py')},
        'ttlnuJet':                {'gen': os.path.join(run3_base,'2023BPix_GEN-ttlnuJet_cfg.py')},
        'ttllNuNuJetNoHiggs':      {'gen': os.path.join(run3_base,'2023BPix_GEN-ttlnuJet_cfg.py')},
        'tllq4fNoSchanWNoHiggs0p': {'gen': os.path.join(run3_base,'2023BPix_GEN-ttlnu_cfg.py')},
        'tHq4f':                   {'gen': os.path.join(run3_base,'2023BPix_GEN-ttlnu_cfg.py')},
        'tttt':                    {'gen': os.path.join(run3_base,'2023BPix_GEN-ttlnu_cfg.py')},
    },
}

# Create the fragment map and inject the gen configs
fragment_map = cfg_map[year]
for k,v in gen_cfg_map[year].items():
    fragment_map[k] = v

########## Specify CMSSW rel for each step ##########
release_map = {
    '2022': {
        'gen' : 'CMSSW_12_4_14_patch3',
        'sim' : 'CMSSW_12_4_14_patch3',
        'digi': 'CMSSW_12_4_14_patch3',
        'reco': 'CMSSW_12_4_14_patch3',
        'maod': 'CMSSW_13_0_13',
        'naod': 'CMSSW_13_0_13',
    },
    '2022EE': {
        'gen' : 'CMSSW_12_4_14_patch3',
        'sim' : 'CMSSW_12_4_14_patch3',
        'digi': 'CMSSW_12_4_14_patch3',
        'reco': 'CMSSW_12_4_14_patch3',
        'maod': 'CMSSW_13_0_13',
        'naod': 'CMSSW_13_0_13',
    },
    '2023': {
        'gen' : 'CMSSW_13_0_13',
        'sim' : 'CMSSW_13_0_13',
        'digi': 'CMSSW_13_0_13',
        'reco': 'CMSSW_13_0_13',
        'maod': 'CMSSW_13_0_13',
        'naod': 'CMSSW_13_0_13',
    },
    '2023BPix': {
        'gen' : 'CMSSW_13_0_13',
        'sim' : 'CMSSW_13_0_13',
        'digi': 'CMSSW_13_0_13',
        'reco': 'CMSSW_13_0_13',
        'maod': 'CMSSW_13_0_13',
        'naod': 'CMSSW_13_0_13',
    },
}

########## Generate workflows ##########
wfs = []
print("Generating Workflows")
for idx,lhe_dir in enumerate(lhe_dirs):
    print(f"\t[{idx+1}/{len(lhe_dirs)}] LHE Input: {lhe_dir}")
    head,tail = os.path.split(lhe_dir)
    arr = tail.split('_')
    p,c,r = arr[2],arr[3],arr[4]
    label_tag = f"{p}_{c}_{r}"

    gen = Workflow(
        label=f"gen_step_{label_tag}",
        command=f"cmsRun {fragment_map[p]['gen']}",
        sandbox=cmssw.Sandbox(release=release_map[year]['gen']),
        merge_size=-1,  # Don't merge files we don't plan to keep
        cleanup_input=False, # Do not accidently clean up the LHE files!!!
        globaltag=False,
        outputs=['GEN-00000.root'],
        dataset=Dataset(
            files=lhe_dir,
            files_per_task=1,
            patterns=["*.root"]
        ),
        category=gen_resources
    )

    sim = Workflow(
        label=f"sim_step_{label_tag}",
        command=f"cmsRun {fragment_map['all_procs']['sim']}",
        sandbox=cmssw.Sandbox(release=release_map[year]['sim']),
        merge_size=-1,  # Don't merge files we don't plan to keep
        cleanup_input=True,
        #cleanup_input=False,
        globaltag=False,
        outputs=['SIM-00000.root'],
        dataset=ParentDataset(
            parent=gen,
            units_per_task=1
        ),
        category=sim_resources
    )

    digi = Workflow(
        label=f"digi_step_{label_tag}",
        command=f"cmsRun {fragment_map['all_procs']['digi']}",
        sandbox=cmssw.Sandbox(release=release_map[year]['digi']),
        merge_size=-1,  # Don't merge files we don't plan to keep
        cleanup_input=True,
        #cleanup_input=False,
        globaltag=False,
        outputs=['DIGI-00000.root'],
        dataset=ParentDataset(
            parent=sim,
            units_per_task=1
        ),
        category=digi_resources
    )

    reco = Workflow(
        label=f"reco_step_{label_tag}",
        command=f"cmsRun {fragment_map['all_procs']['reco']}",
        sandbox=cmssw.Sandbox(release=release_map[year]['reco']),
        merge_size=-1,  # Don't merge files we don't plan to keep
        cleanup_input=True,
        #cleanup_input=False,
        globaltag=False,
        outputs=['RECO-00000.root'],
        dataset=ParentDataset(
            parent=digi,
            units_per_task=1
        ),
        category=reco_resources
    )

    maod = Workflow(
        label=f"mAOD_step_{label_tag}",
        command=f"cmsRun {fragment_map['all_procs']['maod']}",
        sandbox=cmssw.Sandbox(release=release_map[year]['maod']),
        merge_size=-1,  # Don't merge files we don't plan to keep
        cleanup_input=True,
        #cleanup_input=False,
        globaltag=False,
        outputs=['MAOD-00000.root'],
        dataset=ParentDataset(
            parent=reco,
            units_per_task=1
        ),
        category=maod_resources
    )

    naod = Workflow(
        label=f"nAOD_step_{label_tag}",
        command=f"cmsRun {fragment_map['all_procs']['naod']}",
        sandbox=cmssw.Sandbox(release=release_map[year]['naod']),
        merge_size='256M',
        merge_command='python3 haddnano.py @outputfiles @inputfiles',
        extra_inputs=[os.path.join(PATH_TO_NAOD_CMSSW,'src/PhysicsTools/NanoAODTools/scripts/haddnano.py')],
        cleanup_input=False,
        globaltag=False,
        outputs=['NAOD-00000.root'],
        dataset=ParentDataset(
            parent=maod,
            units_per_task=1
        ),
        category=naod_resources
    )

    wfs.extend([gen])
    wfs.extend([sim,digi,reco])
    wfs.extend([maod])
    wfs.extend([naod])

config = Config(
    label=master_label,
    workdir=workdir_path,
    plotdir=plotdir_path,
    storage=storage,
    workflows=wfs,
    advanced=AdvancedOptions(
        bad_exit_codes=[127, 160],
        log_level=1,
        payload=10,
        osg_version="3.6",  # Possibly needed if using Run2 CMSSW release
        # xrootd_servers=["skynet013.crc.nd.edu:1094"]
    )
)