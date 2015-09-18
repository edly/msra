import random
import socket
import urllib2
import cookielib
import time
import re

def adjust(s):
    ret = ''
    cnt = 0
    for i in range(0, len(s)):
        if (s[i] == '<'):
            cnt = cnt + 1
        else:
            if (s[i] == '>'):
                cnt = cnt - 1
            else:
                if (cnt == 0):
                    ret = ret + s[i]
    return ret

def parse1(s, num, line):
    str = r'is a unit|to other unit|from other unit'
    str2 = r'Unit system|unit system'
    infoList = re.findall(re.compile(str), s)
    tmp = re.findall(re.compile(str2), s)
    #for info in infoList:
    #    file.write(adjust(info) + '\n')
    if (len(infoList) > 0 and len(tmp) == 0):
        print num, line
    if (len(infoList) > 0):
        return True
    return False