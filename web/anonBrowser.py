#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
匿名浏览
'''
import mechanicalsoup
import http.cookiejar
import random
import time

class anonBrowser(mechanicalsoup.StatefulBrowser):
  def __init__(self, proxies = [], user_agents = []):
    mechanicalsoup.StatefulBrowser.__init__(self)
    self.proxies = proxies
    self.user_agents = user_agents + ['Mozilla/4.0', \
      'FireFox/6.01', 'ExactSearch', 'Nokiz7110/1.0']
    self.cookie_jar = http.cookiejar.LWPCookieJar()
    self.set_cookiejar(self.cookie_jar)
    self.anonymize()
  def clear_cookies(self):
    self.cookie_jar = http.cookiejar.LWPCookieJar()
    self.set_cookiejar(self.cookie_jar)
  def change_user_agent(self):
    index = random.randrange(0, len(self.user_agents))
    self.set_user_agent(self.user_agents[index])
    # self.addheaders = [('User-agent', (self.user_agents[index]))]
  def change_proxy(self):
    if self.proxies:
      index = random.randrange(0, len(self.proxies))
      # self.set_proxies({'http': self.proxies[index]})
  def anonymize(self, sleep = False):
    self.clear_cookies()
    self.change_user_agent()
    self.change_proxy()
    if sleep:
      time.sleep(60)
