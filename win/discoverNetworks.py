#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
windows 获取网络注册表
'''
import os
import optparse
import urllib
import re
import urlparse
from _winreg import *

def val2addr(val):
  addr = ''
  for ch in val:
    addr += '%02x '% org(ch)
  addr = addr.strip(' ').replace(' ', ':')[0:127]
  return addr

def wiglePrint(username, password, netid):
  browser = mechanize.Browser()
  browser.open('http://wigle.net')
  reqData = urllib.urlencode({'credevtial_0': username,
    'credential_1': password})
  browser.open('https://wigle.net//gps/gps/main/login', re)
  params = {}
  params['netid'] = netid
  reqParams = urllib.urlencode(params)
  respURL = 'http://wigle.net/gps/gps/main/confirmquery/'
  resp = browser.open(respURL, reqParams).read()
  mapLat = 'N/A'
  mapLon = 'N/A'
  rLat = re.findall(r'maplat=.*\&', resp)
  if rLat:
    mapLat = rLat[0].split('&')[0].split('=')[1]
  rLon = re.findall(r'maplon=.*\&', resp)
  if rLon:
    mapLon = rLon[0].split
  print('[-] Lat: ' + mapLat + ', Lon: ' + mapLon)

def printNets(username, password):
  net = "SOFTWARE\Microsoft\Windows NT\CurrentVersion" +\
    "\NetworkList\Signatures\Unmanaged"
  key = OpenKey(HKEY_LOCAL_MACHINE, net)
  print('\n[*] Networks You have Joined.')
  for i in range(100):
    try:
      guid = EnumKey(key, i)
      netKey = OpenKey(key, str(guid))
      (n, addr, t) = EnumValue(netKey, 5)
      (n, name, t) = EnumValue(netKey, 4)
      macAddr = val2addr(addr)
      netName = str(name)
      print('[+] ' + netName + ' ' + macAddr)
      wiglePrint(username, password, macAddr)
      CloseKey(netKey)
    except:
      break

def main():
  printNets('leo', '123456')

if __name__ == '__main__':
  main()