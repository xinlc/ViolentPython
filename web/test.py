from anonBrowser import *
ab = anonBrowser(proxies=[], user_agents=['superSecretBroser'])
for attempt in range(1,5):
  ab.anonymize()
  response = ab.open('http://www.baidu.com')
  for cookie in ab.cookie_jar:
    print(cookie)
