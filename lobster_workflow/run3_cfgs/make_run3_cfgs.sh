#!/bin/bash

# See: https://twiki.cern.ch/twiki/bin/view/CMS/PdmVRun3Analysis#Recipes_for_Run3Summer22_and_Run

# export SCRAM_ARCH=export SCRAM_ARCH=el8_amd64_gcc11
# export SCRAM_ARCH=export SCRAM_ARCH=el9_amd64_gcc11
source source /cvmfs/cms.cern.ch/cmsset_default.sh

setup_rel(){
    printf "\nSet up CMSSW release for $1...\n"
    if [ -r $1/src ] ; then
        echo release $1 already exists
    else
        scram p CMSSW $1
    fi
    cd $1/src
    eval `scram runtime -sh`

    FDIR=../../../fragments # Dir of fragments, relative to CMSSW/src

    mkdir -p ./Configuration/GenProduction/python/ # Make a directory for the fragment if it does not already exist
    cp $FDIR/$2 ./Configuration/GenProduction/python/ # Copy the fragment to the  directory

    scram b
    cd ../..

    printf "CMSSW base: $CMSSW_BASE\n"
}

# 2022 LHE+GEN+RECO
(
    cmssw-el8
    export SCRAM_ARCH=el8_amd64_gcc11


    REL=CMSSW_12_4_14_patch3
    CONDITIONS=124X_mcRun3_2022_realistic_v12
    BEAMSPOT=Realistic25ns13p6TeVEarly2022Collision
    ERA=Run3
    PU_INPUT=dbs:/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer22_124X_mcRun3_2022_realistic_v11-v2/PREMIX

    # LHE
    FRAGMENT=baseline_custom_ND-fragment.py
    FOUT=LHE-00000.root
    CFGNAME=2022_LHE_cfg.py
    setup_rel $REL $FRAGMENT
    cmsDriver.py Configuration/GenProduction/python/$FRAGMENT --mc --eventcontent LHE --datatier LHE --conditions $CONDITIONS --beamspot $BEAMSPOT --step LHE --era $ERA --fileout file:$FOUT --python_filename $CFGNAME --no_exec

    # GEN
    FIN=LHE-00000.root
    FOUT=GEN-00000.root
    
    FRAGMENT=ttlnuJets_custom_ND-fragment.py
    setup_rel $REL $FRAGMENT
    CFGNAME=2022_GEN-ttlnuJet_cfg.py
    cmsDriver.py Configuration/GenProduction/python/$FRAGMENT --mc --eventcontent RAWSIM --datatier GEN --conditions $CONDITIONS --beamspot $BEAMSPOT --step GEN --geometry DB:Extended --era $ERA --fileout file:$FOUT --filein file:$FIN --python_filename $CFGNAME --no_exec

    FRAGMENT=ttHJets_custom_ND-fragment.py
    setup_rel $REL $FRAGMENT
    CFGNAME=2022_GEN-ttHJets_cfg.py
    cmsDriver.py Configuration/GenProduction/python/$FRAGMENT --mc --eventcontent RAWSIM --datatier GEN --conditions $CONDITIONS --beamspot $BEAMSPOT --step GEN --geometry DB:Extended --era $ERA --fileout file:$FOUT --filein file:$FIN --python_filename $CFGNAME --no_exec

    FRAGMENT=tllq4f_custom_ND-fragment.py
    setup_rel $REL $FRAGMENT
    CFGNAME=2022_GEN-tllq4f_cfg.py
    cmsDriver.py Configuration/GenProduction/python/$FRAGMENT --mc --eventcontent RAWSIM --datatier GEN --conditions $CONDITIONS --beamspot $BEAMSPOT --step GEN --geometry DB:Extended --era $ERA --fileout file:$FOUT --filein file:$FIN --python_filename $CFGNAME --no_exec

    # SIM
    FIN=GEN-00000.root
    FOUT=SIM-00000.root
    CFGNAME=2022_SIM_cfg.py
    cmsDriver.py step1 --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions $CONDITIONS --beamspot $BEAMSPOT --step SIM --geometry DB:Extended --era $ERA --filein file:$FIN --fileout file:$FOUT --python_filename $CFGNAME --no_exec

    # DRPremix step1
    FIN=SIM-00000.root
    FOUT=DIGI-00000.root
    CFGNAME=2022_DIGI_cfg.py
    cmsDriver.py step1 --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions $CONDITIONS --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:2022v12 --procModifiers premix_stage2,siPixelQualityRawToDigi --nThreads 4 --geometry DB:Extended --datamix PreMix --era $ERA --filein file:$FIN --fileout file:$FOUT --pileup_input "$PU_INPUT" --python_filename $CFGNAME --no_exec
    
    # DRPremix step2
    FIN=DIGI-00000.root
    FOUT=RECO-00000.root
    CFGNAME=2022_RECO_cfg.py
    cmsDriver.py step2 --mc --eventcontent AODSIM --datatier AODSIM --conditions $CONDITIONS --step RAW2DIGI,L1Reco,RECO,RECOSIM --procModifiers siPixelQualityRawToDigi --nThreads 4 --geometry DB:Extended --era $ERA --filein file:$FIN --fileout file:$FOUT --python_filename $CFGNAME --no_exec

    exit
)

