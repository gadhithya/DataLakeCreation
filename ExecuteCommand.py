from subprocess import Popen
import subprocess
import os
def execute(command):
    cmdout =Popen(command,stdout=subprocess.PIPE,stdin=subprocess.PIPE)
    out=cmdout.stdout.read()
    #print "Out: ",out.communicate()," EO"
    return out
def checkVolume(volumename):
    cmdout1 = Popen(["maprcli", "volume", "list"], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    cmdout2 = Popen(["grep",volumename], stdout=subprocess.PIPE, stdin=cmdout1.stdout)
    return cmdout2.stdout.read()