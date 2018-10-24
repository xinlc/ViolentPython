#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
ftp 扫描器
'''
import ftplib
def anonLogin(hostname):
  try:
    ftp = ftplib.FTP(hostname)
    ftp.login('anonymous', 'me@your.com')
    print('[*] ' + str(hostname) +\
      ' FTP Anonymous Logon Succeeded.')
    ftp.quit()
    return True
  except Exception as e:
    print('[-] ' + str(hostname) +\
      ' FTP Anonymous Logon Failed.')
    return False

host = '192.168.1.1'
anonLogin(host)