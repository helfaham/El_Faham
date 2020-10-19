from Haamm.HaNaMiniAnalyzer.Sample import *

import os
Sample.WD = os.path.dirname(os.path.abspath(__file__))
print Sample.WD

MINIAOD = []

SingleNeutrino_CP1 = Sample("SingleNeutrino_CP1" , 1 , False , "/SingleNeutrino/RunIISummer19UL16MiniAOD-FlatPU0to75TuneCP1_106X_mcRun2_asymptotic_v13-v2/MINIAODSIM")
SingleNeutrino_CP5 = Sample("SingleNeutrino_CP5" , 1 , False , " /SingleNeutrino/RunIISummer19UL16MiniAOD-FlatPU0to75_106X_mcRun2_asymptotic_v13_ext1-v2/MINIAODSIM")

SingleNeutrino_CP1_APV = Sample("SingleNeutrino_CP1_APV" , 1 , False , "/SingleNeutrino/RunIISummer19UL16MiniAODAPV-FlatPU0to75TuneCP1_106X_mcRun2_asymptotic_preVFP_v8_ext1-v3/MINIAODSIM")
SingleNeutrino_CP5_APV = Sample("SingleNeutrino_CP5_APV" , 1 , False , "/SingleNeutrino/RunIISummer19UL16MiniAODAPV-FlatPU0to75_106X_mcRun2_asymptotic_preVFP_v8_ext2-v2/MINIAODSIM")

SingleNeutrinos = []
SingleNeutrinos.extend( [ SingleNeutrino_CP1, SingleNeutrino_CP5, SingleNeutrino_CP1_APV, SingleNeutrino_CP5_APV ] )
MINIAOD.extend( [ SingleNeutrino_CP1, SingleNeutrino_CP5, SingleNeutrino_CP1_APV, SingleNeutrino_CP5_APV ] )

MinBiasH = Sample("MinBiasH" , 0 , False , "/MinimumBias/Run2016H-21Feb2020_UL2016-v1/MINIAOD")
MinBiasG = Sample("MinBiasG" , 0 , False , "/MinimumBias/Run2016G-21Feb2020_UL2016-v1/MINIAOD")
MinBiasF = Sample("MinBiasF" , 0 , False , "/MinimumBias/Run2016F-21Feb2020_UL2016-v1/MINIAOD")

MINIAOD.extend( [ MinBiasH , MinBiasG , MinBiasF ] )

ZeroBiasH = Sample("ZeroBiasH" , 0 , False , "/ZeroBias/Run2016H-21Feb2020_UL2016-v1/MINIAOD")
ZeroBiasG = Sample("ZeroBiasG" , 0 , False , "/ZeroBias/Run2016G-21Feb2020_UL2016-v1/MINIAOD")
ZeroBiasF = Sample("ZeroBiasF" , 0 , False , "/ZeroBias/Run2016F-21Feb2020_UL2016-v1/MINIAOD")

MINIAOD.extend( [ ZeroBiasH , ZeroBiasG , ZeroBiasF ] )

bug 	= Sample("bug" 		, 1 , False , "/RelValQCD_FlatPt_15_3000HS_13/CMSSW_10_6_14-PU25ns_106X_mc2017_realistic_v7_HS-v1/MINIAODSIM")
bugfix = Sample("bugfix" 	, 1 , False , "/RelValQCD_FlatPt_15_3000HS_13/CMSSW_10_6_14_Pyt8240BugFix-PU25ns_106X_mc2017_realistic_v7_HS-v1/MINIAODSIM")

ZMM_bug 		= Sample("ZMM_bug" 		, 1 , False , "/RelValZMM_13/CMSSW_10_6_14-PU25ns_106X_mc2017_realistic_v7_HS-v1/MINIAODSIM")
ZMM_bugfix 		= Sample("ZMM_bugfix" 		, 1 , False , "/RelValZMM_13/CMSSW_10_6_14_Pyt8240BugFix-PU25ns_106X_mc2017_realistic_v7_HS-v1/MINIAODSIM")
ZMM_bugfix_highstat 	= Sample("ZMM_bugfix_highstat" , 1 , False , "/RelValZMM_13/CMSSW_10_6_14_Pyt8240BugFix-PU25ns_106X_mc2017_realistic_v7_HS_rsb-v1/MINIAODSIM")
MINIAOD.extend( [ ZMM_bug, ZMM_bugfix, ZMM_bugfix_highstat, bug, bugfix ] )
