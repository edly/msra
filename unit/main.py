import random
import socket
import urllib2
import cookielib
import time
import re
import parse

match = open("D:\\crawl for unit\\work\\match.txt", "r")
all = open("D:\\crawl for unit\\work\\unit-abbr.txt", "r")

output = open("D:\\crawl for unit\\work\\output2.txt", "w")

a = set()
cnt = 0
while True:
    num = match.readline()
    if not num:
        break
    num = int(num)
    line = match.readline()
    line = line.lower()
    a.add(line)
while True:
    line = all.readline()
    if not line:
        break
    line = line.lower()
    if not line in a:
        output.write(line);
