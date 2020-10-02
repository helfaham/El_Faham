# run "voms-proxy-init -voms cms -rfc" before using
echo did you run ---voms-proxy-init -voms cms -rfc---?
#das_client --limit=0 --query="file dataset=/ZeroBias/Run2017F-09Aug2019_UL2017-v1/MINIAOD" > ZeroBiasF.list
#das_client --limit=0 --query="file dataset=/ZeroBias/Run2017E-09Aug2019_UL2017-v1/MINIAOD" > ZeroBiasE.list
#das_client --limit=0 --query="file dataset=/ZeroBias/Run2017D-09Aug2019_UL2017-v1/MINIAOD" > ZeroBiasD.list
#das_client --limit=0 --query="file dataset=/ZeroBias/Run2017C-09Aug2019_UL2017-v1/MINIAOD" > ZeroBiasC.list
#das_client --limit=0 --query="file dataset=/ZeroBias/Run2017B-09Aug2019_UL2017-v1/MINIAOD" > ZeroBiasB.list

#dasgoclient --limit=0 --query="file dataset =/MinimumBias/Run2017B-09Aug2019_UL2017-v1/MINIAOD" > MinBiasB.list
#dasgoclient --limit=0 --query="file dataset =/MinimumBias/Run2017C-09Aug2019_UL2017-v1/MINIAOD" > MinBiasC.list
#dasgoclient --limit=0 --query="file dataset =/MinimumBias/Run2017D-09Aug2019_UL2017-v1/MINIAOD" > MinBiasD.list
#dasgoclient --limit=0 --query="file dataset =/MinimumBias/Run2017E-09Aug2019_UL2017-v1/MINIAOD" > MinBiasE.list
#dasgoclient --limit=0 --query="file dataset =/MinimumBias/Run2017F-09Aug2019_UL2017-v1/MINIAOD" > MinBiasF.list

##das_client --limit=0 --query="file dataset=/SingleNeutrino/RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM" > SingleNeutrino.list

das_client --limit=0 --query="file dataset=/SingleNeutrino/RunIISummer19UL17MiniAOD-FlatPU0to75_106X_mc2017_realistic_v6_ext2-v1/MINIAODSIM" > SingleNeutrino_CP5.list #this is cp5
das_client --limit=0 --query="file dataset=/SingleNeutrino/RunIISummer19UL17MiniAOD-FlatPU0to75TuneCP1_106X_mc2017_realistic_v6_ext1-v2/MINIAODSIM" > SingleNeutrino_CP1.list #this is cp1
