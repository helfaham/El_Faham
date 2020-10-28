#!/bin/bash
scp *.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2016/ZeroBias
scp ./corr/*_Nominal.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2016/ZeroBias
scp ./corr/*_APV.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2016/ZeroBias_APV
scp ./FitRes/*.png helfaham@server02.fynu.ucl.ac.be:~/public_html/pileup/UL/2016/ZeroBias
#make sure things are sent directly to the APV directory next time
