import os
os.system("git clone https://github.com/50-scratch-tabs/CanYouDecodeThisEngine")
os.chdir("CanYouDecodeThisEngine")
os.system("python3 -m CanYouDecodeThis.gen_html")
os.rename("build/html/","../build")