# 2022EE LHE+GEN+RECO
(
    cmssw-el8
    export SCRAM_ARCH=el8_amd64_gcc11

    REL=CMSSW_12_4_14_patch3
    CONDITIONS=124X_mcRun3_2022_realistic_postEE_v3
    BEAMSPOT=Realistic25ns13p6TeVEarly2022Collision
    ERA=Run3
    PU_INPUT=dbs:/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer22_124X_mcRun3_2022_realistic_v11-v2/PREMIX

    # LHE
    FRAGMENT=baseline_custom_ND-fragment.py
    FOUT=LHE-00000.root
    CFGNAME=2022EE_LHE_cfg.py
    setup_rel $REL $FRAGMENT
    cmsDriver.py Configuration/GenProduction/python/$FRAGMENT --mc --eventcontent LHE --datatier LHE --conditions $CONDITIONS --beamspot $BEAMSPOT --step LHE --era $ERA --fileout file:$FOUT --python_filename $CFGNAME --no_exec

    # GEN
    FIN=LHE-00000.root
    FOUT=GEN-00000.root

    FRAGMENT=ttlnuJets_custom_ND-fragment.py
    setup_rel $REL $FRAGMENT
    CFGNAME=2022EE_GEN-ttlnuJet_cfg.py
    cmsDriver.py Configuration/GenProduction/python/$FRAGMENT --mc --eventcontent RAWSIM --datatier GEN --conditions $CONDITIONS --beamspot $BEAMSPOT --step GEN --geometry DB:Extended --era $ERA --fileout file:$FOUT --filein file:$FIN --python_filename $CFGNAME --no_exec

    FRAGMENT=ttHJets_custom_ND-fragment.py
    setup_rel $REL $FRAGMENT
    CFGNAME=2022EE_GEN-ttHJets_cfg.py
    cmsDriver.py Configuration/GenProduction/python/$FRAGMENT --mc --eventcontent RAWSIM --datatier GEN --conditions $CONDITIONS --beamspot $BEAMSPOT --step GEN --geometry DB:Extended --era $ERA --fileout file:$FOUT --filein file:$FIN --python_filename $CFGNAME --no_exec

    FRAGMENT=tllq4f_custom_ND-fragment.py
    setup_rel $REL $FRAGMENT
    CFGNAME=2022EE_GEN-tllq4f_cfg.py
    cmsDriver.py Configuration/GenProduction/python/$FRAGMENT --mc --eventcontent RAWSIM --datatier GEN --conditions $CONDITIONS --beamspot $BEAMSPOT --step GEN --geometry DB:Extended --era $ERA --fileout file:$FOUT --filein file:$FIN --python_filename $CFGNAME --no_exec

    # SIM
    FIN=GEN-00000.root
    FOUT=SIM-00000.root
    CFGNAME=2022EE_SIM_cfg.py
    cmsDriver.py step1 --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions $CONDITIONS --beamspot $BEAMSPOT --step SIM --geometry DB:Extended --era $ERA --filein file:$FIN --fileout file:$FOUT --python_filename $CFGNAME --no_exec

    # DRPremix step1
    FIN=SIM-00000.root
    FOUT=DIGI-00000.root
    CFGNAME=2022EE_DIGI_cfg.py
    cmsDriver.py step1 --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions $CONDITIONS --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:2022v12 --procModifiers premix_stage2,siPixelQualityRawToDigi --nThreads 4 --geometry DB:Extended --datamix PreMix --era $ERA --filein file:$FIN --fileout file:$FOUT --pileup_input "$PU_INPUT" --python_filename $CFGNAME --no_exec
    
    # DRPremix step2
    FIN=DIGI-00000.root
    FOUT=RECO-00000.root
    CFGNAME=2022EE_RECO_cfg.py
    cmsDriver.py step2 --mc --eventcontent AODSIM --datatier AODSIM --conditions $CONDITIONS --step RAW2DIGI,L1Reco,RECO,RECOSIM --procModifiers siPixelQualityRawToDigi --nThreads 4 --geometry DB:Extended --era $ERA --filein file:$FIN --fileout file:$FOUT --python_filename $CFGNAME --no_exec

    exit
)

