import os
os.system("git clone https://github.com/50-scratch-tabs/CanYouDecodeThisEngine")
os.chdir("cd CanYouDecodeThisEngine")
os.system("python3 CanYouDecodeThisEngine/gen_html.py")
os.rename("build/html","../build")
