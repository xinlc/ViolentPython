#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mechanicalsoup  # pip3 install MechanicalSoup # https://github.com/MechanicalSoup/MechanicalSoup
def viewPage(url):
  browser = mechanicalsoup.StatefulBrowser()
  browser.open(url)
  print(browser.get_current_page())

  # Fill-in the search form
  # browser.select_form('#search_form_homepage')
  # browser["q"] = "MechanicalSoup"
  # browser.submit_selected()

  # Display the results
  # for link in browser.get_current_page().select('a.result__a'):
      # print(link.text, '->', link.attrs['href'])

def main():
  viewPage('http://www.baidu.com')

if __name__ == '__main__':
  main()