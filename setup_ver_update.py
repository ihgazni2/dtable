from efdir import fs
import re

def update_one(line):
    regex = re.compile('(.*)("[0-9]+\.[0-9]+\.)([0-9]+)(".*)')
    groups = regex.search(line)
    g3 = str(int(groups[3])+1)
    line =  groups[1] + groups[2] + g3 + groups[4]
    return(line)

def rplc_ver():
    s = fs.rfile("./setup.py")
    lines = s.split("\n")
    for i in range(len(lines)):
        if("#@version@#" in lines[i]):
            line = lines[i]
            lines[i] = update_one(line)
            break
        else:
            pass
    s = ""
    for i in range(len(lines)):
        s = s + lines[i] + "\n"
    fs.wfile("./setup.py",s)

rplc_ver()
