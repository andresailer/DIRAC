from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from DIRAC.Core.Workflow.Parameter import *
from DIRAC.Core.Workflow.Module import *
from DIRAC.Core.Workflow.Step import *
from DIRAC.Core.Workflow.Workflow import *
from DIRAC.Core.Workflow.WorkflowReader import *

# define Module 2
module2 = ModuleDefinition("GaudiApplication")  # during constraction class creates duplicating copies of the params
module2.setDescription("Gaudi Application module")
module2.setBody("from WorkflowLib.Module.GaudiApplication import GaudiApplication\n")

# we add empty parameters but linked up as default
module2.addParameter(Parameter("DataType", "", "string", "self", "DataType", True, False, "data type"))
module2.addParameter(Parameter("CONFIG_NAME", "", "string", "self", "CONFIG_NAME", True, False, "Configuration Name"))
module2.addParameter(
    Parameter("CONFIG_VERSION", "", "string", "self", "CONFIG_VERSION", True, False, "Configuration Version")
)
module2.addParameter(Parameter("EVENTTYPE", "", "string", "self", "EVENTTYPE", True, False, "Event Type"))
module2.addParameter(Parameter("appName", "", "string", "self", "appName", True, False, "Application Name"))
module2.addParameter(Parameter("appVersion", "", "string", "self", "appVersion", True, False, "Application Version"))
module2.addParameter(Parameter("appType", "", "string", "self", "appType", True, False, "Application Version"))
module2.addParameter(Parameter("appLog", "", "string", "self", "appLog", True, False, "list of logfile"))
module2.addParameter(Parameter("inputData", "", "jdl", "self", "inputData", True, False, "List of InputData"))
module2.addParameter(Parameter("inputDataType", "", "string", "self", "inputDataType", True, False, "Input Data Type"))
module2.addParameter(
    Parameter("NUMBER_OF_EVENTS", "", "string", "self", "NUMBER_OF_EVENTS", True, False, "number of events requested")
)
module2.addParameter(Parameter("optionsFile", "", "string", "self", "optionsFile", True, False, "Options File"))
module2.addParameter(
    Parameter("optionsLine", "", "string", "self", "optionsLine", True, False, "Number of Event", "option")
)
module2.addParameter(Parameter("systemConfig", "", "string", "self", "systemConfig", True, False, "Job Platform"))
module2.addParameter(Parameter("poolXMLCatName", "", "string", "self", "poolXMLCatName", True, False, "POOL XML slice"))

# define module 3
module3 = ModuleDefinition("LogChecker")  # during constraction class creates duplicating copies of the params
module3.setDescription("Check LogFile module")
module3.setBody("from WorkflowLib.Module.LogChecker import *\n")

# we add parameters and link them to the level of step
module3.addParameter(Parameter("DataType", "", "string", "self", "DataType", True, False, "data type"))
module3.addParameter(Parameter("SourceData", "", "string", "self", "SourceData", True, False, "InputData"))
module3.addParameter(Parameter("CONFIG_NAME", "", "string", "self", "CONFIG_NAME", True, False, "Configuration Name"))
module3.addParameter(
    Parameter("CONFIG_VERSION", "", "string", "self", "CONFIG_VERSION", True, False, "Configuration Version")
)
module3.addParameter(
    Parameter("NUMBER_OF_EVENTS", "", "string", "self", "NUMBER_OF_EVENTS", True, False, "number of events requested")
)
module3.addParameter(Parameter("NUMBER_OF_EVENTS_INPUT", "", "string", "", "", True, True, "number of events as input"))
module3.addParameter(
    Parameter("NUMBER_OF_EVENTS_OUTPUT", "", "string", "", "", False, True, "number of events as input")
)
module3.addParameter(Parameter("appName", "", "string", "self", "appName", True, False, "Application Name"))
module3.addParameter(Parameter("appVersion", "", "string", "self", "appVersion", True, False, "Application Version"))
module3.addParameter(Parameter("appType", "", "string", "self", "appType", True, False, "Application Version"))
module3.addParameter(Parameter("appLog", "", "string", "self", "appLog", True, False, "list of logfile"))
module3.addParameter(Parameter("poolXMLCatName", "", "string", "self", "poolXMLCatName", True, False, "POOL XML slice"))
module3.addParameter(Parameter("inputData", "", "string", "self", "inputData", True, False, "InputData"))
module3.addParameter(
    Parameter("OUTPUT_MAX", "", "string", "self", "OUTPUT_MAX", True, False, "nb max of output to keep")
)
module3.addParameter(Parameter("EMAIL", "@{EMAILNAME}", "string", "", "", True, False, "EMAIL adress"))

