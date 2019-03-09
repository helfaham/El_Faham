from Haamm.HaNaMiniAnalyzer.Sample import *

import os
Sample.WD = os.path.dirname(os.path.abspath(__file__))
print Sample.WD

MINIAOD = []
#2017
SingleMuonB  = Sample( "SingleMuB"  ,  0 , False ,  "/SingleMuon/Run2017B-31Mar2018-v1/MINIAOD" )
SingleMuonC  = Sample( "SingleMuC"  ,  0 , False ,  "/SingleMuon/Run2017C-31Mar2018-v1/MINIAOD" )
SingleMuonD  = Sample( "SingleMuD"  ,  0 , False ,  "/SingleMuon/Run2017D-31Mar2018-v1/MINIAOD" )
SingleMuonE  = Sample( "SingleMuE"  ,  0 , False ,  "/SingleMuon/Run2017E-31Mar2018-v1/MINIAOD" )
SingleMuonF  = Sample( "SingleMuF"  ,  0 , False ,  "/SingleMuon/Run2017F-31Mar2018-v1/MINIAOD" )
SingleMuonG  = Sample( "SingleMuG"  ,  0 , False ,  "/SingleMuon/Run2017G-17Nov2017-v1/MINIAOD" )
SingleMuonH1 = Sample( "SingleMuH1" ,  0 , False ,  "/SingleMuon/Run2017H-17Nov2017-v1/MINIAOD" )
SingleMuonH2 = Sample( "SingleMuH2" ,  0 , False ,  "/SingleMuon/Run2017H-17Nov2017-v2/MINIAOD" )

MINIAOD.extend( [ SingleMuonB , SingleMuonC , SingleMuonD , SingleMuonE , SingleMuonF , SingleMuonG , SingleMuonH1 , SingleMuonH2 ] )

#DYMuMu0J = Sample( "DYMuMu0J" , 1 , False ,  "/DYToLL_0J_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM" )
#DYMuMu1J = Sample( "DYMuMu1J" , 1 , False ,  "/DYToLL_1J_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM" )
#DYMuMu2J = Sample( "DYMuMu2J" , 1 , False ,  "/DYToLL_2J_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM" )

#2017
ZMuMuM1 = Sample( "ZmuMuM1" , 1 , False , "/DYJetsToLL_M-50_TuneCP1_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-FlatPU0to75TuneCP1_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM")
ZMuMuM5 = Sample( "ZmuMuM5" , 1 , False , "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17/RunIIFall17MiniAODv2-FlatPU0to75TuneCP5_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM")

MINIAOD.extend( [ ZMuMuM1 , ZMuMuM5  ] ) #, ZMuMu, DYMuMu0J , DYMuMu1J , DYMuMu2J ] )

#NuGunM1 = Sample("NuGunM1" , 1 , False , "/NeutrinoGun_E_10GeV/RunIISummer16MiniAODv2-FlatPU0to75TuneCUETP8M1_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM")
#NuGunM2 = Sample("NuGunM2" , 1 , False , "/NeutrinoGun_E_10GeV/RunIISummer16MiniAODv2-FlatPU0to75TuneCUETP8M2_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM")
#NuGunM3 = Sample("NuGunM3" , 1 , False , "/NeutrinoGun_E_10GeV/RunIISummer16MiniAODv2-FlatPU0to75TuneCUETP8M3_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM")
#NuGunM4 = Sample("NuGunM4" , 1 , False , "/NeutrinoGun_E_10GeV/RunIISummer16MiniAODv2-FlatPU0to75TuneCUETP8M4_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM")

#MINIAOD.extend( [ NuGunM1 , NuGunM2 , NuGunM3 , NuGunM4 ] )

