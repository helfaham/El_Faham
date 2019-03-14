universe                = vanilla
executable              = /afs/cern.ch/user/h/helfaham/CMSSW_8_4_0/src/Haamm/HaNaMiniAnalyzer/test/submit/eraB/Plotter.py
output                  = $(ClusterId)_$(ProcId).out
error                   = $(ClusterId)_$(ProcId).err
log                     = $(ClusterId)_$(ProcId).log
+JobFlavour             = "tomorrow"
environment             = CONDORJOBID=$(ProcId)
notification            = Error
should_transfer_files   = YES
when_to_transfer_output = ON_EXIT
transfer_input_files    = /afs/cern.ch/user/h/helfaham/CMSSW_8_4_0/src/Haamm/HaNaMiniAnalyzer/test/SamplesPU/Samples.py, /afs/cern.ch/user/h/helfaham/CMSSW_8_4_0/src/Haamm/HaNaMiniAnalyzer/test/SamplesPU/__init__.py

arguments               = latest eraB 
queue 1

