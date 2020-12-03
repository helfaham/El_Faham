#!/bin/bash

#big picture plots
scp *.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2017/ZeroBias

#correlation plots
scp ./corr/*.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2017/ZeroBias/corr_plots

#FitRes
scp ./FitRes/new_test_plots/All/*.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2017/ZeroBias/vars_All
scp ./FitRes/new_test_plots/eraB/*.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2017/ZeroBias/vars_eraB
scp ./FitRes/new_test_plots/eraC/*.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2017/ZeroBias/vars_eraC
scp ./FitRes/new_test_plots/eraD/*.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2017/ZeroBias/vars_eraD
scp ./FitRes/new_test_plots/eraE/*.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2017/ZeroBias/vars_eraE
scp ./FitRes/new_test_plots/eraF/*.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2017/ZeroBias/vars_eraF

#Gaussfits
scp ./gaussfits/*_All_test.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2017/ZeroBias/gaussfits_All
scp ./gaussfits/*_eraB_test.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2017/ZeroBias/gaussfits_eraB
scp ./gaussfits/*_eraC_test.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2017/ZeroBias/gaussfits_eraC
scp ./gaussfits/*_eraD_test.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2017/ZeroBias/gaussfits_eraD
scp ./gaussfits/*_eraE_test.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2017/ZeroBias/gaussfits_eraE
scp ./gaussfits/*_eraF_test.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2017/ZeroBias/gaussfits_eraF
