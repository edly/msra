import random
import socket
import urllib2
import cookielib
import time
import re
import parse

match = open("match.txt", "r")
output = open("output.txt", "w")

cnt = 0
a = set()

while True:
    num = match.readline().strip()
    if not num:
        break
    num = int(num)
    #print num
    word = match.readline().strip().lower()
    if word in a:
        print num, word
    a.add(word)
    s = open("data\\" + str(num) + ".txt", "r").readlines()
    html = ""
    for line in s:
        html = html + line
    ret = parse.parse1(html, num, word)
    if (ret == "-1"):
        continue
    output.write(ret + '\n' + word + '\n')
print cnt