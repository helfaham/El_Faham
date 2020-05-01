executable              = /afs/cern.ch/user/h/helfaham/CMSSW_9_4_7/src/Haamm/HaNaMiniAnalyzer/test/test_AOD/AODtest/SetupAndRun.sh
output                  = $(ClusterId)_$(ProcId).out
error                   = $(ClusterId)_$(ProcId).err
log                     = $(ClusterId)_$(ProcId).log
+JobFlavour             = "tomorrow"
environment             = CONDORJOBID=$(ProcId)
notification            = Error

arguments               = /afs/cern.ch/user/h/helfaham/CMSSW_9_4_7/src/Haamm/HaNaMiniAnalyzer/test/test_AOD/.x509up_u119445 slc6_amd64_gcc630 CMSSW_9_4_7 AOD18 AODtest out /./helfaham/ 2
queue 1

