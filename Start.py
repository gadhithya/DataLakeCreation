import ExecuteCommand
import sys
import os
from paramiko import SSHClient
support_dump_path=sys.argv[1]
support_dump_customer=sys.argv[2]
support_dump_path=support_dump_path+"mysupport-output.tar"
print ExecuteCommand.execute(["ls","-lah",support_dump_path]).split()
support_dump_filedetails=os.stat(support_dump_path)
if(support_dump_filedetails[6]>0):
    volumelist = ExecuteCommand.checkVolume(support_dump_customer)
    if(len(volumelist)==0):
        ExecuteCommand.execute(["maprcli","volume","create", support_dump_path,"-path","/prophecy/"+support_dump_customer])
