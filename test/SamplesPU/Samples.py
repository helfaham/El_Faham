from Haamm.HaNaMiniAnalyzer.Sample import *

import os
Sample.WD = os.path.dirname(os.path.abspath(__file__))
print Sample.WD

MINIAOD = []
#2018
ZeroBiasA = Sample("ZeroBiasA" , 0 , False , "/ZeroBias/Run2018A-12Nov2019_UL2018-v2/MINIAOD")
ZeroBiasB = Sample("ZeroBiasB" , 0 , False , "/ZeroBias/Run2018B-12Nov2019_UL2018-v2/MINIAOD")

MINIAOD.extend( [ ZeroBiasA , ZeroBiasB ] )

#2018
SingleNeutrino   = Sample("SingleNeutrinoType1" , 1 , False , "/SingleNeutrino/RunIISummer19UL18MiniAOD-UL18HEMreReco_pilot_106X_upgrade2018_realistic_v11_L1v1-v2/MINIAODSIM" )
SingleNeutrino_FlatPU   = Sample("SingleNeutrinoType2" , 1 , False , "/SingleNeutrino/RunIISummer19UL18MiniAOD-FlatPU0to70_106X_upgrade2018_realistic_v11_L1v1-v1/MINIAODSIM" )

SingleNeutrinos = []
MINIAOD.extend( [ SingleNeutrinoType1, SingleNeutrinoType2 ] )
SingleNeutrinos.extend( [ SingleNeutrinoType1, SingleNeutrinoType2 ] )
