import os
os.system("git clone https://github.com/50-scratch-tabs/CanYouDecodeThisEngine")
os.chdir("CanYouDecodeThisEngine")
os.system("python3 CanYouDecodeThis/gen_html.py")
os.rename("build/html/","../build")
