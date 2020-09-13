from Haamm.HaNaMiniAnalyzer.Sample import *

import os
Sample.WD = os.path.dirname(os.path.abspath(__file__))
print Sample.WD

MINIAOD = []

SingleNeutrinoCP1 = Sample("SingleNeutrinoCP1" , 1 , False , "/SingleNeutrino/RunIISummer19UL16MiniAOD-FlatPU0to75TuneCP1_106X_mcRun2_asymptotic_v13-v2/MINIAODSIM")

SingleNeutrinos = []
SingleNeutrinos.extend( [ SingleNeutrinoCP1 ] )
MINIAOD.extend( [ SingleNeutrinoCP1 ] )

MinBiasH = Sample("MinBiasH" , 0 , False , "/MinimumBias/Run2016H-21Feb2020_UL2016-v1/MINIAOD")
MinBiasG = Sample("MinBiasG" , 0 , False , "/MinimumBias/Run2016G-21Feb2020_UL2016-v1/MINIAOD")
MinBiasF = Sample("MinBiasF" , 0 , False , "/MinimumBias/Run2016F-21Feb2020_UL2016-v1/MINIAOD")

MINIAOD.extend( [ MinBiasH , MinBiasG , MinBiasF ] )

ZeroBiasH = Sample("ZeroBiasH" , 0 , False , "/ZeroBias/Run2016H-21Feb2020_UL2016-v1/MINIAOD")
ZeroBiasG = Sample("ZeroBiasG" , 0 , False , "/ZeroBias/Run2016G-21Feb2020_UL2016-v1/MINIAOD")
ZeroBiasF = Sample("ZeroBiasF" , 0 , False , "/ZeroBias/Run2016F-21Feb2020_UL2016-v1/MINIAOD")

MINIAOD.extend( [ ZeroBiasH , ZeroBiasG , ZeroBiasF ] )

bug = Sample("bug" , 1 , False , "/RelValQCD_FlatPt_15_3000HS_13/CMSSW_10_6_14-PU25ns_106X_mc2017_realistic_v7_HS-v1/MINIAODSIM")
bugfix = Sample("bugfix" , 1 , False , "/RelValQCD_FlatPt_15_3000HS_13/CMSSW_10_6_14_Pyt8240BugFix-PU25ns_106X_mc2017_realistic_v7_HS-v1/MINIAODSIM")

ZMM_bug = Sample("ZMM_bug" , 1 , False , "/RelValZMM_13/CMSSW_10_6_14-PU25ns_106X_mc2017_realistic_v7_HS-v1/MINIAODSIM")
ZMM_bugfix = Sample("ZMM_bugfix" , 1 , False , "/RelValZMM_13/CMSSW_10_6_14_Pyt8240BugFix-PU25ns_106X_mc2017_realistic_v7_HS-v1/MINIAODSIM")
ZMM_bugfix_highstat = Sample("ZMM_bugfix_highstat" , 1 , False , "/RelValZMM_13/CMSSW_10_6_14_Pyt8240BugFix-PU25ns_106X_mc2017_realistic_v7_HS_rsb-v1/MINIAODSIM")
MINIAOD.extend( [ ZMM_bug, ZMM_bugfix, ZMM_bugfix_highstat, bug, bugfix ] )
