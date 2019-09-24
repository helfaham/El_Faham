requirements            = (OpSysAndVer =?= "SLCern6")
executable              = /afs/cern.ch/user/h/helfaham/CMSSW_10_2_10/src/Haamm/HaNaMiniAnalyzer/test/./trial/ZeroBiasE/SetupAndRun.sh
output                  = $(ClusterId)_$(ProcId).out
error                   = $(ClusterId)_$(ProcId).err
log                     = $(ClusterId)_$(ProcId).log
+JobFlavour             = "tomorrow"
environment             = CONDORJOBID=$(ProcId)
notification            = Error

arguments               = /afs/cern.ch/user/h/helfaham/CMSSW_10_2_10/src/Haamm/HaNaMiniAnalyzer/test/./trial/.x509up_u119445 slc6_amd64_gcc700 CMSSW_10_2_10 PileUP18 ZeroBiasE out /eos/home-h/helfaham/ 2
queue 70

