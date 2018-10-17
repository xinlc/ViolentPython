#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
zip破解
'''
import zipfile

def extractFile(zFile, password):
  try:
    zFile.extractall(pwd=password.encode("ascii"))
    return password
  except Exception as err:
    # print(err)
    return

def main():
  zFile = zipfile.ZipFile('evil.zip')
  passFile = open('dictionary.txt')
  for line in passFile.readlines():
    password = line.split('\n')[0]
    guess = extractFile(zFile, password)
    if guess:
      print('[+] Password = ' + password + '\n')
      exit(0)

if __name__ == '__main__':
  main()