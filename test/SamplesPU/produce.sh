# run "voms-proxy-init -voms cms -rfc" before using
echo did you run ---voms-proxy-init -voms cms -rfc---?
# zerobias samples for 2016
#das_client --limit=0 --query="file dataset=/ZeroBias/Run2016H-21Feb2020_UL2016-v1/MINIAOD" > ZeroBiasH.list
#das_client --limit=0 --query="file dataset=/ZeroBias/Run2016G-21Feb2020_UL2016-v1/MINIAOD" > ZeroBiasG.list
#das_client --limit=0 --query="file dataset=/ZeroBias/Run2016F-21Feb2020_UL2016-v1/MINIAOD" > ZeroBiasF.list
#das_client --limit=0 --query="file dataset=/ZeroBias/Run2016E-21Feb2020_UL2016_HIPM-v1/MINIAOD" > ZeroBiasE.list
#das_client --limit=0 --query="file dataset=/ZeroBias/Run2016D-ForValUL2016-v1/MINIAOD" > ZeroBiasD.list
#das_client --limit=0 --query="file dataset=/ZeroBias/Run2016C-21Feb2020_UL2016_HIPM-v1/MINIAOD" > ZeroBiasC.list
#das_client --limit=0 --query="file dataset=/ZeroBias/Run2016B-ForValUL2016-v1/MINIAOD" > ZeroBiasB.list

# produce lists for 2017 (zerobias and singleNeutrino only)
das_client --limit=0 --query="file dataset=/ZeroBias/Run2017F-09Aug2019_UL2017-v1/MINIAOD" > ZeroBiasF.list
das_client --limit=0 --query="file dataset=/ZeroBias/Run2017E-09Aug2019_UL2017-v1/MINIAOD" > ZeroBiasE.list
das_client --limit=0 --query="file dataset=/ZeroBias/Run2017D-09Aug2019_UL2017-v1/MINIAOD" > ZeroBiasD.list
das_client --limit=0 --query="file dataset=/ZeroBias/Run2017C-09Aug2019_UL2017-v1/MINIAOD" > ZeroBiasC.list
das_client --limit=0 --query="file dataset=/ZeroBias/Run2017B-09Aug2019_UL2017-v1/MINIAOD" > ZeroBiasB.list
das_client --limit=0 --query="file dataset=/SingleNeutrino/RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM" > SingleNeutrino.list
das_client --limit=0 --query="file dataset=/SingleNeutrino/RunIISummer19UL17MiniAOD-FlatPU0to75_106X_mc2017_realistic_v6_ext2-v1/MINIAODSIM" > SingleNeutrino_FlatPU.list
