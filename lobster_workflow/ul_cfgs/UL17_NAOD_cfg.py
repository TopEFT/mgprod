# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/ttgamma_custom_ND-fragment.py --python_filename UL17_NAOD_cfg.py --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --filein file:MAOD-00000.root --fileout file:NAOD-00000.root --conditions 106X_mc2017_realistic_v9 --step NANO --geometry DB:Extended --era Run2_2017,run2_nanoAOD_106Xv2 --no_exec --mc -n -1
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2017_cff import Run2_2017
from Configuration.Eras.Modifier_run2_nanoAOD_106Xv2_cff import run2_nanoAOD_106Xv2

import os
envOverride = {}
if 'HOME' not in os.environ:
    envOverride['HOME'] = os.environ.get('PWD', "/")
os.environ.update(envOverride)

process = cms.Process('NANO',Run2_2017,run2_nanoAOD_106Xv2)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:MAOD-00000.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/ttgamma_custom_ND-fragment.py nevts:-1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOAODSIMoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAODSIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:NAOD-00000.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_mc2017_realistic_v9', '')

# Path and EndPath definitions
process.nanoAOD_step = cms.Path(process.nanoSequenceMC)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODSIMoutput_step = cms.EndPath(process.NANOAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOAODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nano_cff
from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeMC 

#call to customisation function nanoAOD_customizeMC imported from PhysicsTools.NanoAOD.nano_cff
process = nanoAOD_customizeMC(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
named_weights = [
"dummy_point",
"EFTrwgt0_ctW_-0.16245_ctq1_1.304017_cpQM_54.332225_cQq81_-4.350409_ctZ_2.643432_cQq83_-1.984127_ctG_0.245977_ctq8_2.134686_cQq13_-2.402022_cQq11_-0.857068_cpt_27.974273",
"EFTrwgt1_ctW_-1.297318_ctq1_-0.598118_cpQM_-18.388237_cQq81_2.46948_ctZ_-3.755554_cQq83_-2.365753_ctG_-0.468947_ctq8_0.351589_cQq13_-1.616981_cQq11_-1.371493_cpt_12.440879",
"EFTrwgt2_ctW_0.009839_ctq1_-0.567511_cpQM_34.23499_cQq81_0.209877_ctZ_-3.259964_cQq83_1.718653_ctG_-0.02887_ctq8_-3.058625_cQq13_-0.278037_cQq11_2.283426_cpt_27.803314",
"EFTrwgt3_ctW_2.162523_ctq1_-0.541379_cpQM_104.490663_cQq81_1.539269_ctZ_1.507844_cQq83_2.743164_ctG_0.127235_ctq8_-3.122216_cQq13_-1.20984_cQq11_0.759695_cpt_-19.63625",
"EFTrwgt4_ctW_-2.373728_ctq1_-0.043402_cpQM_39.315675_cQq81_0.510381_ctZ_-1.30657_cQq83_0.081747_ctG_-0.310666_ctq8_-0.697642_cQq13_0.306642_cQq11_-0.767205_cpt_9.395289",
"EFTrwgt5_ctW_0.454719_ctq1_-0.35858_cpQM_25.695691_cQq81_-1.677035_ctZ_-2.868666_cQq83_3.072346_ctG_0.324845_ctq8_0.680812_cQq13_-1.48552_cQq11_0.910132_cpt_-57.992185",
"EFTrwgt6_ctW_-0.390252_ctq1_1.358411_cpQM_-61.748384_cQq81_-0.020251_ctZ_-0.913267_cQq83_-0.473457_ctG_-0.497783_ctq8_-1.853907_cQq13_-1.562943_cQq11_-0.587927_cpt_16.540402",
"EFTrwgt7_ctW_2.072889_ctq1_1.552031_cpQM_6.166782_cQq81_0.71867_ctZ_0.336713_cQq83_-2.459509_ctG_0.144516_ctq8_-0.277088_cQq13_1.304464_cQq11_-0.563029_cpt_-13.927906",
"EFTrwgt8_ctW_1.64292_ctq1_1.882947_cpQM_-96.065571_cQq81_1.082634_ctZ_4.088112_cQq83_4.01347_ctG_-0.117676_ctq8_2.526408_cQq13_-0.789104_cQq11_-1.141798_cpt_-1.634585",
"EFTrwgt9_ctW_1.137711_ctq1_1.937192_cpQM_99.879208_cQq81_-2.664685_ctZ_0.31067_cQq83_0.957434_ctG_0.172274_ctq8_2.580641_cQq13_-1.212765_cQq11_-2.209526_cpt_8.516787",
"EFTrwgt10_ctW_2.236307_ctq1_-1.976541_cpQM_25.839224_cQq81_0.647943_ctZ_-3.610594_cQq83_1.351363_ctG_0.304926_ctq8_3.635738_cQq13_1.98117_cQq11_1.626699_cpt_-27.696694",
"EFTrwgt11_ctW_-2.635933_ctq1_1.622038_cpQM_36.059318_cQq81_-4.211413_ctZ_3.608153_cQq83_-2.195369_ctG_-0.349908_ctq8_3.137254_cQq13_-1.139053_cQq11_1.789837_cpt_-40.454977",
"EFTrwgt12_ctW_-2.592319_ctq1_-0.11027_cpQM_-29.559146_cQq81_-0.864302_ctZ_2.953632_cQq83_1.455632_ctG_-0.150548_ctq8_3.202221_cQq13_-1.797859_cQq11_-0.50874_cpt_23.81046",
"EFTrwgt13_ctW_2.333052_ctq1_0.326554_cpQM_30.845972_cQq81_4.213714_ctZ_4.10844_cQq83_-1.399543_ctG_0.274457_ctq8_2.46887_cQq13_-0.273645_cQq11_-1.680074_cpt_56.214048",
"EFTrwgt14_ctW_-1.324232_ctq1_-0.797335_cpQM_40.570962_cQq81_-1.343967_ctZ_-3.799167_cQq83_-1.924801_ctG_0.548449_ctq8_-0.648011_cQq13_-2.288337_cQq11_0.849546_cpt_-58.911062",
"EFTrwgt15_ctW_1.80072_ctq1_-0.677994_cpQM_-14.027402_cQq81_-0.919533_ctZ_-3.803558_cQq83_1.436348_ctG_0.126926_ctq8_0.707206_cQq13_-0.606089_cQq11_-0.21032_cpt_-38.519789",
"EFTrwgt16_ctW_-2.405898_ctq1_-0.04465_cpQM_37.614873_cQq81_-4.242658_ctZ_-0.000455_cQq83_0.542708_ctG_-0.349527_ctq8_-0.086737_cQq13_-2.375045_cQq11_-1.671169_cpt_29.198461",
"EFTrwgt17_ctW_0.014982_ctq1_-1.849728_cpQM_62.176008_cQq81_3.905289_ctZ_-3.95353_cQq83_2.332114_ctG_-0.460705_ctq8_2.472076_cQq13_0.312145_cQq11_0.541059_cpt_5.078345",
"EFTrwgt18_ctW_-1.930909_ctq1_1.16411_cpQM_-50.571377_cQq81_-3.359645_ctZ_-1.176952_cQq83_0.329283_ctG_-0.489294_ctq8_-1.747801_cQq13_0.938494_cQq11_0.243506_cpt_-19.895396",
"EFTrwgt19_ctW_1.856778_ctq1_-0.09075_cpQM_66.864873_cQq81_-4.153403_ctZ_2.255188_cQq83_-4.770706_ctG_0.489556_ctq8_-3.22163_cQq13_0.279301_cQq11_-0.134529_cpt_11.02314",
"EFTrwgt20_ctW_2.784795_ctq1_-1.846581_cpQM_50.506641_cQq81_3.709185_ctZ_-2.709796_cQq83_2.997379_ctG_-0.455894_ctq8_0.733119_cQq13_-1.627006_cQq11_-0.13142_cpt_45.575761",
"EFTrwgt21_ctW_0.971847_ctq1_-1.936442_cpQM_-106.825033_cQq81_-3.231366_ctZ_1.18192_cQq83_-4.785439_ctG_-0.469172_ctq8_2.868231_cQq13_1.358905_cQq11_-1.159387_cpt_-30.843549",
"EFTrwgt22_ctW_1.840684_ctq1_1.070337_cpQM_-89.515632_cQq81_2.776799_ctZ_0.439561_cQq83_2.636557_ctG_-0.487392_ctq8_2.631527_cQq13_1.116319_cQq11_1.993128_cpt_-42.92889",
"EFTrwgt23_ctW_-1.854013_ctq1_-1.914017_cpQM_31.611283_cQq81_3.554465_ctZ_-4.16482_cQq83_-1.629055_ctG_0.215949_ctq8_0.546521_cQq13_2.035081_cQq11_-0.246841_cpt_32.294118",
"EFTrwgt24_ctW_-1.865528_ctq1_-1.235808_cpQM_50.514829_cQq81_-0.297463_ctZ_-2.739714_cQq83_-3.483445_ctG_0.159005_ctq8_2.168766_cQq13_1.908592_cQq11_-0.294178_cpt_-55.881995",
"EFTrwgt25_ctW_-0.502461_ctq1_0.860667_cpQM_109.989193_cQq81_0.11795_ctZ_1.054362_cQq83_4.664871_ctG_0.082831_ctq8_2.412608_cQq13_1.371768_cQq11_-1.902203_cpt_-37.425269",
"EFTrwgt26_ctW_-1.082742_ctq1_1.97824_cpQM_-92.140974_cQq81_1.690379_ctZ_-3.000371_cQq83_-1.819492_ctG_-0.190702_ctq8_-0.83025_cQq13_-0.599629_cQq11_0.888209_cpt_14.035087",
"EFTrwgt27_ctW_2.758342_ctq1_1.244606_cpQM_33.462863_cQq81_1.819385_ctZ_-2.480981_cQq83_2.331647_ctG_-0.067468_ctq8_-2.892416_cQq13_-1.360244_cQq11_-1.375957_cpt_-29.131182",
"EFTrwgt28_ctW_-1.005878_ctq1_-2.089979_cpQM_-88.525026_cQq81_-1.006615_ctZ_-0.956304_cQq83_-1.339555_ctG_0.489778_ctq8_-3.420854_cQq13_-1.079041_cQq11_-1.016953_cpt_-57.615843",
"EFTrwgt29_ctW_-1.624069_ctq1_1.147758_cpQM_62.397537_cQq81_-2.041506_ctZ_1.521411_cQq83_-3.138322_ctG_-0.47304_ctq8_0.71336_cQq13_1.883218_cQq11_2.330439_cpt_18.291596",
"EFTrwgt30_ctW_-1.64657_ctq1_0.647895_cpQM_46.280835_cQq81_1.366158_ctZ_-0.330418_cQq83_-0.566046_ctG_-0.401189_ctq8_3.123163_cQq13_2.075639_cQq11_1.270483_cpt_-30.319009",
"EFTrwgt31_ctW_-2.416089_ctq1_1.348194_cpQM_102.667923_cQq81_-0.138568_ctZ_-3.194163_cQq83_-0.16405_ctG_-0.305917_ctq8_1.934516_cQq13_-1.251484_cQq11_2.108554_cpt_44.215848",
"EFTrwgt32_ctW_0.039424_ctq1_-1.877176_cpQM_91.312316_cQq81_4.319439_ctZ_3.768898_cQq83_-0.151831_ctG_0.429042_ctq8_-2.42907_cQq13_-1.528083_cQq11_0.577124_cpt_-1.346214",
"EFTrwgt33_ctW_1.201285_ctq1_-2.117435_cpQM_85.499129_cQq81_0.383177_ctZ_-3.033742_cQq83_-3.618676_ctG_0.057469_ctq8_-0.590398_cQq13_-2.329333_cQq11_2.251544_cpt_-22.977813",
"EFTrwgt34_ctW_0.451879_ctq1_-1.357292_cpQM_100.213084_cQq81_3.758352_ctZ_-3.072257_cQq83_3.384212_ctG_0.394772_ctq8_-0.356256_cQq13_2.283127_cQq11_0.763845_cpt_-52.613356",
"EFTrwgt35_ctW_-0.62955_ctq1_0.421672_cpQM_-82.410999_cQq81_2.921447_ctZ_-0.174602_cQq83_-3.793285_ctG_-0.007805_ctq8_2.839934_cQq13_-0.172306_cQq11_-2.421189_cpt_-47.622286",
"EFTrwgt36_ctW_1.720812_ctq1_-1.696816_cpQM_88.550816_cQq81_1.775882_ctZ_1.580215_cQq83_-1.008881_ctG_-0.26604_ctq8_-1.194294_cQq13_0.099256_cQq11_-0.999979_cpt_-16.201958",
"EFTrwgt37_ctW_2.691069_ctq1_-0.398344_cpQM_42.798763_cQq81_-3.328809_ctZ_-0.598714_cQq83_0.141483_ctG_0.25428_ctq8_-0.476726_cQq13_0.870371_cQq11_1.167203_cpt_16.333174",
"EFTrwgt38_ctW_1.501691_ctq1_2.13849_cpQM_53.670643_cQq81_1.928223_ctZ_-4.485624_cQq83_-3.904765_ctG_0.330642_ctq8_-1.288522_cQq13_0.59375_cQq11_-1.751252_cpt_2.779853",
"EFTrwgt39_ctW_1.47742_ctq1_0.716607_cpQM_-81.326617_cQq81_3.372066_ctZ_4.477895_cQq83_4.888338_ctG_-0.241264_ctq8_1.684046_cQq13_1.772767_cQq11_0.947182_cpt_-30.601389",
"EFTrwgt40_ctW_-2.765515_ctq1_0.256945_cpQM_72.384686_cQq81_3.768729_ctZ_2.089977_cQq83_2.95488_ctG_-0.306021_ctq8_-1.090487_cQq13_2.210539_cQq11_1.856163_cpt_-3.080267",
"EFTrwgt41_ctW_-2.059745_ctq1_-1.026193_cpQM_92.67082_cQq81_0.035686_ctZ_0.548045_cQq83_2.374414_ctG_0.42421_ctq8_0.622961_cQq13_0.72192_cQq11_0.458647_cpt_56.277062",
"EFTrwgt42_ctW_-0.339137_ctq1_0.726266_cpQM_23.094832_cQq81_-3.210599_ctZ_-0.928656_cQq83_-0.303169_ctG_0.226975_ctq8_-1.884483_cQq13_-1.195663_cQq11_-1.5971_cpt_27.703159",
"EFTrwgt43_ctW_0.72634_ctq1_-1.741812_cpQM_31.805087_cQq81_3.214778_ctZ_0.466011_cQq83_2.118199_ctG_0.474219_ctq8_2.176324_cQq13_1.846005_cQq11_0.628894_cpt_7.539509",
"EFTrwgt44_ctW_2.152953_ctq1_1.265844_cpQM_77.179153_cQq81_-0.090919_ctZ_3.962811_cQq83_0.064698_ctG_0.184365_ctq8_-3.283826_cQq13_-0.669421_cQq11_1.702434_cpt_-2.440148",
"EFTrwgt45_ctW_0.619067_ctq1_-1.001255_cpQM_3.32818_cQq81_1.760842_ctZ_1.551092_cQq83_-0.787589_ctG_0.205938_ctq8_-2.200091_cQq13_-1.379596_cQq11_-1.011474_cpt_57.769931",
"EFTrwgt46_ctW_0.219392_ctq1_-1.511099_cpQM_-11.652713_cQq81_0.425457_ctZ_3.937921_cQq83_0.254819_ctG_0.069591_ctq8_-0.702966_cQq13_-2.238194_cQq11_2.073553_cpt_-48.55572",
"EFTrwgt47_ctW_1.835929_ctq1_0.692001_cpQM_82.26727_cQq81_-1.598964_ctZ_1.217169_cQq83_-0.754397_ctG_0.34955_ctq8_-1.874995_cQq13_-1.062411_cQq11_1.625879_cpt_-41.328193",
"EFTrwgt48_ctW_2.806848_ctq1_-1.184752_cpQM_-103.836567_cQq81_-4.215133_ctZ_0.087075_cQq83_-3.991513_ctG_-0.190217_ctq8_1.433862_cQq13_-1.72213_cQq11_1.790052_cpt_37.540596",
"EFTrwgt49_ctW_1.72689_ctq1_-0.512793_cpQM_-90.348171_cQq81_-2.044811_ctZ_4.126778_cQq83_0.412108_ctG_0.302064_ctq8_0.715003_cQq13_1.038163_cQq11_-1.75289_cpt_-45.690415",
"EFTrwgt50_ctW_-1.993276_ctq1_-1.57414_cpQM_80.696131_cQq81_-1.347646_ctZ_-1.799942_cQq83_4.176308_ctG_0.07224_ctq8_-1.709055_cQq13_-1.23745_cQq11_1.727025_cpt_-15.502136",
"EFTrwgt51_ctW_0.097021_ctq1_1.460888_cpQM_77.006065_cQq81_2.855513_ctZ_0.707779_cQq83_0.498632_ctG_-0.127799_ctq8_2.949634_cQq13_-0.732746_cQq11_-0.329988_cpt_-21.534647",
"EFTrwgt52_ctW_2.446243_ctq1_-1.162549_cpQM_48.810218_cQq81_2.749855_ctZ_1.496297_cQq83_0.454651_ctG_0.532326_ctq8_2.033457_cQq13_-2.250151_cQq11_0.541947_cpt_-50.619305",
"EFTrwgt53_ctW_2.512767_ctq1_-0.244017_cpQM_4.259919_cQq81_-4.242976_ctZ_1.997292_cQq83_-0.88833_ctG_-0.431671_ctq8_-0.23777_cQq13_-2.156746_cQq11_-0.716064_cpt_24.523105",
"EFTrwgt54_ctW_-2.12621_ctq1_1.568933_cpQM_88.778789_cQq81_-3.859994_ctZ_-4.389785_cQq83_4.426213_ctG_-0.21525_ctq8_-3.616162_cQq13_-0.781531_cQq11_-0.550108_cpt_20.635122",
"EFTrwgt55_ctW_2.791293_ctq1_-1.545816_cpQM_-24.723381_cQq81_1.206369_ctZ_1.060133_cQq83_-1.73707_ctG_0.186547_ctq8_-1.9841_cQq13_-1.936208_cQq11_-0.415_cpt_44.816028",
"EFTrwgt56_ctW_2.622276_ctq1_0.543482_cpQM_-41.797621_cQq81_-3.981678_ctZ_0.446493_cQq83_-0.522484_ctG_0.556407_ctq8_-0.478169_cQq13_2.029752_cQq11_-0.090587_cpt_6.905872",
"EFTrwgt57_ctW_-0.897093_ctq1_1.311132_cpQM_68.749217_cQq81_0.561907_ctZ_4.136291_cQq83_-4.205789_ctG_-0.240374_ctq8_-3.514358_cQq13_0.683221_cQq11_0.676994_cpt_12.41834",
"EFTrwgt58_ctW_-1.327393_ctq1_-0.352251_cpQM_43.388852_cQq81_1.614421_ctZ_0.156408_cQq83_-2.37545_ctG_0.317068_ctq8_-0.413349_cQq13_2.188493_cQq11_1.84056_cpt_-47.845978",
"EFTrwgt59_ctW_-1.30898_ctq1_-0.566015_cpQM_29.908105_cQq81_0.569781_ctZ_3.700817_cQq83_-4.572927_ctG_0.12214_ctq8_2.257588_cQq13_0.975263_cQq11_-0.219551_cpt_9.476736",
"EFTrwgt60_ctW_-0.420295_ctq1_1.502536_cpQM_74.641999_cQq81_-3.283783_ctZ_4.138897_cQq83_-0.019471_ctG_-0.312553_ctq8_0.131618_cQq13_-0.221762_cQq11_0.912787_cpt_47.048099",
"EFTrwgt61_ctW_-0.7852_ctq1_-0.847365_cpQM_-72.398031_cQq81_-1.606772_ctZ_-1.211654_cQq83_2.112586_ctG_-0.007274_ctq8_-0.962473_cQq13_2.083096_cQq11_-1.306995_cpt_-36.930191",
"EFTrwgt62_ctW_-2.322079_ctq1_0.059459_cpQM_-6.631693_cQq81_-0.925117_ctZ_3.929508_cQq83_1.729173_ctG_-0.27651_ctq8_-1.278206_cQq13_-0.210605_cQq11_-1.505337_cpt_-1.786385",
"EFTrwgt63_ctW_2.262101_ctq1_2.107264_cpQM_2.312071_cQq81_-3.853934_ctZ_-3.652483_cQq83_-2.701154_ctG_-0.286443_ctq8_-1.114796_cQq13_1.995843_cQq11_2.427202_cpt_-47.418615",
"EFTrwgt64_ctW_1.001653_ctq1_1.335837_cpQM_87.236882_cQq81_0.083658_ctZ_-2.282979_cQq83_1.052152_ctG_0.420455_ctq8_3.012854_cQq13_1.989038_cQq11_0.42084_cpt_7.165793",
"EFTrwgt65_ctW_1.835685_ctq1_2.024257_cpQM_100.442596_cQq81_3.386039_ctZ_-1.883207_cQq83_1.353038_ctG_-0.466567_ctq8_2.73031_cQq13_-1.389841_cQq11_0.699002_cpt_-54.407403",
"EFTrwgt66_ctW_2.636588_ctq1_-1.361568_cpQM_74.576815_cQq81_0.903828_ctZ_3.811544_cQq83_-1.659434_ctG_0.143056_ctq8_0.609379_cQq13_-0.403458_cQq11_-1.015016_cpt_-41.728143",
"EFTrwgt67_ctW_-1.319847_ctq1_-1.290013_cpQM_32.794377_cQq81_-0.007684_ctZ_-2.459265_cQq83_-1.786402_ctG_0.23487_ctq8_-2.412255_cQq13_-2.166239_cQq11_-1.014964_cpt_33.401697",
"EFTrwgt68_ctW_-1.619302_ctq1_-1.135357_cpQM_3.201763_cQq81_4.014855_ctZ_-3.438943_cQq83_3.768074_ctG_0.060653_ctq8_1.142254_cQq13_-1.60296_cQq11_1.19429_cpt_-11.119373",
"EFTrwgt69_ctW_-1.323948_ctq1_-1.223788_cpQM_78.197745_cQq81_-2.986354_ctZ_-3.865269_cQq83_-2.862333_ctG_0.430082_ctq8_2.560563_cQq13_0.677728_cQq11_1.495989_cpt_-37.790729",
"EFTrwgt70_ctW_-0.591645_ctq1_0.5008_cpQM_-64.704711_cQq81_-3.584259_ctZ_-2.412439_cQq83_1.613097_ctG_0.377978_ctq8_0.447085_cQq13_0.155649_cQq11_-1.232682_cpt_55.797354",
"EFTrwgt71_ctW_1.45124_ctq1_-1.007718_cpQM_-11.448208_cQq81_-1.037692_ctZ_-2.565506_cQq83_0.998683_ctG_0.343448_ctq8_-2.606427_cQq13_-1.898299_cQq11_-0.561965_cpt_-13.060504",
"EFTrwgt72_ctW_1.396947_ctq1_1.279369_cpQM_-105.0842_cQq81_2.683615_ctZ_-4.303924_cQq83_-1.03177_ctG_0.010027_ctq8_3.1352_cQq13_0.472026_cQq11_2.228299_cpt_29.143636",
"EFTrwgt73_ctW_-0.61945_ctq1_0.770749_cpQM_-1.190503_cQq81_-0.654227_ctZ_-0.960873_cQq83_0.636947_ctG_0.028977_ctq8_-0.027851_cQq13_-2.377413_cQq11_-1.066718_cpt_13.883975",
"EFTrwgt74_ctW_2.307767_ctq1_1.917003_cpQM_-8.885499_cQq81_-2.411016_ctZ_3.45322_cQq83_0.28811_ctG_0.255227_ctq8_-1.740448_cQq13_-0.159334_cQq11_-1.932983_cpt_-12.515901",
"EFTrwgt75_ctW_-0.615986_ctq1_-0.619804_cpQM_8.967051_cQq81_2.93285_ctZ_-2.223642_cQq83_4.944356_ctG_-0.394648_ctq8_1.831894_cQq13_1.500919_cQq11_0.603406_cpt_-12.30319",
"EFTrwgt76_ctW_2.688956_ctq1_1.72426_cpQM_-17.239657_cQq81_-2.437576_ctZ_2.439383_cQq83_0.637111_ctG_0.403187_ctq8_2.815428_cQq13_-1.749258_cQq11_-1.655429_cpt_-27.495456",
"EFTrwgt77_ctW_2.026817_ctq1_-0.836338_cpQM_51.836308_cQq81_1.0395_ctZ_0.777762_cQq83_-0.318817_ctG_0.05272_ctq8_-0.758307_cQq13_-0.350384_cQq11_0.411143_cpt_-5.009765",
"EFTrwgt78_ctW_2.830824_ctq1_-0.051242_cpQM_-11.088574_cQq81_-0.003055_ctZ_1.123669_cQq83_-4.491581_ctG_-0.266156_ctq8_-3.620633_cQq13_1.447288_cQq11_0.697661_cpt_36.638482",
"EFTrwgt79_ctW_-2.414037_ctq1_-0.069126_cpQM_-50.929022_cQq81_1.100513_ctZ_4.270487_cQq83_-3.411685_ctG_-0.386276_ctq8_-0.229591_cQq13_1.175226_cQq11_2.260528_cpt_-26.587302",
"EFTrwgt80_ctW_0.123012_ctq1_-1.925375_cpQM_63.321569_cQq81_-3.24007_ctZ_1.30941_cQq83_4.79549_ctG_0.518687_ctq8_0.3531_cQq13_0.161362_cQq11_-0.100574_cpt_38.562012",
"EFTrwgt81_ctW_2.320828_ctq1_0.904378_cpQM_56.409806_cQq81_2.127197_ctZ_-2.686487_cQq83_-3.261195_ctG_-0.290293_ctq8_-3.472011_cQq13_-2.328137_cQq11_1.53763_cpt_-52.01013",
"EFTrwgt82_ctW_-2.079452_ctq1_-1.993574_cpQM_-102.493689_cQq81_-1.696196_ctZ_-1.665486_cQq83_-2.021804_ctG_-0.307742_ctq8_-1.624141_cQq13_2.003721_cQq11_1.24282_cpt_-55.815836",
"EFTrwgt83_ctW_2.577951_ctq1_0.120515_cpQM_-63.121406_cQq81_-0.807094_ctZ_2.163942_cQq83_4.463206_ctG_-0.508893_ctq8_1.476251_cQq13_-0.040435_cQq11_-0.449776_cpt_1.845994",
"EFTrwgt84_ctW_2.650081_ctq1_1.827702_cpQM_16.562006_cQq81_2.050632_ctZ_1.841398_cQq83_-4.761442_ctG_0.377873_ctq8_-0.75913_cQq13_2.120747_cQq11_0.891991_cpt_-21.407885",
"EFTrwgt85_ctW_2.751044_ctq1_-1.019858_cpQM_62.421197_cQq81_-2.689145_ctZ_-1.419972_cQq83_-1.69879_ctG_0.331688_ctq8_-2.465612_cQq13_-1.040774_cQq11_-1.765293_cpt_-15.212984",
"EFTrwgt86_ctW_2.405946_ctq1_1.144113_cpQM_-74.365223_cQq81_-2.026017_ctZ_-0.803148_cQq83_1.379116_ctG_-0.419214_ctq8_-1.068765_cQq13_0.561148_cQq11_1.162244_cpt_-32.933598",
"EFTrwgt87_ctW_-1.442597_ctq1_-0.43251_cpQM_82.988034_cQq81_0.253702_ctZ_-1.07293_cQq83_2.525373_ctG_0.056288_ctq8_0.123376_cQq13_-1.065924_cQq11_0.165163_cpt_29.392141",
"EFTrwgt88_ctW_0.164876_ctq1_-1.689242_cpQM_107.616171_cQq81_1.124793_ctZ_3.341765_cQq83_-2.791928_ctG_-0.163976_ctq8_1.257676_cQq13_1.696878_cQq11_1.709262_cpt_-30.917084",
"EFTrwgt89_ctW_-2.337783_ctq1_-0.714434_cpQM_-63.670486_cQq81_3.238774_ctZ_-3.595536_cQq83_-1.9822_ctG_0.12202_ctq8_2.160168_cQq13_0.931712_cQq11_0.863855_cpt_-22.038371",
"EFTrwgt90_ctW_0.801544_ctq1_-1.182374_cpQM_-64.251067_cQq81_4.245204_ctZ_4.563175_cQq83_4.51754_ctG_-0.106507_ctq8_-1.522158_cQq13_0.507611_cQq11_-0.894452_cpt_-27.365295",
"EFTrwgt91_ctW_-0.347924_ctq1_1.109701_cpQM_-81.647939_cQq81_-2.641106_ctZ_3.918178_cQq83_-1.715963_ctG_-0.533335_ctq8_-1.112604_cQq13_0.565921_cQq11_0.569334_cpt_-41.902587",
"EFTrwgt92_ctW_2.761246_ctq1_-1.191196_cpQM_98.969753_cQq81_-0.478348_ctZ_-1.363954_cQq83_1.536194_ctG_0.410772_ctq8_0.679164_cQq13_-0.682814_cQq11_2.188621_cpt_31.906238",
"EFTrwgt93_ctW_0.0_ctq1_0.0_cpQM_0.0_cQq81_0.0_ctZ_0.0_cQq83_0.0_ctG_0.0_ctq8_0.0_cQq13_0.0_cQq11_0.0_cpt_0.0",
]
process.genWeightsTable.namedWeightIDs = named_weights
process.genWeightsTable.namedWeightLabels = named_weights
