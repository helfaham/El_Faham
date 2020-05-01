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
SingleNeutrino   = Sample("SingleNeutrino" , 1 , False , "/SingleNeutrino/RunIISummer19UL18MiniAOD-FlatPU0to70_106X_upgrade2018_realistic_v11_L1v1-v1/MINIAODSIM" )

SingleNeutrinos = []
MINIAOD.extend( [ SingleNeutrino ] )
SingleNeutrinos.extend( [ SingleNeutrino ] )


#2018 AOD test
AODtest = Sample("AODtest","1",False,"/SingleNeutrino/RunIISummer19UL18RECO-FlatPU0to70_106X_upgrade2018_realistic_v11_L1v1-v1/AODSIM ")
AODtests=[]
MINIAOD.extend([AODtest])
AODtests.extend([AODtest])
