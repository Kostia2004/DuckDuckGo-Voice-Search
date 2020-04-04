from STT import listen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib

request = urllib.parse.quote_plus(listen())
print('OK')

browser = webdriver.Chrome()
browser.get('https://duckduckgo.com/?q='+request+'&t=h_&ia=web')
