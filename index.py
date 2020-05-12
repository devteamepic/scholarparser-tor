# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
import argparse
import time
import random
import os.path
import os

from datetime import date, timedelta
import traceback
import urllib.parse

from langdetect import detect, detect_langs

import dateparser
from tqdm import tqdm_notebook


# #Chrome
# options = webdriver.ChromeOptions()
# #options.add_argument('headless')
# #options.add_argument('--headless')
# prefs = {"profile.default_content_setting_values.notifications" : 2}
# options.add_experimental_option("prefs",prefs)
# options.add_argument('--disable-logging')
# options.add_argument("--disable-dev-shm-usage");
# options.add_argument('--log-level=3')
# options.add_argument("start-maximized"); #// open Browser in maximized mode
# options.add_argument("disable-infobars"); #// disabling infobars
# options.add_argument("--disable-extensions"); #// disabling extensions
# options.add_argument("--disable-gpu"); #// applicable to windows os only
# options.add_argument("--disable-dev-shm-usage"); #// overcome limited resource problems
# options.add_argument("--no-sandbox"); #// Bypass OS security model
#
# driver = webdriver.Chrome(options=options)

def open_page(num, browser):
    browser.get(f'https://scholar.google.com/scholar?cites=6150928651221943815&as_sdt=2005&sciodt=0,5&as_ylo={num}&as_yhi={num}')
    time.sleep(random.randint(0, 40))
    try:
        number_of_docs=max([int(n.replace(',','')) for n in browser.find_elements_by_class_name('gs_ab_mdw')[1].text.split() if n.replace(',','').isdigit()])
        print(num, number_of_docs)
        return True
    except:
        browser.close()
        return False


# Tor setup
socks_ports = [9050, 9052, 9053, 9054, 9055, 9056, 9057, 9058, 9059, 9060, 9061, 9062, 9063, 9064, 9065, 9066, 9068]


# специфичные настройки моей версии фаерфокс
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False

# тут нужно поставить свой путь к бинарнику (у меня убунту)
binary = FirefoxBinary(r"/home/paydaylight/b_firefox/firefox")


# показывает что для каждого SOCKS порта используется разный айпишник
def flex():
    for port in socks_ports:
        profile = FirefoxProfile()
        profile.set_preference('network.proxy.type', 1)
        profile.set_preference('network.proxy.socks', '127.0.0.1')
        profile.set_preference('network.proxy.socks_port', port)
        driver = webdriver.Firefox(profile, binary, capabilities=cap)
        driver.get("http://api.ipify.org/")
        print(driver.find_element_by_tag_name('pre').text)
        time.sleep(4)
        driver.close()


for y in range(1979, 2021):
    profile = FirefoxProfile()
    profile.set_preference('network.proxy.type', 1)
    profile.set_preference('network.proxy.socks', '127.0.0.1')
    profile.set_preference('network.proxy.socks_port', socks_ports.pop())
    driver = webdriver.Firefox(profile, binary, capabilities=cap)

    while open_page(y, driver) != True:
        profile = FirefoxProfile()
        profile.set_preference('network.proxy.type', 1)
        profile.set_preference('network.proxy.socks', '127.0.0.1')
        profile.set_preference('network.proxy.socks_port', socks_ports.pop())
        driver = webdriver.Firefox(profile, binary, capabilities=cap)




