#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
解析pdf文件元数据
'''
import optparse
from PyPDF2 import PdfFileReader

def printMeta(fileName):
  pdfFile = PdfFileReader(open(fileName, 'rb'))
  docInfo = pdfFile.getDocumentInfo()
  print('[*] PDF MetaData For: ' + str(fileName) )
  for metaItem in docInfo:
    print('[+] ' + metaItem + ':' + docInfo[metaItem])

def main():
  fileName = '/Users/cyq/Downloads/testdata.pdf'
  printMeta(fileName)

if __name__ == '__main__':
  main()