# 2023 LHE+GEN+RECO
(
    cmssw-el9
    export SCRAM_ARCH=el9_amd64_gcc11

    REL=CMSSW_13_0_13
    CONDITIONS=130X_mcRun3_2023_realistic_v14
    BEAMSPOT=Realistic25ns13p6TeVEarly2023Collision
    ERA=Run3_2023
    PU_INPUT=dbs:/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer23_130X_mcRun3_2023_realistic_v13-v1/PREMIX

    # LHE
    FRAGMENT=baseline_custom_ND-fragment.py
    FOUT=LHE-00000.root
    CFGNAME=2023_LHE_cfg.py
    setup_rel $REL $FRAGMENT
    cmsDriver.py Configuration/GenProduction/python/$FRAGMENT --mc --eventcontent LHE --datatier LHE --conditions $CONDITIONS --beamspot $BEAMSPOT --step LHE --era $ERA --fileout file:$FOUT --python_filename $CFGNAME --no_exec

    # GEN
    FIN=LHE-00000.root
    FOUT=GEN-00000.root

    FRAGMENT=ttlnuJets_custom_ND-fragment.py
    setup_rel $REL $FRAGMENT
    CFGNAME=2023_GEN-ttlnuJet_cfg.py
    cmsDriver.py Configuration/GenProduction/python/$FRAGMENT --mc --eventcontent RAWSIM --datatier GEN --conditions $CONDITIONS --beamspot $BEAMSPOT --step GEN --geometry DB:Extended --era $ERA --fileout file:$FOUT --filein file:$FIN --python_filename $CFGNAME --no_exec

    FRAGMENT=ttHJets_custom_ND-fragment.py
    setup_rel $REL $FRAGMENT
    CFGNAME=2023_GEN-ttHJets_cfg.py
    cmsDriver.py Configuration/GenProduction/python/$FRAGMENT --mc --eventcontent RAWSIM --datatier GEN --conditions $CONDITIONS --beamspot $BEAMSPOT --step GEN --geometry DB:Extended --era $ERA --fileout file:$FOUT --filein file:$FIN --python_filename $CFGNAME --no_exec

    FRAGMENT=tllq4f_custom_ND-fragment.py
    setup_rel $REL $FRAGMENT
    CFGNAME=2023_GEN-tllq4f_cfg.py
    cmsDriver.py Configuration/GenProduction/python/$FRAGMENT --mc --eventcontent RAWSIM --datatier GEN --conditions $CONDITIONS --beamspot $BEAMSPOT --step GEN --geometry DB:Extended --era $ERA --fileout file:$FOUT --filein file:$FIN --python_filename $CFGNAME --no_exec

    # SIM
    FIN=GEN-00000.root
    FOUT=SIM-00000.root
    CFGNAME=2023_SIM_cfg.py
    cmsDriver.py step1 --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions $CONDITIONS --beamspot $BEAMSPOT --step SIM --geometry DB:Extended --era $ERA --filein file:$FIN --fileout file:$FOUT --python_filename $CFGNAME --no_exec

    # DRPremix step1
    FIN=SIM-00000.root
    FOUT=DIGI-00000.root
    CFGNAME=2023_DIGI_cfg.py
    cmsDriver.py step1 --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions $CONDITIONS --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:2022v12 --procModifiers premix_stage2,siPixelQualityRawToDigi --nThreads 4 --geometry DB:Extended --datamix PreMix --era $ERA --filein file:$FIN --fileout file:$FOUT --pileup_input "$PU_INPUT" --python_filename $CFGNAME --no_exec
    
    # DRPremix step2
    FIN=DIGI-00000.root
    FOUT=RECO-00000.root
    CFGNAME=2023_RECO_cfg.py
    cmsDriver.py step2 --mc --eventcontent AODSIM --datatier AODSIM --conditions $CONDITIONS --step RAW2DIGI,L1Reco,RECO,RECOSIM --procModifiers siPixelQualityRawToDigi --nThreads 4 --geometry DB:Extended --era $ERA --filein file:$FIN --fileout file:$FOUT --python_filename $CFGNAME --no_exec

    exit
)

