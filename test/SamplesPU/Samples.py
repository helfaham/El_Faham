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

SingleNeutrino   = Sample("SingleNeutrinoType1"   , 1 , False , "/SingleNeutrino/RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM" )
SingleNeutrino_FlatPU = Sample("SingleNeutrinoType2" , 1 , False , "/SingleNeutrino/RunIISummer19UL17MiniAOD-FlatPU0to75_106X_mc2017_realistic_v6_ext2-v1/MINIAODSIM" )

SingleNeutrinos = []
MINIAOD.extend( [ SingleNeutrinoType1 , SingleNeutrinoType2 ] )
SingleNeutrinos.extend( [ SingleNeutrinoType1 , SingleNeutrinoType2 ] )