#2017
MinBiasA3 = Sample("MinBiasA3"  , 0 , False , "/MinimumBias/Run2017A-PromptReco-v3/MINIAOD")
MinBiasA2 = Sample("MinBiasA2"  , 0 , False , "/MinimumBias/Run2017A-PromptReco-v2/MINIAOD")
MinBiasA1 = Sample("MinBiasA1"  , 0 , False , "/MinimumBias/Run2017A-PromptReco-v1/MINIAOD")
MinBiasB2 = Sample("MinBiasB2"  , 0 , False , "/MinimumBias/Run2017B-PromptReco-v2/MINIAOD")
MinBiasB1 = Sample("MinBiasB1"  , 0 , False , "/MinimumBias/Run2017B-PromptReco-v1/MINIAOD")
MinBiasC3 = Sample("MinBiasC3"  , 0 , False , "/MinimumBias/Run2017C-PromptReco-v3/MINIAOD")
MinBiasC2 = Sample("MinBiasC2"  , 0 , False , "/MinimumBias/Run2017C-PromptReco-v2/MINIAOD")
MinBiasC1 = Sample("MinBiasC1"  , 0 , False , "/MinimumBias/Run2017C-PromptReco-v1/MINIAOD")
MinBiasD  = Sample("MinBiasD"   , 0 , False , "/MinimumBias/Run2017D-PromptReco-v1/MINIAOD")
MinBiasE  = Sample("MinBiasE"   , 0 , False , "/MinimumBias/Run2017E-PromptReco-v1/MINIAOD")
MinBiasF  = Sample("MinBiasF"   , 0 , False , "/MinimumBias/Run2017F-PromptReco-v1/MINIAOD")
MinBiasG  = Sample("MinBiasG"   , 0 , False , "/MinimumBias/Run2017G-PromptReco-v1/MINIAOD")
MinBiasH  = Sample("MinBiasH"   , 0 , False , "/MinimumBias/Run2017H-PromptReco-v1/MINIAOD")

MINIAOD.extend( [ MinBiasA3, MinBiasA2, MinBiasA1, MinBiasB2 , MinBiasB1, MinBiasC3, MinBiasC2, MinBiasC1,  MinBiasD , MinBiasE , MinBiasF , MinBiasG , MinBiasH ] )

#2017
ZeroBiasH = Sample("ZeroBiasH" , 0 , False , "/ZeroBias/Run2017H-17Nov2017-v1/MINIAOD")
ZeroBiasG = Sample("ZeroBiasG" , 0 , False , "/ZeroBias/Run2017G-17Nov2017-v1/MINIAOD")
ZeroBiasF = Sample("ZeroBiasF" , 0 , False , "/ZeroBias/Run2017F-31Mar2018-v1/MINIAOD")
ZeroBiasE = Sample("ZeroBiasE" , 0 , False , "/ZeroBias/Run2017E-31Mar2018-v1/MINIAOD")
ZeroBiasD = Sample("ZeroBiasD" , 0 , False , "/ZeroBias/Run2017D-31Mar2018-v1/MINIAOD")
ZeroBiasC = Sample("ZeroBiasC" , 0 , False , "/ZeroBias/Run2017C-31Mar2018-v1/MINIAOD")

MINIAOD.extend( [ ZeroBiasC , ZeroBiasD , ZeroBiasE , ZeroBiasF , ZeroBiasG , ZeroBiasH ] )

#2017
SingleNeutrinoTuneCP1 = Sample("SingleNeutrinoTuneCP1" , 1 , False , "/SingleNeutrino/RunIIFall17MiniAODv2-FlatPU0to75TuneCP1_12Apr2018_94X_mc2017_realistic_v14_ext3-v1/MINIAODSIM" )
SingleNeutrinoTuneCP5 = Sample("SingleNeutrinoTuneCP5" , 1 , False , "/SingleNeutrino/RunIIFall17MiniAODv2-FlatPU0to75TuneCP5_12Apr2018_94X_mc2017_realistic_v14_ext2-v1/MINIAODSIM" )

SingleNeutrinos = []
MINIAOD.extend( [ SingleNeutrinoTuneCP1 , SingleNeutrinoTuneCP5 ] )
SingleNeutrinos.extend( [ SingleNeutrinoTuneCP1 , SingleNeutrinoTuneCP5 ] )
