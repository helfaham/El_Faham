#!/usr/bin/env python
import sys
import getpass
user = getpass.getuser()


import os
from os import listdir

eras=["All"]
eras.extend(["era"+ c for c in ["B","C","D","E","F","G","H"]])

#puScenarios = {"pcc" :[95,105,5], "bestfit":[95,105,5], "latest":[84,117,1]}
puScenarios = {"latest" :[84,117,1]}

workingdir = sys.argv[1] 
while os.path.isdir( "./%s" % (workingdir) ):
    workingdir += "_"
os.mkdir( workingdir )

from subprocess import call
call(["voms-proxy-init" , "--out" , "/tmp/.x509up_u%d" % (os.getuid()) , "--voms" , "cms" , "--valid" , "1000:0"])

file_sh = open ("%s/Submit.sh" % (workingdir), "w")
import shutil
from shutil import copy

for puScenario in puScenarios:
    variation = puScenarios[puScenario]
    xsecs="%d-%d:%d" % (variation[0], variation[1], variation[2])
    for era in eras:
        if not era.count("B"):
           continue 
        os.mkdir( "%s/%s" % (workingdir , era) )
        shutil.copy( "Plotter.py" , "./%s/%s" % (workingdir,era))

        file = open ("%s/%s/Submit.cmd" % (workingdir, era), "w")
        print >> file, "universe                = vanilla"
        print >> file, "executable              = %s/%s/%s/Plotter.py" % (os.getcwd() , workingdir , era)
        print >> file, "output                  = $(ClusterId)_$(ProcId).out"
        print >> file, "error                   = $(ClusterId)_$(ProcId).err"
        print >> file, "log                     = $(ClusterId)_$(ProcId).log"
        print >> file, '+JobFlavour             = "tomorrow"'
        print >> file, "environment             = CONDORJOBID=$(ProcId)"
        print >> file, "notification            = Error"
        print >> file, "should_transfer_files   = YES"
        print >> file, "when_to_transfer_output = ON_EXIT"
        print >> file, "transfer_input_files    = /afs/cern.ch/user/h/helfaham/CMSSW_8_4_0/src/Haamm/HaNaMiniAnalyzer/test/SamplesPU/Samples.py, /afs/cern.ch/user/h/helfaham/CMSSW_8_4_0/src/Haamm/HaNaMiniAnalyzer/test/SamplesPU/__init__.py"
        print >> file, ""
        print >> file, "arguments               = %(puScenario)s %(Appendix)s " % {
		"puScenario":puScenario ,
                "Appendix"  :era
		}
        print >> file, "queue 1"
        print >> file, ""
        file.close()

        print >> file_sh, "cd %s" % (era)
        print >> file_sh, "condor_submit -batch-name %s Submit.cmd" % (era)
        print >> file_sh, "cd .."


print "to submit the jobs, you have to run the following commands :"
print "cd %s" % (workingdir)
print "source Submit.sh"
file_sh.close()

