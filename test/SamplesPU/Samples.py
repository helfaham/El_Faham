from Haamm.HaNaMiniAnalyzer.Sample import *

import os
Sample.WD = os.path.dirname(os.path.abspath(__file__))
print Sample.WD

MINIAOD = []
#2017UL
ZeroBiasF = Sample("ZeroBiasF" , 0 , False , "/ZeroBias/Run2017F-09Aug2019_UL2017-v1/MINIAOD")
ZeroBiasE = Sample("ZeroBiasE" , 0 , False , "/ZeroBias/Run2017E-09Aug2019_UL2017-v1/MINIAOD")
ZeroBiasD = Sample("ZeroBiasD" , 0 , False , "/ZeroBias/Run2017D-09Aug2019_UL2017-v1/MINIAOD")
ZeroBiasC = Sample("ZeroBiasC" , 0 , False , "/ZeroBias/Run2017C-09Aug2019_UL2017-v1/MINIAOD")
ZeroBiasB = Sample("ZeroBiasB" , 0 , False , "/ZeroBias/Run2017B-09Aug2019_UL2017-v1/MINIAOD")

MINIAOD.extend( [ ZeroBiasB, ZeroBiasC , ZeroBiasD , ZeroBiasE , ZeroBiasF ] )

MinBiasB = Sample("MinBiasB" , 0 , False , "/MinimumBias/Run2017B-09Aug2019_UL2017-v1/MINIAOD")
MinBiasC = Sample("MinBiasC" , 0 , False , "/MinimumBias/Run2017C-09Aug2019_UL2017-v1/MINIAOD")
MinBiasD = Sample("MinBiasD" , 0 , False , "/MinimumBias/Run2017D-09Aug2019_UL2017-v1/MINIAOD")
MinBiasE = Sample("MinBiasE" , 0 , False , "/MinimumBias/Run2017E-09Aug2019_UL2017-v1/MINIAOD")
MinBiasF = Sample("MinBiasF" , 0 , False , "/MinimumBias/Run2017F-09Aug2019_UL2017-v1/MINIAOD")

MINIAOD.extend( [ MinBiasB, MinBiasC , MinBiasD , MinBiasE , MinBiasF ] )

#SingleNeutrino   	= Sample("SingleNeutrinoType1"   	, 1 , False , "/SingleNeutrino/RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM" )
#SingleNeutrino_FlatPU 	= Sample("SingleNeutrinoType2" 		, 1 , False , "/SingleNeutrino/RunIISummer19UL17MiniAOD-FlatPU0to75_106X_mc2017_realistic_v6_ext2-v1/MINIAODSIM" )

SingleNeutrino_CP5 = Sample("SingleNeutrino_CP5" , 1 , False , "/SingleNeutrino/RunIISummer19UL17MiniAOD-FlatPU0to75_106X_mc2017_realistic_v6_ext2-v1/MINIAODSIM" )
SingleNeutrino_CP1 = Sample("SingleNeutrino_CP1" , 1 , False , "/SingleNeutrino/RunIISummer19UL17MiniAOD-FlatPU0to75TuneCP1_106X_mc2017_realistic_v6_ext1-v2/MINIAODSIM" )

SingleNeutrinos = []
MINIAOD.extend( [ SingleNeutrino_CP5 , SingleNeutrino_CP1 ] )
SingleNeutrinos.extend( [ SingleNeutrino_CP5 , SingleNeutrino_CP1 ] )
