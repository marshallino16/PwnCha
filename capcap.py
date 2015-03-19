# -*- coding: iso-8859-15 -*-
import os, sys, re, subprocess
import fileinput
import hashlib
import time
import math
import urllib
import urllib2
import cookielib

from PIL import Image
from operator import itemgetter

#https://www.hscripts.com/scripts/jquery/captcha-code.php

millis = int(round(time.time()))
imgGenerator = "http://localhost/captcha/captcha/image.php?"
formPage = "http://localhost/captcha/"
basewidth = 500

#print("[+] Setting up cookies storage");

cookies = cookielib.LWPCookieJar()
handlers = [
    urllib2.HTTPHandler(),
    urllib2.HTTPSHandler(),
    urllib2.HTTPCookieProcessor(cookies)
    ]

opener = urllib2.build_opener(*handlers)

#print("[+] Downloading Page");

req = urllib2.Request(formPage)
site = opener.open(req)
site_html = site.read()
#print("---page loaded")
#print("---cookie retrieve");
#for cookie in cookies:
    #print cookie.name, cookie.value

#print("[+] Downloading Captcha");
f = open('captcha.png','wb')
reqImg = urllib2.Request(imgGenerator+str(millis))
siteImg = opener.open(reqImg)
f.write(siteImg.read())
f.close()

#print("\n[+] Resizing image");
imgToResize = Image.open("captcha.png")
wpercent = (basewidth/float(imgToResize.size[0]))
hsize = int((float(imgToResize.size[1])*float(wpercent)))
imgToResize = imgToResize.resize((basewidth,hsize), Image.ANTIALIAS)
imgToResize.save('captcha.png')

im = Image.open("captcha.png")
im = im.convert("P")
im2 = Image.new("P",im.size,16)

#get a complete histogram of color by hex value 0 to 255 -> 256 colors
#print("\n[+] Getting color histogram");
his = im.histogram()
#print his
#sort histogram color by most present color | ID | COUNT |
values = {}

for i in range(256):
  values[i] = his[i]

#for j,k in sorted(values.items(), key=itemgetter(1), reverse=True)[:10]:
#  print '\t ' + str(j) + ' | ' + str(k)

#print '\n'
temp = {}
for x in range(im.size[1]):
  for y in range(im.size[0]):
    pix = im.getpixel((y,x))
    temp[pix] = pix
    if pix == 92 or pix == 98 or pix == 140 or pix == 141 or pix == 134:
        im2.putpixel((y,x),0)
    else:
        im2.putpixel((y,x),255)

im2.save('captchaCustom.png')

#print '[+] OCR converting and analyzin'

cmdConvert = '/usr/local/bin/convert -density 200 -units PixelsPerInch -type Grayscale +compress captchaCustom.png captchaConverted.tif'
cmdOCR = '/usr/local/bin/tesseract captchaConverted.tif outputOCR'

os.system(cmdConvert)
os.system(cmdOCR)

#print '[+] Reading result'
fh = open("outputOCR.txt", "r")
value = fh.read().replace(" ", "").split('\n')
#print 'output is = ' + value[0]


#print("[+] Sending request...");
method = "POST"

data = urllib.urlencode({'captcha' : value[0]})
req = urllib2.Request(formPage, data)
connect = opener.open(req)

content = connect.read()
#print(content);

if "Successful!........" in str(content):
    print("Success.");
else:
    print("Fail.");

#print("[+] Finished!");
