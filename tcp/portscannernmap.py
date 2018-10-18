
#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
使用nmap端口扫描
'''

import nmap
import optparse

def nmapScan(tgtHost, tgtPort):
  nmScan = nmap.PortScanner()
  nmScan.scan(tgtHost, tgtPort)
  state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
  print(" [*] " + tgtHost + " tcp/" + tgtPort + " " + state)

def main():
  tgtHost = 'www.baidu.com'
  tgtPort = '80'
  nmapScan(tgtHost, tgtPort)

if __name__ == '__main__' :
  main()