# 2023BPix LHE+GEN+RECO
(
    cmssw-el9
    export SCRAM_ARCH=el9_amd64_gcc11

    REL=CMSSW_13_0_13
    CONDITIONS=130X_mcRun3_2023_realistic_postBPix_v2
    BEAMSPOT=Realistic25ns13p6TeVEarly2023Collision
    ERA=Run3_2023
    PU_INPUT=dbs:/Neutrino_E-10_gun/Run3Summer21PrePremix-Summer23BPix_130X_mcRun3_2023_realistic_postBPix_v1-v1/PREMIX

    # LHE
    FRAGMENT=baseline_custom_ND-fragment.py
    FOUT=LHE-00000.root
    CFGNAME=2023_LHE_cfg.py
    setup_rel $REL $FRAGMENT
    cmsDriver.py Configuration/GenProduction/python/$FRAGMENT --mc --eventcontent LHE --datatier LHE --conditions $CONDITIONS --beamspot $BEAMSPOT --step LHE --era $ERA --fileout file:$FOUT --python_filename $CFGNAME --no_exec

    # GEN
    FIN=LHE-00000.root
    FOUT=GEN-00000.root

    FRAGMENT=ttlnuJets_custom_ND-fragment.py
    setup_rel $REL $FRAGMENT
    CFGNAME=2023BPix_GEN-ttlnuJet_cfg.py
    cmsDriver.py Configuration/GenProduction/python/$FRAGMENT --mc --eventcontent RAWSIM --datatier GEN --conditions $CONDITIONS --beamspot $BEAMSPOT --step GEN --geometry DB:Extended --era $ERA --fileout file:$FOUT --filein file:$FIN --python_filename $CFGNAME --no_exec

    FRAGMENT=ttHJets_custom_ND-fragment.py
    setup_rel $REL $FRAGMENT
    CFGNAME=2023BPix_GEN-ttHJets_cfg.py
    cmsDriver.py Configuration/GenProduction/python/$FRAGMENT --mc --eventcontent RAWSIM --datatier GEN --conditions $CONDITIONS --beamspot $BEAMSPOT --step GEN --geometry DB:Extended --era $ERA --fileout file:$FOUT --filein file:$FIN --python_filename $CFGNAME --no_exec

    FRAGMENT=tllq4f_custom_ND-fragment.py
    setup_rel $REL $FRAGMENT
    CFGNAME=2023BPix_GEN-tllq4f_cfg.py
    cmsDriver.py Configuration/GenProduction/python/$FRAGMENT --mc --eventcontent RAWSIM --datatier GEN --conditions $CONDITIONS --beamspot $BEAMSPOT --step GEN --geometry DB:Extended --era $ERA --fileout file:$FOUT --filein file:$FIN --python_filename $CFGNAME --no_exec

    # SIM
    FIN=GEN-00000.root
    FOUT=SIM-00000.root
    CFGNAME=2023BPix_SIM_cfg.py
    cmsDriver.py step1 --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions $CONDITIONS --beamspot $BEAMSPOT --step SIM --geometry DB:Extended --era $ERA --filein file:$FIN --fileout file:$FOUT --python_filename $CFGNAME --no_exec

    # DRPremix step1
    FIN=SIM-00000.root
    FOUT=DIGI-00000.root
    CFGNAME=2023BPix_DIGI_cfg.py
    cmsDriver.py step1 --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions $CONDITIONS --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:2022v12 --procModifiers premix_stage2,siPixelQualityRawToDigi --nThreads 4 --geometry DB:Extended --datamix PreMix --era $ERA --filein file:$FIN --fileout file:$FOUT --pileup_input "$PU_INPUT" --python_filename $CFGNAME --no_exec
    
    # DRPremix step2
    FIN=DIGI-00000.root
    FOUT=RECO-00000.root
    CFGNAME=2023BPix_RECO_cfg.py
    cmsDriver.py step2 --mc --eventcontent AODSIM --datatier AODSIM --conditions $CONDITIONS --step RAW2DIGI,L1Reco,RECO,RECOSIM --procModifiers siPixelQualityRawToDigi --nThreads 4 --geometry DB:Extended --era $ERA --filein file:$FIN --fileout file:$FOUT --python_filename $CFGNAME --no_exec

    exit
)

