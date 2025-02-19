import os
os.system("git clone https://github.com/50-scratch-tabs/CanYouDecodeThisEngine")
open("CanYouDecodeThisEngine/ciphers.txt","wb").write(open("ciphers.txt","rb").read())
os.chdir("CanYouDecodeThisEngine")
os.system("python3 -m CanYouDecodeThis.gen_html")
os.rename("build/html/","../build")
os.system("git add build")
os.system('git commit -m "Automated build"')