# define module 4
module4 = ModuleDefinition("BookkeepingReport")
module4.setDescription("Bookkeeping Report module")
module4.setBody("from WorkflowLib.Module.BookkeepingReport import * \n")
module4.addParameter(Parameter("STEP_ID", "", "string", "self", "STEP_ID", True, False, "EMAIL adress"))
module4.addParameter(
    Parameter("NUMBER_OF_EVENTS", "", "string", "self", "NUMBER_OF_EVENTS", True, False, "number of events requested")
)
module4.addParameter(
    Parameter("NUMBER_OF_EVENTS_INPUT", "", "string", "", "", True, False, "number of events as input")
)
module4.addParameter(
    Parameter("NUMBER_OF_EVENTS_OUTPUT", "", "string", "", "", True, False, "number of events as input")
)
module4.addParameter(Parameter("DataType", "", "string", "self", "DataType", True, False, "data type"))
module4.addParameter(Parameter("CONFIG_NAME", "", "string", "self", "CONFIG_NAME", True, False, "Configuration Name"))
module4.addParameter(
    Parameter("CONFIG_VERSION", "", "string", "self", "CONFIG_VERSION", True, False, "Configuration Version")
)
module4.addParameter(Parameter("appName", "", "string", "self", "appName", True, False, "Application Name"))
module4.addParameter(Parameter("appVersion", "", "string", "self", "appVersion", True, False, "Application Version"))
module4.addParameter(Parameter("inputData", "", "string", "self", "inputData", True, False, "InputData"))
module4.addParameter(Parameter("inputDataType", "", "string", "self", "inputDataType", True, False, "Input Data Type"))
module4.addParameter(Parameter("EVENTTYPE", "", "string", "self", "EVENTTYPE", True, False, "Event Type"))
module4.addParameter(Parameter("appType", "", "string", "self", "appType", True, False, "Application Version"))
module4.addParameter(Parameter("poolXMLCatName", "", "string", "self", "poolXMLCatName", True, False, "POOL XML slice"))
module4.addParameter(Parameter("SourceData", "", "string", "self", "SourceData", True, False, "InputData"))
module4.addParameter(Parameter("appLog", "", "string", "self", "appLog", True, False, "list of logfile"))
module4.addParameter(Parameter("listoutput", [], "list", "self", "listoutput", True, False, "list of output data"))


# define module 5
module5 = ModuleDefinition("StepFinalization")
module5.setDescription("Step Finalization module")
module5.setBody("from WorkflowLib.Module.StepFinalization import * \n")
module5.addParameter(Parameter("listoutput", [], "list", "self", "listoutput", True, False, "list of output data"))
module5.addParameter(Parameter("poolXMLCatName", "", "string", "self", "poolXMLCatName", True, False, "POOL XML slice"))
module5.addParameter(Parameter("inputData", "", "string", "self", "inputData", True, False, "InputData"))
module5.addParameter(Parameter("SourceData", "", "string", "self", "SourceData", True, False, "InputData"))

# define module 6
module6 = ModuleDefinition("JobFinalization")
module6.setDescription("Job Finalization module")
module6.setBody("from WorkflowLib.Module.JobFinalization import * \n")
# module6.addParameter(Parameter("listoutput",[],"list","self","listoutput",True,False,"list of output data"))
# module6.addParameter(Parameter("outputData",'',"string","self","outputData",True,False,"list of output data"))
module6.addParameter(Parameter("poolXMLCatName", "", "string", "self", "poolXMLCatName", True, False, "POOL XML slice"))
# KGG Some problem with InputData and with inputData - it is not clear for me
# module6.addParameter(Parameter("inputData","","string","self","InputData",True,False,"InputData"))
module6.addParameter(Parameter("SourceData", "", "string", "self", "SourceData", True, False, "InputData"))