# MAODv4
(
    cmssw-el9
    export SCRAM_ARCH=el9_amd64_gcc11

    REL=CMSSW_13_0_13
    FRAGMENT=baseline_custom_ND-fragment.py
    COMMON="step1 --mc --eventcontent MINIAODSIM --datatier MINIAODSIM --step PAT --nThreads 2 --geometry DB:Extended"
    FIN=RECO-00000.root
    FOUT=MAOD-00000.root

    # All use the same CMSSW release
    setup_rel $REL $FRAGMENT

    # 2022
    CFGNAME=2022_MAODv4_cfg.py
    CONDITIONS=130X_mcRun3_2022_realistic_v5
    ERA=Run3,run3_miniAOD_12X
    cmsDriver.py $COMMON --conditions $CONDITIONS --era $ERA --filein file:$FIN --fileout file:$FOUT

    # 2022EE
    CFGNAME=2022EE_MAODv4_cfg.py
    CONDITIONS=130X_mcRun3_2022_realistic_postEE_v6
    ERA=Run3,run3_miniAOD_12X
    cmsDriver.py $COMMON --conditions $CONDITIONS --era $ERA --filein file:$FIN --fileout file:$FOUT

    # 2023
    CFGNAME=2023_MAODv4_cfg.py
    CONDITIONS=130X_mcRun3_2023_realistic_v14
    ERA=Run3_2023
    cmsDriver.py $COMMON --conditions $CONDITIONS --era $ERA --filein file:$FIN --fileout file:$FOUT

    # 2023BPix
    CFGNAME=2023BPix_MAODv4_cfg.py
    CONDITIONS=130X_mcRun3_2023_realistic_postBPix_v2
    ERA=Run3_2023
    cmsDriver.py $COMMON --conditions $CONDITIONS --era $ERA --filein file:$FIN --fileout file:$FOUT

    exit
)

# NAODv12
(
    cmssw-el9
    export SCRAM_ARCH=el9_amd64_gcc11

    REL=CMSSW_13_0_13
    FRAGMENT=baseline_custom_ND-fragment.py
    COMMON="--mc --eventcontent NANOEDMAODSIM --datatier NANOAODSIM --step NANO --nThreads 4 --scenario pp"
    FIN=MAOD-00000.root
    FOUT=NAOD-00000.root

    # All use the same CMSSW release
    setup_rel $REL $FRAGMENT

    # 2022
    CFGNAME=2022_NAODv12_cfg.py
    CONDITIONS=130X_mcRun3_2022_realistic_v5
    ERA=Run3
    cmsDriver.py step1 $COMMON --conditions $CONDITIONS --era $ERA --filein file:$FOUT --fileout file:$FOUT

    # 2022EE
    CFGNAME=2022EE_NAODv12_cfg.py
    CONDITIONS=130X_mcRun3_2022_realistic_postEE_v6
    ERA=Run3
    cmsDriver.py step1 $COMMON --conditions $CONDITIONS --era $ERA --filein file:$FOUT --fileout file:$FOUT

    # 2023
    CFGNAME=2023_NAODv12_cfg.py
    CONDITIONS=130X_mcRun3_2023_realistic_v14
    ERA=Run3_2023
    cmsDriver.py step1 $COMMON --conditions $CONDITIONS --era $ERA --filein file:$FOUT --fileout file:$FIN

    # 2023BPix
    CFGNAME=2023BPix_NAODv12_cfg.py
    CONDITIONS=130X_mcRun3_2023_realistic_postBPix_v2
    ERA=Run3_2023
    cmsDriver.py step1 $COMMON --conditions $CONDITIONS --era $ERA --filein file:$FOUT --fileout file:$FIN

    exit
)