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

def parse1(s, num, word):
    ret = -1
    if (len(re.findall(re.compile(r'is a unit|to other unit|from other unit|Unit system|unit system'), s)) > 0):
        ret = 0
    if (ret == -1):
        return ret
    if (len(re.findall(re.compile(r'/input/\?i=(time)&'), s)) > 0):
        return -1
    if (len(re.findall(re.compile(r'/input/\?i=(length|width|height|depth|thickness|radius|distance|wavelength)&'), s)) > 0):
        ret = 1
    if (len(re.findall(re.compile(r'/input/\?i=(area|surface\+area)&'), s)) > 0):
        ret = 2
    if (len(re.findall(re.compile(r'/input/\?i=(volume)&'), s)) > 0):
        ret = 3
    if (len(re.findall(re.compile(r'/input/\?i=(mass)&'), s)) > 0):
        ret = 4
    if (len(re.findall(re.compile(r'/input/\?i=(temperature\+difference)&'), s)) > 0):
        ret = 5
    if (len(re.findall(re.compile(r'/input/\?i=(energy)&'), s)) > 0):
        ret = 6
    if (len(re.findall(re.compile(r'/input/\?i=(speed)&'), s)) > 0):
        ret = 7
    if (len(re.findall(re.compile(r'/input/\?i=(pressure)&'), s)) > 0):
        ret = 8
    if (len(re.findall(re.compile(r'/input/\?i=(power)&'), s)) > 0):
        ret = 9
    if (len(re.findall(re.compile(r'/input/\?i=(force)&'), s)) > 0):
        ret = 10
    if (len(re.findall(re.compile(r'dimensionless'), s)) > 0):
        ret = 11
    if (len(re.findall(re.compile(r'/input/\?i=(information)&'), s)) > 0):
        ret = 12
    return ret