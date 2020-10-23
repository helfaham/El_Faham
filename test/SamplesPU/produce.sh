#/afs/cern.ch/user/h/helfaham/CMSSW_10_6_12/src/Haamm/HaNaMiniAnalyzer/test/SamplesPU
# before tuneCP1 and CP5
# ----------------------
#dasgoclient --limit=0 --query="file dataset=/SingleNeutrino/RunIISummer19UL16MiniAOD-FlatPU0to75TuneCP1_106X_mcRun2_asymptotic_v13-v2/MINIAODSIM" > SingleNeutrinoCP1.list
#dasgoclient --limit=0 --query="file dataset=/SingleNeutrino/RunIISummer19UL16MiniAOD-FlatPU0to75_106X_mcRun2_asymptotic_v13_ext1-v2/MINIAODSIM" > SingleNeutrinoCP5.list

# tune CP1 and CP5 (latest)
# -------------------------
#dasgoclient --limit=0 --query="file dataset=/SingleNeutrino/RunIISummer19UL16MiniAODAPV-FlatPU0to75TuneCP1_106X_mcRun2_asymptotic_preVFP_v8_ext1-v3/MINIAODSIM" > SingleNeutrino_CP1_APV.list
#dasgoclient --limit=0 --query="file dataset=/SingleNeutrino/RunIISummer19UL16MiniAODAPV-FlatPU0to75_106X_mcRun2_asymptotic_preVFP_v8_ext2-v2/MINIAODSIM" > SingleNeutrino_CP5_APV.list


# ZeroBias post the HIP
# ---------------------
#dasgoclient --limit=0 --query="file dataset=/ZeroBias/Run2016H-21Feb2020_UL2016-v1/MINIAOD" > ZeroBiasH.list
#dasgoclient --limit=0 --query="file dataset=/ZeroBias/Run2016G-21Feb2020_UL2016-v1/MINIAOD" > ZeroBiasG.list
#dasgoclient --limit=0 --query="file dataset=/ZeroBias/Run2016F-21Feb2020_UL2016-v1/MINIAOD" > ZeroBiasF.list

# ZeroBias in HIP
# ---------------
dasgoclient --limit=0 --query="file dataset=/ZeroBias/Run2016B-21Feb2020_ver1_UL2016_HIPM-v1/MINIAOD" > ZeroBiasB_APV_ver1.list
dasgoclient --limit=0 --query="file dataset=/ZeroBias/Run2016B-21Feb2020_ver2_UL2016_HIPM-v1/MINIAOD" > ZeroBiasB_APV_ver2.list
dasgoclient --limit=0 --query="file dataset=/ZeroBias/Run2016C-21Feb2020_UL2016_HIPM-v1/MINIAOD" > ZeroBiasC_APV.list
dasgoclient --limit=0 --query="file dataset=/ZeroBias/Run2016D-21Feb2020_UL2016_HIPM-v1/MINIAOD" > ZeroBiasD_APV.list
dasgoclient --limit=0 --query="file dataset=/ZeroBias/Run2016E-21Feb2020_UL2016_HIPM-v1/MINIAOD" > ZeroBiasE_APV.list
dasgoclient --limit=0 --query="file dataset=/ZeroBias/Run2016F-21Feb2020_UL2016_HIPM-v1/MINIAOD" > ZeroBiasF_APV.list

# bug analysis
# ------------
#dasgoclient --limit=0 --query="file dataset=/RelValQCD_FlatPt_15_3000HS_13/CMSSW_10_6_14-PU25ns_106X_mc2017_realistic_v7_HS-v1/MINIAODSIM" > bug.list
#dasgoclient --limit=0 --query="file dataset=/RelValQCD_FlatPt_15_3000HS_13/CMSSW_10_6_14_Pyt8240BugFix-PU25ns_106X_mc2017_realistic_v7_HS-v1/MINIAODSIM" > bugfix.list

#dasgoclient --limit=0 --query="file dataset=/RelValZMM_13/CMSSW_10_6_14_Pyt8240BugFix-PU25ns_106X_mc2017_realistic_v7_HS-v1/MINIAODSIM" > ZMM_bugfix.list
#dasgoclient --limit=0 --query="file dataset=/RelValZMM_13/CMSSW_10_6_14_Pyt8240BugFix-PU25ns_106X_mc2017_realistic_v7_HS_rsb-v1/MINIAODSIM" > ZMM_bugfix_highstat.list
#dasgoclient --limit=0 --query="file dataset=/RelValZMM_13/CMSSW_10_6_14-PU25ns_106X_mc2017_realistic_v7_HS-v1/MINIAODSIM" > ZMM_bug.list
