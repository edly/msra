import random
import socket
import urllib2
import cookielib
import time
import re
import parse

new = open("unit-new", "r")
out1 = open("unit-abbr-v3", "w")
out2 = open("unit-all-v3", "w")


cnt = 0
abbr = set()
for word in open("unit-abbr-v1", "r").readlines():
    abbr.add(word.strip().lower())

all = set()
for word in open("unit-all-v1", "r").readlines():
    all.add(word.strip().lower())

ban = set()
for word in open("banlist", "r").readlines():
    ban.add(word.strip().lower())

while True:
    tmp = new.readline().strip()
    if not word:
        break
    word = new.readline().strip().lower()
    if word in ban:
        continue
    if word in all:
        out2.write(tmp + '\n' + word + '\n')
        continue
    if word in abbr:
        out1.write(tmp + '\n' + word + '\n')
    else:
        out2.write(tmp + '\n' + word + '\n')