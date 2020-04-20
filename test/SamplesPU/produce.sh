#/afs/cern.ch/user/h/helfaham/CMSSW_10_6_4_patch1/src/Haamm/HaNaMiniAnalyzer/test/SamplesPU

das_client --limit=0 --query="file dataset=/SingleNeutrino/RunIISummer19UL18MiniAOD-FlatPU0to70_106X_upgrade2018_realistic_v11_L1v1-v1/MINIAODSIM" > SingleNeutrino.list


das_client --limit=0 --query="file dataset=/ZeroBias/Run2018A-12Nov2019_UL2018-v2/MINIAOD  " > ZeroBiasA.list
das_client --limit=0 --query="file dataset=/ZeroBias/Run2018B-12Nov2019_UL2018-v2/MINIAOD  " > ZeroBiasB.list