# module6.addParameter(Parameter("listoutput",[],"list","self","listoutput",True,False,"list of output data"))
# I am adding those parameters with empty list
# used one going to be replaced on the level of the step
module6.addParameter(Parameter("listoutput_1", [], "list", "self", "listoutput_1", True, False, "list of output data"))
module6.addParameter(Parameter("listoutput_2", [], "list", "self", "listoutput_2", True, False, "list of output data"))
module6.addParameter(Parameter("listoutput_3", [], "list", "self", "listoutput_3", True, False, "list of output data"))
module6.addParameter(Parameter("listoutput_4", [], "list", "self", "listoutput_4", True, False, "list of output data"))
module6.addParameter(Parameter("listoutput_5", [], "list", "self", "listoutput_5", True, False, "list of output data"))
module6.addParameter(Parameter("listoutput_6", [], "list", "self", "listoutput_6", True, False, "list of output data"))

# define module 7
# module7 = ModuleDefinition('Dummy')
# module7.setDescription('Dummy module')
# module7.setBody('from WorkflowLib.Module.Dummy import * \n')


###############   STEPS ##################################
# step 1 we are creating step definition
step1 = StepDefinition("Gaudi_App_Step")
step1.addModule(module2)  # Creating instance of the module 'Gaudi_App_Step'
moduleInstance2 = step1.createModuleInstance("GaudiApplication", "module2")
# moduleInstance2 = step1.createModuleInstance('Dummy', 'module7')

step1.addModule(module3)  # Creating instance of the module 'LogChecker'
moduleInstance3 = step1.createModuleInstance("LogChecker", "module3")

step1.addModule(module4)  # Creating instance of the module 'LogChecker'
moduleInstance4 = step1.createModuleInstance("BookkeepingReport", "module4")
moduleInstance4.setLink("NUMBER_OF_EVENTS_INPUT", moduleInstance3.getName(), "NUMBER_OF_EVENTS_INPUT")
moduleInstance4.setLink("NUMBER_OF_EVENTS_OUTPUT", moduleInstance3.getName(), "NUMBER_OF_EVENTS_OUTPUT")
# in principle we can link parameters of moduleInstance2 with moduleInstance1 but
# in this case we going to use link with the step
# step1.addModule(module5)
# moduleInstance5 = step1.createModuleInstance('StepFinalization','module5')

# now we can add parameters for the STEP but instead of typing them we can just use old one from modules
step1.addParameterLinked(module3.parameters)
step1.addParameterLinked(module2.parameters)

# and we can add additional parameter which will be used as a global
step1.addParameter(
    Parameter("STEP_ID", "@{PRODUCTION_ID}_@{JOB_ID}_@{STEP_NUMBER}", "string", "", "", True, False, "Temporary fix")
)
step1.addParameter(Parameter("EVENTTYPE", "30000000", "string", "", "", True, False, "Event Type"))
step1.addParameter(Parameter("outputData", "@{STEP_ID}.root", "string", "", "", True, False, "etc name"))
step1.addParameter(Parameter("etcf", "SETC_@{STEP_ID}.root", "string", "", "", True, False, "etc name"))
step1.setValue("appLog", "@{appName}_@{PRODUCTION_ID}_@{JOB_ID}_@{STEP_NUMBER}.log")
step1.unlink(["appLog", "appName", "appType"])
step1.unlink(["poolXMLCatName", "SourceData", "DataType", "CONFIG_NAME", "CONFIG_VERSION"])
step1.addParameter(Parameter("listoutput", [], "list", "", "", True, False, "list of output data"))

# outputData = "@{PRODUCTION_ID}_@{JOB_ID}_@{STEP_NUMBER}.@{appType}"
opt_dav = "EvtTupleSvc.Output = {}"
opt_dav = opt_dav + ";ApplicationMgr.OutStream -= {'DstWriter'}"
opt_dav = opt_dav + ";ApplicationMgr.OutStream = {'Sequencer/SeqWriteTag'}"
opt_dav = opt_dav + ';ApplicationMgr.TopAlg -= { "GaudiSequencer/SeqPreselHWZ2bbl" }'
opt_dav = opt_dav + ";MessageSvc.Format = '%u % F%18W%S%7W%R%T %0W%M';MessageSvc.timeFormat = '%Y-%m-%d %H:%M:%S UTC'"
opt_dav = (
    opt_dav
    + ";WR.Output = \"Collection='EVTTAGS/TagCreator/1' ADDRESS='/Event' "
    + "DATAFILE='@{outputData}' TYP='POOL_ROOTTREE' OPT='RECREATE'\""
)
opt_dav = opt_dav + ';EventPersistencySvc.CnvServices += { "LHCb::RawDataCnvSvc" }'
opt_dav = opt_dav + ';ApplicationMgr.TopAlg += {"StoreExplorerAlg"}'
opt_dav = opt_dav + ";StoreExplorerAlg.Load = 1"
opt_dav = opt_dav + ";StoreExplorerAlg.PrintFreq = 0.99"
opt_dav = opt_dav + ";StoreExplorerAlg.AccessForeign = true"

