from Haamm.HaNaMiniAnalyzer.Sample import *

import os
Sample.WD = os.path.dirname(os.path.abspath(__file__))
print Sample.WD

MINIAOD = []
#2018
SingleMuonA  = Sample( "SingleMuA"  ,  0 , False ,  "/SingleMuon/Run2018A-17Sep2018-v2/MINIAOD" )
SingleMuonB  = Sample( "SingleMuB"  ,  0 , False ,  "/SingleMuon/Run2018B-17Sep2018-v1/MINIAOD" )
SingleMuonC  = Sample( "SingleMuC"  ,  0 , False ,  "/SingleMuon/Run2018C-17Sep2018-v1/MINIAOD" )
SingleMuonD  = Sample( "SingleMuD"  ,  0 , False ,  "/SingleMuon/Run2018D-22Jan2019-v2/MINIAOD" )

MINIAOD.extend( [ SingleMuonA , SingleMuonB , SingleMuonC , SingleMuonD ] )

#2018
ZMuMuM1 = Sample( "ZmuMuM1" , 1 , False , "/DYJetsToLL_M-50_TuneCP1_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-FlatPU0to75TuneCP1_102X_upgrade2018_realistic_v15-v1/MINIAODSIM")
ZMuMuM5 = Sample( "ZmuMuM5" , 1 , False , "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-FlatPU0to75TuneCP5_102X_upgrade2018_realistic_v15-v1/MINIAODSIM")

MINIAOD.extend( [ ZMuMuM1 , ZMuMuM5  ] ) 

#2018
ZeroBiasA = Sample("ZeroBiasA" , 0 , False , "/ZeroBias/Run2018A-17Sep2018-v1/MINIAOD")
ZeroBiasB = Sample("ZeroBiasB" , 0 , False , "/ZeroBias/Run2018B-17Sep2018-v1/MINIAOD")
ZeroBiasC = Sample("ZeroBiasC" , 0 , False , "/ZeroBias/Run2018C-17Sep2018-v1/MINIAOD")
ZeroBiasD = Sample("ZeroBiasD" , 0 , False , "/ZeroBias/Run2018D-PromptReco-v2/MINIAOD")
ZeroBiasE = Sample("ZeroBiasE" , 0 , False , "/ZeroBias/Run2018E-PromptReco-v1/MINIAOD")

MINIAOD.extend( [ ZeroBiasA , ZeroBiasB , ZeroBiasC , ZeroBiasD , ZeroBiasE ] )

#2018
#SingleNeutrinoTuneCP1_1   = Sample("SingleNeutrinoTuneCP1_1" , 1 , False , "/SingleNeutrino/RunIIAutumn18MiniAOD-FlatPU0to75TuneCP1_102X_upgrade2018_realistic_v15_ext4-v1/MINIAODSIM" )
#SingleNeutrinoTuneCP1_2   = Sample("SingleNeutrinoTuneCP1_2" , 1 , False , "/SingleNeutrino/RunIIAutumn18MiniAOD-FlatPU0to75TuneCP1_102X_upgrade2018_realistic_v15_ext2-v1/MINIAODSIM" )
SingleNeutrinoTuneCP5     = Sample("SingleNeutrinoTuneCP5"   , 1 , False , "/SingleNeutrino/RunIIAutumn18MiniAOD-FlatPU0to75TuneCP5_102X_upgrade2018_realistic_v15_ext5-v1/MINIAODSIM" )
SingleNeutrinoTuneCP1_1   = Sample("SingleNeutrinoTuneCP1" , 1 , False , "/SingleNeutrino/RunIIAutumn18MiniAOD-FlatPU0to75TuneCP1_102X_upgrade2018_realistic_v15_ext4-v1/MINIAODSIM" )
SingleNeutrinoTuneCP1_2   = Sample("SingleNeutrinoTuneCP1" , 1 , False , "/SingleNeutrino/RunIIAutumn18MiniAOD-FlatPU0to75TuneCP1_102X_upgrade2018_realistic_v15_ext2-v1/MINIAODSIM" )

SingleNeutrinos = []
#MINIAOD.extend( [ SingleNeutrinoTuneCP1_1 , SingleNeutrinoTuneCP1_2, SingleNeutrinoTuneCP5 ] )
MINIAOD.extend( [ SingleNeutrinoTuneCP1, SingleNeutrinoTuneCP5 ] )
#SingleNeutrinos.extend( [ SingleNeutrinoTuneCP1_1 , SingleNeutrinoTuneCP1_2, SingleNeutrinoTuneCP5 ] )
SingleNeutrinos.extend( [ SingleNeutrinoTuneCP1,  SingleNeutrinoTuneCP5 ] )
