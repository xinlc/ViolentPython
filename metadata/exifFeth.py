#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
获取HTML中的图片，解析元数据
Exif(exchange image file formate, 交换图像文件格式)
https://sno.phy.queensu.ca/~phil/exiftool/
'''
import ssl
import urllib.request
import optparse
from urllib.parse import urlsplit
from os.path import basename
from bs4 import BeautifulSoup
from PIL import Image          # Pillow
from PIL.ExifTags import TAGS

# 取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context

def findImages(url):
  try:
    print('[+] Finding images on ' + url)
    file = urllib.request.urlopen(url)
    urlContent = file.read()
    soup = BeautifulSoup(urlContent)
    imgTags = soup.findAll('img')
    return imgTags
  except Exception as e:
    print(e)

def downloadImage(imgTag):
  try:
    print('[+] Download image...')
    imgSrc = imgTag['src']
    # print('[+] Download image...' + imgSrc)
    imgContent = urllib.request.urlopen(imgSrc).read()
    imgFileName = basename(urlsplit(imgSrc)[2])
    imgFile = open(imgFileName, 'wb')
    imgFile.write(imgContent)
    imgFile.close()
    return imgFileName
  except:
    return ''

def testForExif(imgFileName):
  try:
    exifData = {}
    imgFile = Image.open(imgFileName)
    info = imgFile._getexif()
    if info:
      for (tag, value) in info.items():
        decoded = TAGS.get(tag, tag)
        exifData[decoded] = value
      exifGPS = exifData['GPSInfo']
      if exifGPS:
        print('[*] ' + imgFileName +\
          ' contains GPS MetaData' + str(exifGPS))
  except:
    pass

def main():
  parser = optparse.OptionParser('usage%prog ' +\
    '-u <target url>')
  parser.add_option('-u', dest='url', type='string',
    help='specify url address')
  (options, args) = parser.parse_args()
  url = options.url
  if url == None:
    print(parser.usage)
    exit(0)
  else:
    imgTags = findImages(url)
    for imgTag in imgTags:
      imgFileName = downloadImage(imgTag)
      testForExif(imgFileName)

if __name__ == '__main__':
  main()

'''
python3 exifFeth.py -u https://www.flickr.com/photos/dvids/4999001925/sizes/o
'''