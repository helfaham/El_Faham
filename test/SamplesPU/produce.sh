#/afs/cern.ch/user/h/helfaham/CMSSW_10_6_12/src/Haamm/HaNaMiniAnalyzer/test/SamplesPU
#dasgoclient --limit=0 --query="file dataset=/SingleNeutrino/RunIISummer19UL16MiniAOD-FlatPU0to75TuneCP1_106X_mcRun2_asymptotic_v13-v2/MINIAODSIM" > SingleNeutrinoCP1.list
dasgoclient --limit=0 --query="file dataset=/SingleNeutrino/RunIISummer19UL16MiniAOD-FlatPU0to75_106X_mcRun2_asymptotic_v13_ext1-v2/MINIAODSIM" > SingleNeutrinoCP5.list

#dasgoclient --limit=0 --query="file dataset=/ZeroBias/Run2016H-21Feb2020_UL2016-v1/MINIAOD" > ZeroBiasH.list
#dasgoclient --limit=0 --query="file dataset=/ZeroBias/Run2016G-21Feb2020_UL2016-v1/MINIAOD" > ZeroBiasG.list
#dasgoclient --limit=0 --query="file dataset=/ZeroBias/Run2016F-21Feb2020_UL2016-v1/MINIAOD" > ZeroBiasF.list

#dasgoclient --limit=0 --query="file dataset=/MinimumBias/Run2016H-21Feb2020_UL2016-v1/MINIAOD" > MinBiasH.list
#dasgoclient --limit=0 --query="file dataset=/MinimumBias/Run2016G-21Feb2020_UL2016-v1/MINIAOD" > MinBiasG.list
#dasgoclient --limit=0 --query="file dataset=/MinimumBias/Run2016F-21Feb2020_UL2016-v1/MINIAOD" > MinBiasF.list

#dasgoclient --limit=0 --query="file dataset=/RelValQCD_FlatPt_15_3000HS_13/CMSSW_10_6_14-PU25ns_106X_mc2017_realistic_v7_HS-v1/MINIAODSIM" > bug.list
#dasgoclient --limit=0 --query="file dataset=/RelValQCD_FlatPt_15_3000HS_13/CMSSW_10_6_14_Pyt8240BugFix-PU25ns_106X_mc2017_realistic_v7_HS-v1/MINIAODSIM" > bugfix.list

