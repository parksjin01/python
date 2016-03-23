#-*- coding: utf-8 -*-
import os
import subprocess
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
cmd=[]
c=''

while True:
    cmd=raw_input()
    pmd=subprocess.check_output(c+cmd+';pwd', shell=True).split('\n')
    for i in pmd:
        print i;
    c='cd '+''.join(pmd[-2])+';'