# etcf = "SETC_@{STEP_ID}.root"
opt_brunel = '#include "$BRUNELOPTS/SuppressWarnings.opts"'
opt_brunel = (
    opt_brunel + ";MessageSvc.Format = '%u % F%18W%S%7W%R%T %0W%M';" + "MessageSvc.timeFormat = '%Y-%m-%d %H:%M:%S UTC'"
)
opt_brunel = opt_brunel + ";EventLoopMgr.OutputLevel = 3"
opt_brunel = opt_brunel + ";DstWriter.Output = \"DATAFILE='PFN:@{outputData}' TYP='POOL_ROOTTREE' OPT='RECREATE'\""
opt_brunel = (
    opt_brunel + ";EvtTupleSvc.Output = {\"EVTTAGS2 DATAFILE='PFN:@{etcf}' TYP='POOL_ROOTTREE' OPT='RECREATE'\"}"
)
# opt_brunel = opt_brunel+";EventSelector.Input = {\"COLLECTION=\'TagCreator/1\' DATAFILE=\'@{InputData}\' TYPE=\'POOL_ROOTTREE\' SEL=\'(GlobalOr>=1)\' OPT=\'READ\'\"}"
opt_brunel = opt_brunel + ';EventPersistencySvc.CnvServices += { "LHCb::RawDataCnvSvc" }'
opt_brunel = opt_brunel + ';ApplicationMgr.TopAlg += {"StoreExplorerAlg"}'
opt_brunel = opt_brunel + ";StoreExplorerAlg.Load = 1"
opt_brunel = opt_brunel + ";StoreExplorerAlg.PrintFreq = 0.99"
opt_brunel = opt_brunel + ";IODataManager.AgeLimit = 2"

step3 = StepDefinition("Job_Finalization")
step3.addModule(module6)
moduleInstance6 = step3.createModuleInstance("JobFinalization", "module6")
step3.addParameterLinked(module6.parameters)
step3.unlink(["poolXMLCatName", "SourceData", "DataType", "CONFIG_NAME", "CONFIG_VERSION"])


##############  WORKFLOW #################################
workflow1 = Workflow(name="CCRC-strip-test")
workflow1.setDescription("Workflow of GaudiApplication")

workflow1.addStep(step1)
step1_prefix = "step1_"
stepInstance1 = workflow1.createStepInstance("Gaudi_App_Step", "Step1")
# lets link all parameters them up with the level of workflow
stepInstance1.linkUp(stepInstance1.parameters, step1_prefix)
stepInstance1.setLink("systemConfig", "self", "SystemConfig")  # capital letter corrected
stepInstance1.unlink(
    [
        "listoutput",
        "STEP_ID",
        "optionsFile",
        "optionsLine",
        "appLog",
        "appName",
        "etcf",
        "appType",
        "outputData",
        "EVENTTYPE",
    ]
)
stepInstance1.setValue("appName", "DaVinci")
stepInstance1.setValue("appType", "root")
stepInstance1.setValue("outputData", "@{PRODUCTION_ID}_@{JOB_ID}_@{STEP_NUMBER}.@{appType}")
stepInstance1.setValue("optionsFile", "DVOfficialStrippingFile.opts")
stepInstance1.setValue("optionsLine", opt_dav)
stepInstance1.linkUp("CONFIG_NAME")
stepInstance1.linkUp("CONFIG_VERSION")
stepInstance1.linkUp("DataType")
stepInstance1.linkUp("SourceData")
stepInstance1.linkUp("poolXMLCatName")
stepInstance1.setLink("inputData", "self", "InputData")  # KGG linked with InputData of the Workflow
list1_out = [
    {
        "outputDataName": "@{PRODUCTION_ID}_@{JOB_ID}_@{STEP_NUMBER}.@{appType}",
        "outputType": "FETC",
        "outputDataSE": "Tier1_M-DST",
    }
]
stepInstance1.setValue("listoutput", list1_out)

