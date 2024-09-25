# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/SMP-RunIISummer20UL16wmLHEGENAPV-00001-fragment.py --filein file:yourFile.root --fileout testNano.root --mc --eventcontent NANOAODGEN --datatier NANOAODSIM --conditions auto:mc --step GEN,NANOGEN --nThreads 4 --python_filename nanGenConfig.py --no_exec -n -1
import FWCore.ParameterSet.Config as cms



process = cms.Process('NANOGEN')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic50ns13TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('PhysicsTools.NanoAOD.nanogen_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring('file:LHE-00000.root'),
    #fileNames = cms.untracked.vstring('file:LHE-00000.root'),
    inputCommands = cms.untracked.vstring(
        'keep *', 
        'drop LHEXMLStringProduct_*_*_*'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('/afs/crc.nd.edu/user/b/byates2/mgprod/lobster_workflow/fragments/ttgamma_custom_ND-fragment.py'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOAODGENoutput = cms.OutputModule("NanoAODOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAODSIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('testNano.root'),
    outputCommands = process.NANOAODGENEventContent.outputCommands
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:mc', '')
process.generator = cms.EDFilter("Pythia8HadronizerFilter",
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring(
            'pythia8CommonSettings', 
            'pythia8CP5Settings', 
            'processParameters'
        ),
        processParameters = cms.vstring(
            'JetMatching:setMad = off', 
            'JetMatching:scheme = 1', 
            'JetMatching:merge = on', 
            'JetMatching:jetAlgorithm = 2', 
            'JetMatching:etaJetMax = 999.', 
            'JetMatching:coneRadius = 1.', 
            'JetMatching:slowJetPower = 1', 
            'JetMatching:qCut = 20.', 
            'JetMatching:nQmatch = 5', 
            'JetMatching:nJetMax = 1', 
            'JetMatching:doShowerKt = off', 
            'TimeShower:mMaxGamma = 4.0', 
            'UncertaintyBands:doVariations = on', 
            'UncertaintyBands:List = {isrRedHi isr:muRfac=0.707,fsrRedHi fsr:muRfac=0.707,isrRedLo isr:muRfac=1.414,fsrRedLo fsr:muRfac=1.414,isrDefHi isr:muRfac=0.5, fsrDefHi fsr:muRfac=0.5,isrDefLo isr:muRfac=2.0,fsrDefLo fsr:muRfac=2.0,isrConHi isr:muRfac=0.25, fsrConHi fsr:muRfac=0.25,isrConLo isr:muRfac=4.0,fsrConLo fsr:muRfac=4.0}', 
            'UncertaintyBands:MPIshowers = on', 
            'UncertaintyBands:overSampleFSR = 10.0', 
            'UncertaintyBands:overSampleISR = 10.0', 
            'UncertaintyBands:FSRpTmin2Fac = 20', 
            'UncertaintyBands:ISRpTmin2Fac = 1'
        ),
        pythia8CP5Settings = cms.vstring(
            'Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:ecmPow=0.03344', 
            'MultipartonInteractions:bProfile=2', 
            'MultipartonInteractions:pT0Ref=1.41', 
            'MultipartonInteractions:coreRadius=0.7634', 
            'MultipartonInteractions:coreFraction=0.63', 
            'ColourReconnection:range=5.176', 
            'SigmaTotal:zeroAXB=off', 
            'SpaceShower:alphaSorder=2', 
            'SpaceShower:alphaSvalue=0.118', 
            'SigmaProcess:alphaSvalue=0.118', 
            'SigmaProcess:alphaSorder=2', 
            'MultipartonInteractions:alphaSvalue=0.118', 
            'MultipartonInteractions:alphaSorder=2', 
            'TimeShower:alphaSorder=2', 
            'TimeShower:alphaSvalue=0.118', 
            'SigmaTotal:mode = 0', 
            'SigmaTotal:sigmaEl = 21.89', 
            'SigmaTotal:sigmaTot = 100.309', 
            'PDF:pSet=LHAPDF6:NNPDF31_nnlo_as_0118'
        ),
        pythia8CommonSettings = cms.vstring(
            'Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on'
        )
    ),
    comEnergy = cms.double(13000.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.nanoAOD_step = cms.Path(process.nanogenSequence)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODGENoutput_step = cms.EndPath(process.NANOAODGENoutput)

process.load("EFTGenReader.LHEReader.EFTLHEReader_cfi")
process.EFTLHEReader.min_pt_jet  = cms.double(-1)
process.EFTLHEReader.min_pt_lep  = cms.double(-1)
process.EFTLHEReader.max_eta_jet = cms.double(2.5)
process.EFTLHEReader.max_eta_lep = cms.double(2.5)
process.EFTLHEReader.is4fScheme = cms.bool(False)

process.EFTLHEReader.GenParticles = cms.InputTag("genParticles")
process.EFTLHEReader.GenJets      = cms.InputTag("ak4GenJets")

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.nanoAOD_step,process.endjob_step,process.NANOAODGENoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path).insert(0, process.generator)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(4)
process.options.numberOfStreams=cms.untracked.uint32(0)
process.options.numberOfConcurrentLuminosityBlocks=cms.untracked.uint32(1)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nanogen_cff
from PhysicsTools.NanoAOD.nanogen_cff import customizeNanoGEN 

#call to customisation function customizeNanoGEN imported from PhysicsTools.NanoAOD.nanogen_cff
process = customizeNanoGEN(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
named_weights = [
"dummy_point",
"EFTrwgt0_ctlTi_-1.186157_ctq1_1.043744_ctq8_0.156087_cQq83_-0.132766_cQQ1_-28.314236_cQt1_-154.754592_cQt8_-10.088065_ctli_2.523097_cQq81_1.283575_cQlMi_7.389211_cbW_8.694071_cpQ3_-10.153017_ctei_-8.232308_cQei_-9.519405_ctW_2.626174_cpQM_1.080403_ctlSi_-5.458784_ctZ_-0.926101_cQl3i_-2.015518_ctG_0.348264_cQq13_-0.394787_cQq11_0.397674_cptb_36.427294_ctt1_-138.644498_ctp_145.735594_cpt_2.535175",
"EFTrwgt1_ctlTi_0.617575_ctq1_0.853168_ctq8_1.395444_cQq83_2.104024_cQQ1_-81.591281_cQt1_-47.260845_cQt8_77.159395_ctli_4.326184_cQq81_-0.671522_cQlMi_2.351492_cbW_-2.948531_cpQ3_7.42216_ctei_2.376752_cQei_-8.117603_ctW_0.131434_cpQM_1.167242_ctlSi_-6.695004_ctZ_0.569788_cQl3i_-4.18844_ctG_-0.035775_cQq13_0.388577_cQq11_0.680939_cptb_-17.615475_ctt1_159.292405_ctp_96.811178_cpt_-1.622798",
"EFTrwgt2_ctlTi_-1.41392_ctq1_-0.651966_ctq8_-1.486615_cQq83_2.10039_cQQ1_67.508822_cQt1_-164.609828_cQt8_-27.498836_ctli_-4.512791_cQq81_-0.411805_cQlMi_8.428333_cbW_3.456177_cpQ3_-7.713254_ctei_-1.641315_cQei_-11.146997_ctW_-0.019975_cpQM_-1.660626_ctlSi_10.658436_ctZ_-0.161041_cQl3i_5.40587_ctG_0.151752_cQq13_-0.303736_cQq11_-0.623131_cptb_8.023912_ctt1_-127.868357_ctp_-120.343875_cpt_-0.03569",
"EFTrwgt3_ctlTi_1.806498_ctq1_-0.192591_ctq8_-0.719985_cQq83_-1.923466_cQQ1_-10.101618_cQt1_118.708765_cQt8_-14.043393_ctli_1.214815_cQq81_1.341626_cQlMi_9.723215_cbW_-8.104848_cpQ3_8.177354_ctei_-0.500928_cQei_-5.272612_ctW_1.37705_cpQM_0.516897_ctlSi_-16.251245_ctZ_-1.531779_cQl3i_2.285592_ctG_0.181178_cQq13_-0.1842_cQq11_-0.554635_cptb_-34.607201_ctt1_-66.811637_ctp_-7.426853_cpt_-1.19164",
"EFTrwgt4_ctlTi_-1.858768_ctq1_0.944636_ctq8_-0.851889_cQq83_-0.983433_cQQ1_54.443094_cQt1_114.672073_cQt8_14.14351_ctli_-8.703349_cQq81_-0.076006_cQlMi_-0.386902_cbW_-0.144525_cpQ3_-9.241121_ctei_0.175757_cQei_9.692116_ctW_0.788895_cpQM_-0.6617_ctlSi_-9.728193_ctZ_-0.473113_cQl3i_-1.025302_ctG_0.344333_cQq13_-0.420058_cQq11_-0.180321_cptb_9.550963_ctt1_-162.645735_ctp_-147.52709_cpt_-2.487854",
"EFTrwgt5_ctlTi_-2.111406_ctq1_-0.350017_ctq8_-0.155736_cQq83_2.120534_cQQ1_-133.564035_cQt1_-130.71064_cQt8_-58.634799_ctli_2.768616_cQq81_-1.214031_cQlMi_1.448348_cbW_-11.224983_cpQ3_-8.654441_ctei_11.695348_cQei_-12.88184_ctW_0.548482_cpQM_0.846255_ctlSi_-11.579324_ctZ_-0.131562_cQl3i_5.621832_ctG_-0.03326_cQq13_0.049282_cQq11_0.849288_cptb_-25.307871_ctt1_-46.785903_ctp_-175.555626_cpt_-2.466879",
"EFTrwgt6_ctlTi_0.755399_ctq1_0.864524_ctq8_-1.390031_cQq83_0.221981_cQQ1_-86.077733_cQt1_-75.628974_cQt8_132.749362_ctli_7.722323_cQq81_-0.486241_cQlMi_-9.29505_cbW_10.376122_cpQ3_-13.836883_ctei_8.998601_cQei_-2.710594_ctW_1.605036_cpQM_-0.084861_ctlSi_17.253682_ctZ_1.280292_cQl3i_4.252956_ctG_-0.23375_cQq13_-0.371999_cQq11_-0.826254_cptb_-43.712451_ctt1_61.160061_ctp_28.69051_cpt_-2.506577",
"EFTrwgt7_ctlTi_-1.555159_ctq1_0.493334_ctq8_1.391866_cQq83_-0.532819_cQQ1_152.552304_cQt1_28.742218_cQt8_-46.035424_ctli_-1.025342_cQq81_-1.384664_cQlMi_9.773105_cbW_3.779446_cpQ3_12.842612_ctei_4.153507_cQei_12.02902_ctW_-0.714541_cpQM_0.882084_ctlSi_11.726174_ctZ_1.265865_cQl3i_4.502313_ctG_0.263911_cQq13_-0.139556_cQq11_0.327104_cptb_-17.620894_ctt1_-111.677163_ctp_-160.032362_cpt_0.493094",
"EFTrwgt8_ctlTi_0.180654_ctq1_-0.479368_ctq8_-0.477777_cQq83_-0.3009_cQQ1_173.46259_cQt1_130.801921_cQt8_-29.159875_ctli_-8.051302_cQq81_-0.251789_cQlMi_-2.009747_cbW_3.610185_cpQ3_-8.231222_ctei_2.236344_cQei_-3.60203_ctW_1.70754_cpQM_0.257333_ctlSi_-15.845982_ctZ_-0.515634_cQl3i_3.762_ctG_-0.412131_cQq13_0.514044_cQq11_0.626068_cptb_4.688973_ctt1_1.280497_ctp_-22.428913_cpt_2.654613",
"EFTrwgt9_ctlTi_1.225489_ctq1_-0.620788_ctq8_0.6254_cQq83_-2.11265_cQQ1_-71.804967_cQt1_89.677411_cQt8_30.245224_ctli_-7.953917_cQq81_1.167931_cQlMi_-5.05699_cbW_10.257123_cpQ3_-8.922011_ctei_12.542128_cQei_2.365164_ctW_1.435641_cpQM_1.499634_ctlSi_-11.057423_ctZ_0.634093_cQl3i_-0.21356_ctG_0.055507_cQq13_-0.695101_cQq11_0.420134_cptb_28.125226_ctt1_-14.311561_ctp_8.201586_cpt_-0.465983",
"EFTrwgt10_ctlTi_-2.147035_ctq1_-1.01697_ctq8_0.622078_cQq83_1.145759_cQQ1_-1.270163_cQt1_-71.177027_cQt8_-179.000258_ctli_3.723761_cQq81_0.256957_cQlMi_-9.415328_cbW_-4.931594_cpQ3_-3.066554_ctei_-12.486125_cQei_12.997863_ctW_-0.999582_cpQM_0.409261_ctlSi_-7.263955_ctZ_-0.250715_cQl3i_-4.657662_ctG_0.186577_cQq13_0.626576_cQq11_0.097668_cptb_-4.637062_ctt1_-29.611013_ctp_-102.250528_cpt_-2.14311",
"EFTrwgt11_ctlTi_2.019716_ctq1_0.897375_ctq8_-0.937063_cQq83_0.060237_cQQ1_-109.137405_cQt1_154.298495_cQt8_-62.713653_ctli_-1.399867_cQq81_1.279053_cQlMi_4.04292_cbW_11.755795_cpQ3_9.976631_ctei_8.374953_cQei_-1.876604_ctW_-0.422634_cpQM_1.186399_ctlSi_10.018039_ctZ_0.758337_cQl3i_2.922383_ctG_0.049502_cQq13_0.803429_cQq11_-0.556782_cptb_-28.837833_ctt1_46.319561_ctp_-131.706387_cpt_-1.181397",
"EFTrwgt12_ctlTi_-1.840312_ctq1_0.012035_ctq8_-0.205028_cQq83_-0.316026_cQQ1_61.170496_cQt1_-160.233095_cQt8_23.948682_ctli_-4.817311_cQq81_0.7971_cQlMi_6.230793_cbW_-2.628099_cpQ3_11.907784_ctei_5.812788_cQei_5.965171_ctW_-1.859539_cpQM_-0.212281_ctlSi_12.781438_ctZ_1.38748_cQl3i_5.494764_ctG_0.036246_cQq13_-0.675291_cQq11_-0.656838_cptb_-2.793111_ctt1_-52.188755_ctp_9.307317_cpt_-2.45412",
"EFTrwgt13_ctlTi_-2.49128_ctq1_-0.058078_ctq8_1.054447_cQq83_-1.352413_cQQ1_-141.298907_cQt1_136.825636_cQt8_-66.218313_ctli_-2.13885_cQq81_0.974369_cQlMi_-9.125929_cbW_-11.057773_cpQ3_10.928343_ctei_8.856806_cQei_-11.998848_ctW_2.037072_cpQM_0.818544_ctlSi_5.164135_ctZ_-1.5923_cQl3i_4.584764_ctG_-0.303852_cQq13_0.585796_cQq11_-0.128016_cptb_43.940247_ctt1_-59.445094_ctp_-172.645577_cpt_-1.931606",
"EFTrwgt14_ctlTi_-2.502509_ctq1_-0.041309_ctq8_-0.480223_cQq83_-1.177695_cQQ1_-96.58148_cQt1_127.586308_cQt8_-125.979935_ctli_8.783521_cQq81_-0.453485_cQlMi_8.852994_cbW_11.764819_cpQ3_7.732196_ctei_5.084156_cQei_-5.122277_ctW_1.561874_cpQM_-1.124781_ctlSi_-0.906089_ctZ_0.791761_cQl3i_-4.038412_ctG_-0.042361_cQq13_-0.304371_cQq11_-0.548302_cptb_42.051644_ctt1_22.368438_ctp_48.717211_cpt_1.885085",
"EFTrwgt15_ctlTi_-0.607985_ctq1_-0.93471_ctq8_-0.64111_cQq83_-1.190759_cQQ1_81.465467_cQt1_-66.005699_cQt8_11.107875_ctli_7.773844_cQq81_-1.250762_cQlMi_4.474081_cbW_-5.880341_cpQ3_7.217581_ctei_5.494854_cQei_-10.480775_ctW_-1.499187_cpQM_-0.10428_ctlSi_0.123422_ctZ_-0.573059_cQl3i_0.330141_ctG_0.139496_cQq13_-0.189901_cQq11_0.177753_cptb_13.175209_ctt1_34.763205_ctp_176.704784_cpt_-0.230511",
"EFTrwgt16_ctlTi_1.262293_ctq1_0.775169_ctq8_-0.174919_cQq83_1.979432_cQQ1_-112.061997_cQt1_-162.461606_cQt8_-123.416174_ctli_6.668753_cQq81_-1.028027_cQlMi_-4.370948_cbW_-8.480861_cpQ3_-5.917377_ctei_5.166894_cQei_11.383912_ctW_0.321514_cpQM_-0.587392_ctlSi_5.061613_ctZ_-0.792782_cQl3i_-2.526811_ctG_0.376127_cQq13_-0.857075_cQq11_-0.057869_cptb_25.370993_ctt1_-158.729376_ctp_172.20116_cpt_-1.875739",
"EFTrwgt17_ctlTi_2.485594_ctq1_-0.411919_ctq8_0.611042_cQq83_-1.474854_cQQ1_-100.228009_cQt1_-6.376778_cQt8_-63.821632_ctli_-9.165912_cQq81_-0.838186_cQlMi_1.224395_cbW_2.632588_cpQ3_4.106815_ctei_-5.027958_cQei_-7.693638_ctW_-2.383965_cpQM_0.510159_ctlSi_-1.650942_ctZ_-0.259097_cQl3i_1.851173_ctG_-0.106482_cQq13_-0.085905_cQq11_0.21906_cptb_14.940897_ctt1_-168.317273_ctp_-95.198653_cpt_-0.407668",
"EFTrwgt18_ctlTi_2.056988_ctq1_0.237983_ctq8_-1.431084_cQq83_-0.016601_cQQ1_-18.651275_cQt1_-123.26926_cQt8_-163.96633_ctli_1.573601_cQq81_-1.349583_cQlMi_1.167439_cbW_-10.907929_cpQ3_1.42043_ctei_4.162143_cQei_4.927132_ctW_-1.280014_cpQM_1.190674_ctlSi_-9.149956_ctZ_1.321283_cQl3i_1.098606_ctG_-0.318731_cQq13_0.032645_cQq11_0.385334_cptb_26.852759_ctt1_146.023245_ctp_28.543535_cpt_2.632005",
"EFTrwgt19_ctlTi_-0.827655_ctq1_1.145334_ctq8_0.768135_cQq83_-0.033159_cQQ1_-36.256174_cQt1_-76.362264_cQt8_31.19025_ctli_1.148549_cQq81_-0.873243_cQlMi_-5.425348_cbW_8.19991_cpQ3_-9.12537_ctei_-0.924794_cQei_8.340258_ctW_0.722404_cpQM_-0.554043_ctlSi_-0.059807_ctZ_-0.463877_cQl3i_-2.697054_ctG_-0.381304_cQq13_-0.314559_cQq11_0.703417_cptb_21.181288_ctt1_59.63388_ctp_37.54865_cpt_-1.298296",
"EFTrwgt20_ctlTi_-0.108089_ctq1_-0.209133_ctq8_0.451924_cQq83_-0.331602_cQQ1_34.902141_cQt1_-174.09244_cQt8_91.292486_ctli_-9.530805_cQq81_0.581382_cQlMi_-1.573869_cbW_0.950469_cpQ3_7.307878_ctei_-0.963173_cQei_5.661549_ctW_-1.512242_cpQM_0.202733_ctlSi_-6.578751_ctZ_1.298058_cQl3i_0.350814_ctG_-0.322305_cQq13_0.256143_cQq11_0.392273_cptb_-24.105122_ctt1_49.079923_ctp_-128.684167_cpt_1.83022",
"EFTrwgt21_ctlTi_-0.951417_ctq1_0.946983_ctq8_1.451416_cQq83_0.646075_cQQ1_161.60003_cQt1_88.689393_cQt8_-137.616238_ctli_4.25845_cQq81_0.125725_cQlMi_-6.519667_cbW_1.677704_cpQ3_11.744712_ctei_7.13887_cQei_3.180257_ctW_-0.611514_cpQM_0.081307_ctlSi_1.226757_ctZ_0.934216_cQl3i_3.417653_ctG_-0.176773_cQq13_0.246785_cQq11_-0.28875_cptb_7.426498_ctt1_140.897521_ctp_84.896722_cpt_1.646565",
"EFTrwgt22_ctlTi_-0.839213_ctq1_-0.568019_ctq8_1.44071_cQq83_-1.036428_cQQ1_76.787709_cQt1_105.646207_cQt8_142.642711_ctli_5.515415_cQq81_-1.097038_cQlMi_2.229727_cbW_6.657629_cpQ3_-0.879397_ctei_10.235615_cQei_-3.004091_ctW_2.619578_cpQM_-1.54482_ctlSi_-14.010573_ctZ_-0.958647_cQl3i_5.689717_ctG_0.421588_cQq13_-0.401134_cQq11_0.462488_cptb_-18.836314_ctt1_55.632859_ctp_63.61327_cpt_-2.480388",
"EFTrwgt23_ctlTi_0.871103_ctq1_0.57617_ctq8_1.312355_cQq83_-0.797704_cQQ1_71.817048_cQt1_-92.556827_cQt8_91.365804_ctli_1.271845_cQq81_0.096368_cQlMi_7.075067_cbW_8.468131_cpQ3_9.030465_ctei_9.055322_cQei_-4.835791_ctW_0.766708_cpQM_0.186259_ctlSi_-14.038281_ctZ_-0.815314_cQl3i_-2.140035_ctG_0.107658_cQq13_0.736641_cQq11_0.630617_cptb_-38.387318_ctt1_-13.579045_ctp_-0.352788_cpt_0.265785",
"EFTrwgt24_ctlTi_-1.755824_ctq1_-0.732234_ctq8_1.046124_cQq83_-0.799472_cQQ1_-96.676167_cQt1_-100.37424_cQt8_-70.563222_ctli_-2.544008_cQq81_-0.352854_cQlMi_8.994036_cbW_2.048401_cpQ3_-10.734568_ctei_9.953565_cQei_-4.111199_ctW_-2.073965_cpQM_-1.603715_ctlSi_11.339661_ctZ_-1.081679_cQl3i_-5.671831_ctG_0.395824_cQq13_0.41099_cQq11_-0.341274_cptb_-9.546896_ctt1_-13.542658_ctp_79.355702_cpt_1.026606",
"EFTrwgt25_ctlTi_1.313616_ctq1_1.112265_ctq8_-0.80467_cQq83_-0.991762_cQQ1_-47.719139_cQt1_-130.062093_cQt8_-9.160455_ctli_-4.392106_cQq81_0.805689_cQlMi_-6.859472_cbW_-10.31602_cpQ3_2.38439_ctei_7.052756_cQei_-1.920771_ctW_0.391498_cpQM_-0.884026_ctlSi_14.49622_ctZ_-1.574323_cQl3i_0.387191_ctG_0.226085_cQq13_-0.136977_cQq11_-0.468207_cptb_-0.514653_ctt1_114.972191_ctp_111.621288_cpt_-0.348907",
"EFTrwgt26_ctlTi_-2.329998_ctq1_-0.192599_ctq8_0.024256_cQq83_-1.297494_cQQ1_83.804775_cQt1_21.5826_cQt8_70.033642_ctli_-1.565193_cQq81_0.306474_cQlMi_0.724126_cbW_11.205437_cpQ3_-0.034274_ctei_-0.837966_cQei_-10.179394_ctW_-1.266169_cpQM_0.884049_ctlSi_3.148766_ctZ_1.240378_cQl3i_-1.389046_ctG_0.215132_cQq13_-0.803935_cQq11_0.16013_cptb_-21.229563_ctt1_61.85174_ctp_-121.439421_cpt_-1.185141",
"EFTrwgt27_ctlTi_0.610805_ctq1_-0.734664_ctq8_-1.16144_cQq83_0.994919_cQQ1_-21.126944_cQt1_-117.667514_cQt8_120.995603_ctli_-8.057404_cQq81_-0.486885_cQlMi_4.366147_cbW_6.101221_cpQ3_-1.844898_ctei_-8.784714_cQei_0.114662_ctW_2.332498_cpQM_-1.531638_ctlSi_5.526081_ctZ_-0.947797_cQl3i_3.322275_ctG_0.095017_cQq13_0.375814_cQq11_0.134853_cptb_31.94538_ctt1_118.14155_ctp_-179.419927_cpt_1.263705",
"EFTrwgt28_ctlTi_1.214355_ctq1_-1.016892_ctq8_0.070249_cQq83_-1.292968_cQQ1_-153.194542_cQt1_-176.092628_cQt8_-95.280502_ctli_-4.076715_cQq81_1.072683_cQlMi_-9.093062_cbW_4.292176_cpQ3_-8.887746_ctei_-1.329298_cQei_-6.41218_ctW_-2.284176_cpQM_-1.602749_ctlSi_16.693106_ctZ_0.706522_cQl3i_6.560517_ctG_-0.103732_cQq13_-0.800511_cQq11_0.192976_cptb_33.134897_ctt1_-143.658924_ctp_-16.782573_cpt_-2.677603",
"EFTrwgt29_ctlTi_-0.871852_ctq1_0.696109_ctq8_-0.997494_cQq83_-1.980832_cQQ1_-125.795626_cQt1_-139.614284_cQt8_124.551763_ctli_2.593268_cQq81_-0.742047_cQlMi_-6.193989_cbW_3.269038_cpQ3_-9.144661_ctei_-8.973316_cQei_-6.908957_ctW_-1.860546_cpQM_-0.117337_ctlSi_6.049285_ctZ_0.630841_cQl3i_1.851074_ctG_0.33833_cQq13_0.07984_cQq11_-0.513637_cptb_-3.817602_ctt1_16.966587_ctp_50.861113_cpt_-0.345766",
"EFTrwgt30_ctlTi_2.431544_ctq1_0.441256_ctq8_-1.172703_cQq83_0.231248_cQQ1_-44.160784_cQt1_72.806735_cQt8_39.379953_ctli_6.686882_cQq81_-0.289726_cQlMi_-4.609646_cbW_-0.163938_cpQ3_4.799258_ctei_-0.388628_cQei_9.774918_ctW_-2.243697_cpQM_1.367098_ctlSi_-9.122799_ctZ_1.60696_cQl3i_-5.026907_ctG_0.227196_cQq13_0.529481_cQq11_-0.353773_cptb_-30.250044_ctt1_-71.542437_ctp_-12.189806_cpt_-1.878226",
"EFTrwgt31_ctlTi_-0.924518_ctq1_0.665834_ctq8_-1.052632_cQq83_1.828769_cQQ1_3.081738_cQt1_-69.004502_cQt8_170.217703_ctli_7.264664_cQq81_-0.847489_cQlMi_-3.537748_cbW_2.198814_cpQ3_-7.819644_ctei_5.014376_cQei_0.26261_ctW_1.084642_cpQM_-0.744058_ctlSi_9.720781_ctZ_1.498761_cQl3i_1.914093_ctG_0.169389_cQq13_0.759463_cQq11_0.045541_cptb_-18.213549_ctt1_68.888898_ctp_-69.398915_cpt_1.82348",
"EFTrwgt32_ctlTi_0.712769_ctq1_0.578967_ctq8_1.194595_cQq83_1.983427_cQQ1_26.093932_cQt1_-124.964459_cQt8_65.229466_ctli_5.096018_cQq81_-1.314448_cQlMi_-9.3207_cbW_7.618144_cpQ3_-8.268085_ctei_-10.824311_cQei_5.534418_ctW_0.259363_cpQM_-1.16791_ctlSi_2.017034_ctZ_0.274821_cQl3i_-4.28099_ctG_0.287449_cQq13_-0.569459_cQq11_-0.487696_cptb_-43.144878_ctt1_-38.312769_ctp_-81.263265_cpt_-1.174928",
"EFTrwgt33_ctlTi_0.082718_ctq1_0.8591_ctq8_-1.477203_cQq83_-0.050976_cQQ1_-152.893163_cQt1_-165.494153_cQt8_-24.915157_ctli_3.951127_cQq81_1.249747_cQlMi_-6.884902_cbW_-5.700096_cpQ3_10.238424_ctei_8.651925_cQei_-3.095287_ctW_1.710352_cpQM_0.583084_ctlSi_8.61486_ctZ_-1.463932_cQl3i_4.822727_ctG_0.23932_cQq13_-0.098925_cQq11_0.723217_cptb_-20.290335_ctt1_153.425986_ctp_-152.936525_cpt_-0.760092",
"EFTrwgt34_ctlTi_-1.044199_ctq1_-0.450525_ctq8_-0.914864_cQq83_-0.096747_cQQ1_-59.769488_cQt1_-70.569412_cQt8_-95.36666_ctli_1.240143_cQq81_0.755288_cQlMi_2.304811_cbW_8.336494_cpQ3_-8.150882_ctei_3.987717_cQei_4.296741_ctW_-0.692476_cpQM_-1.548591_ctlSi_-16.498245_ctZ_-1.395976_cQl3i_5.64965_ctG_0.24838_cQq13_0.506715_cQq11_-0.402353_cptb_7.866829_ctt1_65.269803_ctp_126.874771_cpt_2.631596",
"EFTrwgt35_ctlTi_-1.797896_ctq1_0.386178_ctq8_1.32958_cQq83_0.133788_cQQ1_-107.120537_cQt1_-43.099985_cQt8_-140.454085_ctli_0.437747_cQq81_-0.954901_cQlMi_5.04519_cbW_-7.286061_cpQ3_7.138635_ctei_-12.015062_cQei_12.103577_ctW_-0.339484_cpQM_1.282166_ctlSi_-1.227637_ctZ_-1.091037_cQl3i_-2.51233_ctG_0.249075_cQq13_0.527566_cQq11_0.744893_cptb_-1.793318_ctt1_26.26925_ctp_34.744138_cpt_0.731901",
"EFTrwgt36_ctlTi_-2.166697_ctq1_-0.845031_ctq8_-0.589745_cQq83_0.162485_cQQ1_-54.163122_cQt1_11.892712_cQt8_113.962511_ctli_-3.576078_cQq81_-1.108789_cQlMi_-2.629773_cbW_9.595578_cpQ3_-13.619024_ctei_-7.017175_cQei_-1.419252_ctW_-0.676752_cpQM_1.39555_ctlSi_-4.787118_ctZ_-0.080497_cQl3i_-4.522714_ctG_0.393177_cQq13_-0.133593_cQq11_0.625115_cptb_5.804295_ctt1_-35.32228_ctp_109.074415_cpt_-0.574207",
"EFTrwgt37_ctlTi_-1.265875_ctq1_0.615716_ctq8_-0.581364_cQq83_-0.066614_cQQ1_-113.863486_cQt1_-77.184494_cQt8_-124.043097_ctli_-3.347147_cQq81_1.142853_cQlMi_3.680897_cbW_-10.639031_cpQ3_-7.690705_ctei_4.976358_cQei_-0.516968_ctW_-0.763326_cpQM_-0.943123_ctlSi_-10.946572_ctZ_0.862443_cQl3i_-0.061198_ctG_-0.129806_cQq13_0.671601_cQq11_0.506325_cptb_8.539477_ctt1_-75.948736_ctp_-16.59551_cpt_1.594316",
"EFTrwgt38_ctlTi_1.591952_ctq1_-0.80434_ctq8_0.264687_cQq83_1.629513_cQQ1_-163.323565_cQt1_10.230054_cQt8_-141.511857_ctli_-1.228367_cQq81_0.83965_cQlMi_-0.957242_cbW_12.292194_cpQ3_3.094308_ctei_-12.144066_cQei_-7.14269_ctW_-0.59456_cpQM_0.460131_ctlSi_-9.242853_ctZ_-0.505577_cQl3i_3.251109_ctG_-0.310117_cQq13_-0.455425_cQq11_0.118811_cptb_17.508673_ctt1_-146.747594_ctp_157.422763_cpt_2.152352",
"EFTrwgt39_ctlTi_-1.849714_ctq1_0.653594_ctq8_1.26402_cQq83_-0.834742_cQQ1_-159.997016_cQt1_92.916196_cQt8_-40.500402_ctli_9.001534_cQq81_-0.355022_cQlMi_-9.188076_cbW_4.30778_cpQ3_8.043229_ctei_-9.697684_cQei_-2.426285_ctW_-0.846278_cpQM_-1.175383_ctlSi_9.765218_ctZ_0.482335_cQl3i_-3.252973_ctG_-0.054024_cQq13_0.348971_cQq11_-0.100666_cptb_-4.520705_ctt1_7.738743_ctp_-126.198188_cpt_0.318394",
"EFTrwgt40_ctlTi_-1.431695_ctq1_0.245046_ctq8_0.946386_cQq83_-1.080756_cQQ1_-71.41238_cQt1_81.5492_cQt8_102.638863_ctli_-8.537472_cQq81_0.635796_cQlMi_4.556504_cbW_8.856974_cpQ3_10.144294_ctei_-9.109178_cQei_-5.173831_ctW_2.179293_cpQM_0.857425_ctlSi_-8.271729_ctZ_0.498546_cQl3i_4.850153_ctG_0.133666_cQq13_0.006287_cQq11_0.835825_cptb_31.30529_ctt1_166.966226_ctp_-104.444612_cpt_1.843209",
"EFTrwgt41_ctlTi_0.261884_ctq1_0.562444_ctq8_-0.388918_cQq83_-2.131991_cQQ1_-3.964471_cQt1_29.802034_cQt8_-76.634867_ctli_-6.091178_cQq81_-0.65568_cQlMi_-9.49888_cbW_-2.395683_cpQ3_-11.666197_ctei_-1.562181_cQei_-9.369845_ctW_-2.61969_cpQM_0.101307_ctlSi_-1.481386_ctZ_-0.05526_cQl3i_-5.8314_ctG_0.004074_cQq13_0.115691_cQq11_0.011358_cptb_30.64875_ctt1_-97.522252_ctp_110.591619_cpt_-0.566676",
"EFTrwgt42_ctlTi_0.59288_ctq1_0.111674_ctq8_0.282932_cQq83_0.152363_cQQ1_63.550072_cQt1_12.895623_cQt8_-109.726219_ctli_8.924076_cQq81_-0.277629_cQlMi_6.537728_cbW_11.072623_cpQ3_-14.163767_ctei_3.17218_cQei_-0.032598_ctW_0.099709_cpQM_-0.760755_ctlSi_-6.933603_ctZ_0.061983_cQl3i_5.069386_ctG_-0.402646_cQq13_0.101308_cQq11_0.188603_cptb_14.093363_ctt1_175.971596_ctp_-146.673956_cpt_0.892072",
"EFTrwgt43_ctlTi_-1.490355_ctq1_-0.91814_ctq8_-0.183023_cQq83_1.49648_cQQ1_90.552177_cQt1_147.564333_cQt8_118.935344_ctli_-8.11936_cQq81_0.636512_cQlMi_10.285589_cbW_-12.050657_cpQ3_-11.667732_ctei_3.746395_cQei_1.003216_ctW_-0.995658_cpQM_-0.918343_ctlSi_14.71538_ctZ_-1.461632_cQl3i_-2.181292_ctG_-0.384216_cQq13_-0.081096_cQq11_0.281283_cptb_-3.782047_ctt1_55.649017_ctp_-119.624938_cpt_0.809095",
"EFTrwgt44_ctlTi_0.792516_ctq1_0.513703_ctq8_-1.343901_cQq83_-0.782964_cQQ1_-57.769254_cQt1_97.754858_cQt8_114.835833_ctli_3.643102_cQq81_-0.267654_cQlMi_-0.386227_cbW_-5.858459_cpQ3_8.842843_ctei_12.574467_cQei_-3.047572_ctW_-0.983231_cpQM_1.203703_ctlSi_-2.256204_ctZ_1.343477_cQl3i_-6.527878_ctG_0.23892_cQq13_-0.395378_cQq11_-0.87098_cptb_15.84172_ctt1_-20.571701_ctp_21.924756_cpt_-0.77339",
"EFTrwgt45_ctlTi_-0.18554_ctq1_0.318097_ctq8_0.964758_cQq83_0.741119_cQQ1_31.00521_cQt1_14.655205_cQt8_26.580838_ctli_-5.446611_cQq81_0.365043_cQlMi_2.061253_cbW_12.378675_cpQ3_1.115162_ctei_5.156616_cQei_8.382226_ctW_1.165473_cpQM_1.741866_ctlSi_4.879894_ctZ_1.396095_cQl3i_-4.078378_ctG_-0.220765_cQq13_-0.365804_cQq11_-0.932621_cptb_-6.639324_ctt1_110.56566_ctp_31.682252_cpt_-1.514468",
"EFTrwgt46_ctlTi_-0.024651_ctq1_-0.909431_ctq8_-1.242547_cQq83_-1.229443_cQQ1_-55.395824_cQt1_-112.756335_cQt8_59.099135_ctli_7.044663_cQq81_1.323843_cQlMi_-1.795678_cbW_-3.146393_cpQ3_2.507901_ctei_5.792805_cQei_-4.323496_ctW_-1.874258_cpQM_-1.108619_ctlSi_-6.232129_ctZ_-1.61047_cQl3i_-2.446391_ctG_-0.040011_cQq13_0.189373_cQq11_0.151144_cptb_-14.714898_ctt1_36.085444_ctp_-25.007829_cpt_-0.363011",
]
process.genWeightsTable.namedWeightIDs = named_weights
process.genWeightsTable.namedWeightLabels = named_weights
