requirements            = (OpSysAndVer =?= "SLCern6")
executable              = /afs/cern.ch/user/h/helfaham/CMSSW_10_2_7/src/Haamm/HaNaMiniAnalyzer/test/Nu18/SingleNeutrinoTuneCP1_1/SetupAndRun.sh
output                  = $(ClusterId)_$(ProcId).out
error                   = $(ClusterId)_$(ProcId).err
log                     = $(ClusterId)_$(ProcId).log
+JobFlavour             = "tomorrow"
environment             = CONDORJOBID=$(ProcId)
notification            = Error

arguments               = /afs/cern.ch/user/h/helfaham/CMSSW_10_2_7/src/Haamm/HaNaMiniAnalyzer/test/Nu18/.x509up_u119445 slc6_amd64_gcc700 CMSSW_10_2_7 PileUP18 SingleNeutrinoTuneCP1_1 out /eos/home-h/helfaham/ 2
queue 0