step2_prefix = "step2_"
stepInstance2 = workflow1.createStepInstance("Gaudi_App_Step", "Step2")
# lets link all parameters them up with the level of workflow
stepInstance2.linkUp(stepInstance2.parameters, step2_prefix)
stepInstance2.setLink("systemConfig", "self", "SystemConfig")  # capital letter corrected
# except "STEP_ID", "appLog"
stepInstance2.unlink(
    [
        "listoutput",
        "STEP_ID",
        "optionsFile",
        "outputData",
        "optionsLine",
        "appLog",
        "appName",
        "appType",
        "etcf",
        "EVENTTYPE",
    ]
)
stepInstance2.setValue("appName", "Brunel")
stepInstance2.setValue("appType", "dst")
stepInstance2.setValue("outputData", "@{PRODUCTION_ID}_@{JOB_ID}_@{STEP_NUMBER}.@{appType}")
stepInstance2.setValue("etcf", "SETC_@{PRODUCTION_ID}_@{JOB_ID}_@{STEP_NUMBER}.root")
stepInstance2.setValue("optionsFile", "RealData-ETC.opts")
stepInstance2.setValue("optionsLine", opt_brunel)
# stepInstance2.setValue("outputDataSE","Tier1_M-DST")
stepInstance2.linkUp("CONFIG_NAME")
stepInstance2.linkUp("CONFIG_VERSION")
stepInstance2.linkUp("DataType")
stepInstance2.linkUp("SourceData")
stepInstance2.linkUp("poolXMLCatName")
stepInstance2.setLink("inputData", stepInstance1.getName(), "outputData")
list2_out = [
    {
        "outputDataName": "@{PRODUCTION_ID}_@{JOB_ID}_@{STEP_NUMBER}.@{appType}",
        "outputType": "dst",
        "outputDataSE": "Tier1_M-DST",
    },
    {
        "outputDataName": "SETC_@{PRODUCTION_ID}_@{JOB_ID}_@{STEP_NUMBER}.root",
        "outputType": "SETC",
        "outputDataSE": "Tier1_M-DST",
    },
]
stepInstance2.setValue("listoutput", list2_out)

workflow1.addStep(step3)
step3_prefix = "step3_"
stepInstance3 = workflow1.createStepInstance("Job_Finalization", "Step3")
# stepInstance3.linkUp(stepInstance3.parameters, step3_prefix)
stepInstance3.linkUp("CONFIG_NAME")
stepInstance3.linkUp("CONFIG_VERSION")
stepInstance3.linkUp("DataType")
stepInstance3.linkUp("SourceData")
stepInstance3.linkUp("poolXMLCatName")
# I am adding
stepInstance3.unlink(["listoutput_1", "listoutput_2", "listoutput_3", "listoutput_4", "listoutput_5", "listoutput_6"])
stepInstance3.setLink("listoutput_1", stepInstance1.getName(), "listoutput")
stepInstance3.setLink("listoutput_2", stepInstance2.getName(), "listoutput")
# **************************
workflow1.addParameterLinked(step1.parameters, step1_prefix)
workflow1.addParameterLinked(step1.parameters, step2_prefix)
# and finally we can unlink them because we inherit them linked
workflow1.unlink(workflow1.parameters)

workflow1.setValue(step1_prefix + "appVersion", "v19r11")
workflow1.setValue(step2_prefix + "appVersion", "v32r4")
workflow1.setValue(step1_prefix + "NUMBER_OF_EVENTS", "5")
workflow1.setValue(step2_prefix + "NUMBER_OF_EVENTS", "-1")
workflow1.removeParameter(step1_prefix + "inputData")  # KGG wrong parameter
workflow1.setValue(step1_prefix + "inputDataType", "RDST")
workflow1.setValue(step2_prefix + "inputDataType", "ETC")
workflow1.setValue(step1_prefix + "OUTPUT_MAX", "20")
# remove unwanted
workflow1.removeParameter(step1_prefix + "outputData")
workflow1.removeParameter(step1_prefix + "systemConfig")
workflow1.removeParameter(step2_prefix + "outputData")
workflow1.removeParameter(step2_prefix + "systemConfig")

