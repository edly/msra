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
    if (len(re.findall(re.compile(r'is a unit|to other unit|from other unit|Unit system|unit system'), s)) == 0):
        return "-1"
    if (len(re.findall(re.compile(r'/input/\?i=(time)&'), s)) > 0):
        return "TIME"
    if (len(re.findall(re.compile(r'/input/\?i=(([a-zA-Z]+\+)*length|width|height|depth|thickness|radius|distance|wavelength)&'), s)) > 0):
        return "1D"
    if (len(re.findall(re.compile(r'/input/\?i=(area|surface\+area)&'), s)) > 0):
        return "2D"
    if (len(re.findall(re.compile(r'/input/\?i=(volume)(&|\+of)'), s)) > 0):
        return "3D"
    if (len(re.findall(re.compile(r'/input/\?i=(mass)&'), s)) > 0):
        return "Mass"
    if (len(re.findall(re.compile(r'/input/\?i=(temperature\+difference)&'), s)) > 0):
        return "Temperature"
    if (len(re.findall(re.compile(r'/input/\?i=(energy)&'), s)) > 0):
        return "Physical:Energy"
    if (len(re.findall(re.compile(r'/input/\?i=(speed)&'), s)) > 0):
        return "Speed"
    if (len(re.findall(re.compile(r'/input/\?i=(pressure)&'), s)) > 0):
        return "Physical:Pressure"
    if (len(re.findall(re.compile(r'/input/\?i=([a-zA-Z]+\+)*(power)&'), s)) > 0):
        return "Physical:Power"
    if (len(re.findall(re.compile(r'/input/\?i=(force)&'), s)) > 0):
        return "Physical:Force"
    if (len(re.findall(re.compile(r'dimensionless'), s)) > 0):
        return "Unknown"
    if (len(re.findall(re.compile(r'/input/\?i=(information|data\+word)&'), s)) > 0):
        return "Information"
    if (len(re.findall(re.compile(r'/input/\?i=([a-zA-Z]+\+)*(momentum)&'), s)) > 0):
        return "Physical:Momentum"
    if (len(re.findall(re.compile(r'/input/\?i=(plane\+angle)&'), s)) > 0):
        return "Angle"
    if (len(re.findall(re.compile(r'/input/\?i=([a-zA-Z]+\+)*(frequency)&'), s)) > 0):
        return "Frequency"
    if (len(re.findall(re.compile(r'/input/\?i=(equivalent\+dose\+of\+ionizing\+radiation)&'), s)) > 0):
        return "Physical:Radiation"
    if (len(re.findall(re.compile(r'/input/\?i=(music(\+[a-zA-Z]+)*)&'), s)) > 0):
        return "Music"
    if (len(re.findall(re.compile(r'/input/\?i=(electric\+(resistance|current))&'), s)) > 0):
        return "Physical:Electric"
    if (len(re.findall(re.compile(r'/input/\?i=(electric\+potential\+difference)&'), s)) > 0):
        return "Physical:Electric"
    if (len(re.findall(re.compile(r'/input/\?i=(periodic\+phenomena\+cycle)&'), s)) > 0):
        return "PeriodicPhenomenaCycle"
    if (len(re.findall(re.compile(r'/input/\?i=(radioactivity)&'), s)) > 0):
        return "Physical:Radiation"
    if (len(re.findall(re.compile(r'/input/\?i=(volume\+flow)&'), s)) > 0):
        return "Physical:VolumeFlow"
    if (len(re.findall(re.compile(r'/input/\?i=(mass\+density)&'), s)) > 0):
        return "Physical:MassDensity"
    if (len(re.findall(re.compile(r'/input/\?i=(luminance)&'), s)) > 0):
        return "Physical:Luminance"
    return "Unknown"