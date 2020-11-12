#!/bin/bash

#big picture plots
scp *_Nominal.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2016/ZeroBias
scp *_APV.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2016/ZeroBias_APV

#correlation plots
scp ./corr/*_Nominal.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2016/ZeroBias/corr_plots
scp ./corr/*_APV.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2016/ZeroBias_APV/corr_plots

#FitRes Normal
scp ./FitRes/new_test_plots/All/*.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2016/ZeroBias/vars_All
scp ./FitRes/new_test_plots/eraF/*.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2016/ZeroBias/vars_eraF
scp ./FitRes/new_test_plots/eraG/*.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2016/ZeroBias/vars_eraG
scp ./FitRes/new_test_plots/eraH/*.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2016/ZeroBias/vars_eraH

#FitRes APV
scp ./FitRes/new_test_plots/All_APV/*_APV.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2016/ZeroBias_APV/vars_All
scp ./FitRes/new_test_plots/eraB_APV/*_APV.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2016/ZeroBias_APV/vars_eraB
scp ./FitRes/new_test_plots/eraC_APV/*_APV.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2016/ZeroBias_APV/vars_eraC
scp ./FitRes/new_test_plots/eraD_APV/*_APV.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2016/ZeroBias_APV/vars_eraD
scp ./FitRes/new_test_plots/eraE_APV/*_APV.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2016/ZeroBias_APV/vars_eraE
scp ./FitRes/new_test_plots/eraF_APV/*.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2016/ZeroBias_APV/vars_eraF

#Gaussfits Nominal
scp ./gaussfits/*_All_test.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2016/ZeroBias/gaussfits_All
scp ./gaussfits/*_eraF_test.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2016/ZeroBias/gaussfits_eraF
scp ./gaussfits/*_eraG_test.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2016/ZeroBias/gaussfits_eraG
scp ./gaussfits/*_eraH_test.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2016/ZeroBias/gaussfits_eraH

#Gaussfits APV 
scp ./gaussfits/*_All_test_APV.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2016/ZeroBias_APV/gaussfits_All
scp ./gaussfits/*_eraB_test_APV.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2016/ZeroBias_APV/gaussfits_eraB
scp ./gaussfits/*_eraC_test_APV.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2016/ZeroBias_APV/gaussfits_eraC
scp ./gaussfits/*_eraD_test_APV.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2016/ZeroBias_APV/gaussfits_eraD
scp ./gaussfits/*_eraE_test_APV.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2016/ZeroBias_APV/gaussfits_eraE
scp ./gaussfits/*_eraF_test_APV.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2016/ZeroBias_APV/gaussfits_eraF