# add syspem config which common for all modules
# workflow1.addParameter(Parameter("systemConfig","slc4_ia32_gcc34","string","","",True, False, "Application Name"))
workflow1.addParameter(
    Parameter("SystemConfig", "x86_64-slc5-gcc43-opt", "JDLReqt", "", "", True, False, "Application Name")
)

# Now lets define parameters on the top
# indata = "LFN:/lhcb/production/DC06/phys-v2-lumi2/00001820/SIM/0000/00001820_00000001_1.sim;LFN:/lhcb/production/DC06/phys-v2-lumi2/00001820/SIM/0000/00001820_00000001_2.sim;LFN:/lhcb/production/DC06/phys-v2-lumi2/00001820/SIM/0000/00001820_00000001_3.sim"
indata = "LFN:/lhcb/data/CCRC08/RDST/00000106/0000/00000106_00007918_1.rdst"
# indata = "LFN:/lhcb/data/CCRC08/RDST/00000106/0000/00000106_00007918_1.rdst;/lhcb/data/CCRC08/RAW/LHCb/CCRC/420217/420217_0000116193.raw"
# etcf = "joel.root"
# indata = "LFN:/lhcb/data/CCRC08/RAW/LHCb/CCRC/402154/402154_0000047096.raw;LFN:/lhcb/data/CCRC08/RAW/LHCb/CCRC/402154/402154_0000047097.raw"
# lets specify parameters on the level of workflow


workflow1.addParameter(Parameter("InputData", indata, "JDL", "", "", True, False, "Application Name"))
workflow1.addParameter(Parameter("JobType", "test", "JDL", "", "", True, False, "Job TYpe"))
workflow1.addParameter(Parameter("AncestorDepth", "2", "JDL", "", "", True, False, "Ancestor Depth"))
workflow1.addParameter(Parameter("Owner", "joel", "JDL", "", "", True, False, "user Name"))
workflow1.addParameter(Parameter("StdError", "std.err", "JDL", "", "", True, False, "user Name"))
workflow1.addParameter(Parameter("StdOutput", "std.out", "JDL", "", "", True, False, "user Name"))
workflow1.addParameter(Parameter("SoftwarePackages", "Brunel.v32r4", "JDL", "", "", True, False, "software"))

workflow1.addParameter(Parameter("CPUTime", 300000, "JDLReqt", "", "", True, False, "Application Name"))
# workflow1.addParameter(Parameter("Site","LCG.CERN.ch","JDLReqt","","",True, False, "Site"))
workflow1.addParameter(Parameter("Platform", "gLite", "JDLReqt", "", "", True, False, "platform"))

# and finally we can unlink them because we inherit them linked
workflow1.unlink(workflow1.parameters)

workflow1.addParameter(Parameter("PRODUCTION_ID", "00003033", "string", "", "", True, False, "Temporary fix"))
workflow1.addParameter(Parameter("JOB_ID", "00000011", "string", "", "", True, False, "Temporary fix"))
workflow1.addParameter(
    Parameter(
        "EMAILNAME",
        "joel.closier@cern.ch",
        "string",
        "",
        "",
        True,
        False,
        "Email to send a report from the LogCheck module",
    )
)
workflow1.addParameter(Parameter("DataType", "DATA", "string", "", "", True, False, "type of Datatype"))
workflow1.addParameter(Parameter("SourceData", indata, "string", "", "", True, False, "Application Name"))
workflow1.addParameter(
    Parameter("poolXMLCatName", "pool_xml_catalog.xml", "string", "", "", True, False, "Application Name")
)
workflow1.addParameter(Parameter("CONFIG_NAME", "LHCb", "string", "", "", True, False, "Configuration Name"))
workflow1.addParameter(Parameter("CONFIG_VERSION", "CCRC08", "string", "", "", True, False, "Configuration Version"))
# workflow1.addParameter(Parameter("NUMBER_OF_EVENTS","5","string","","",True, False, "number of events requested"))
workflow1.toXMLFile("wkf_CCRC_3.xml")
# w4 = fromXMLFile("/afs/cern.ch/user/g/gkuznets/test1.xml")
# print 'Creating code for the workflow'
# eval(compile(workflow1.createCode(),'<string>','exec'))
# workflow1.execute()
