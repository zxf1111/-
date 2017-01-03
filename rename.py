#!/usr/bin/env python
# --*-- coding:utf-8 --*--

import os
import sys

folder = sys.argv[1]
filelist = os.listdir(folder)
os.chdir(folder)

for file in filelist:
    num = file.split()[-1].split('-')[0]
    print num
    if num == num:
        os.rename(file,num.zfill(2)+"."+file)
