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
