# Project     : text-list-sorter
# Script      : app.py
# Description : main program script
# Author      : DOMINGUES PEDROSA SamueWl
# Date        : 2023.02.01, V1.0
import os, shutil, sys

file = sys.argv[1]

os.makedirs('./.tmp/', exist_ok=True)

#f = open('.tmp/a.txt', 'a')
strg = ""
#lst = open(file, 'rt')
#lines = lst.readlines()
with open(file, 'rt', encoding='utf-8', errors='ignore') as lines:
    for line in lines:
        with open(f'.tmp/{line.lower()[0]}.txt', 'at') as f:
            f.write(line)


#lst.close()

#shutil.rmtree('.tmp/')