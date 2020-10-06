from Haamm.HaNaMiniAnalyzer.Sample import *

import os
Sample.WD = os.path.dirname(os.path.abspath(__file__))
print Sample.WD

MINIAOD = []
#2018
ZeroBiasA = Sample("ZeroBiasA" , 0 , False , "/ZeroBias/Run2018A-12Nov2019_UL2018-v2/MINIAOD")
ZeroBiasB = Sample("ZeroBiasB" , 0 , False , "/ZeroBias/Run2018B-12Nov2019_UL2018-v2/MINIAOD")

MINIAOD.extend( [ ZeroBiasA , ZeroBiasB ] )

MinBiasA = Sample("MinBiasA" , 0 , False , "/MinimumBias/Run2018A-12Nov2019_UL2018-v1/MINIAOD")
MinBiasB = Sample("MinBiasB" , 0 , False , "/MinimumBias/Run2018B-12Nov2019_UL2018-v1/MINIAOD")
MinBiasC = Sample("MinBiasC" , 0 , False , "/MinimumBias/Run2018C-12Nov2019_UL2018-v1/MINIAOD")
MinBiasD = Sample("MinBiasD" , 0 , False , "/MinimumBias/Run2018D-12Nov2019_UL2018-v1/MINIAOD")

MINIAOD.extend( [ MinBiasA , MinBiasB, MinBiasC, MinBiasD ] )
#2018
#SingleNeutrinoType1   = Sample("SingleNeutrinoType1" , 1 , False , "/SingleNeutrino/RunIISummer19UL18MiniAOD-UL18HEMreReco_pilot_106X_upgrade2018_realistic_v11_L1v1-v2/MINIAODSIM" )
#SingleNeutrinoType2   = Sample("SingleNeutrinoType2" , 1 , False , "/SingleNeutrino/RunIISummer19UL18MiniAOD-FlatPU0to70_106X_upgrade2018_realistic_v11_L1v1-v1/MINIAODSIM" )

SingleNeutrino_CP1   = Sample("SingleNeutrino_CP1" , 1 , False , "/SingleNeutrino/RunIISummer19UL18MiniAOD-FlatPU0to75_106X_upgrade2018_realistic_v11_L1v1_ext2-v2/MINIAODSIM" )
SingleNeutrino_CP5   = Sample("SingleNeutrino_CP5" , 1 , False , "/SingleNeutrino/RunIISummer19UL18MiniAOD-FlatPU0to75_106X_upgrade2018_realistic_v11_L1v1_ext1-v1/MINIAODSIM" )

SingleNeutrinos = []

MINIAOD.extend( [ SingleNeutrino_CP1 , SingleNeutrino_CP5 ] )
SingleNeutrinos.extend( [ SingleNeutrino_CP1 , SingleNeutrino_CP5 ] )
#MINIAOD.extend( [ SingleNeutrinoType1, SingleNeutrinoType2, SingleNeutrino_CP1 , SingleNeutrino_CP5 ] )
#SingleNeutrinos.extend( [ SingleNeutrinoType1, SingleNeutrinoType2, SingleNeutrino_CP1 , SingleNeutrino_CP5 ] )
