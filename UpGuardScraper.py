import urllib
from concurrent.futures import thread
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

url = input("What is your url? ")


# class DmarcCheck:
#     browser = webdriver.Chrome("chromedriver.exe")
#     browser.get("https://mxtoolbox.com/dmarc.aspx")
#     browser.find_element_by_id("ctl00_ContentPlaceHolder1_ucToolhandler_txtToolInput").send_keys(url)
#     browser.find_element_by_id("ctl00_ContentPlaceHolder1_ucToolhandler_btnAction").click()
#     sleep(5)
#     browser.execute_script("window.scrollBy(0, 500);")
#     dmarc = browser.find_element_by_class_name("table-column-Response")
#     print("DMARC Results: " + dmarc.text)
#     dmarc = browser.find_element_by_class_name("table-column-Response")
#     print("DMARC Results: " + dmarc.text)

# class DkimCheck:
#    browser = webdriver.Chrome("chromedriver.exe")
#    browser.get("https://mxtoolbox.com/dkim.aspx")
#    browser.find_element_by_id("ctl00_ContentPlaceHolder1_ucToolhandler_txtToolInput").send_keys(url)

# class SpfCheck:
#   browser = webdriver.Chrome("chromedriver.exe")
#  browser.get("https://mxtoolbox.com/spf.aspx")
# browser.find_element_by_id("ctl00_ContentPlaceHolder1_ucToolhandler_txtToolInput").send_keys(url)
# browser.find_element_by_id("ctl00_ContentPlaceHolder1_ucToolhandler_btnAction").click()
#browser = webdriver.Chrome("chromedriver.exe")
#x = 1


class UpGuardCheck:
    browser = webdriver.Chrome("chromedriver.exe")
    browser.get("https://webscan.upguard.com/")
    browser.find_element_by_id("score-input").clear()
    browser.find_element_by_id("score-input").send_keys(url)
    browser.find_element_by_id("score-action").click()
    sleep(5)
    browser.execute_script("window.scrollBy(0, 1000);")
    sleep(2)
    try:
        browser.find_element_by_xpath("""//*[@id="accordian-cards"]/div[""" + str(1) + """]""").click()
        browser.find_element_by_xpath("""//*[@id="accordian-cards"]/div[""" + str(2) + """]""").click()
        browser.find_element_by_xpath("""//*[@id="accordian-cards"]/div[""" + str(3) + """]""").click()
        browser.find_element_by_xpath("""//*[@id="accordian-cards"]/div[""" + str(4) + """]""").click()
        browser.find_element_by_xpath("""//*[@id="accordian-cards"]/div[""" + str(5) + """]""").click()
        browser.find_element_by_xpath("""//*[@id="accordian-cards"]/div[""" + str(6) + """]""").click()
        browser.find_element_by_xpath("""//*[@id="accordian-cards"]/div[""" + str(7) + """]""").click()
        browser.find_element_by_xpath("""//*[@id="accordian-cards"]/div[""" + str(8) + """]""").click()
        browser.find_element_by_xpath("""//*[@id="accordian-cards"]/div[""" + str(9) + """]""").click()
        browser.find_element_by_xpath("""//*[@id="accordian-cards"]/div[""" + str(10) + """]""").click()
    except NoSuchElementException:
        pass
    try:
        browser.find_element_by_xpath("""//*[@id="passing-cards"]/div[""" + str(3) + """]""").click()
        browser.find_element_by_xpath("""//*[@id="passing-cards"]/div[""" + str(4) + """]""").click()
        browser.find_element_by_xpath("""//*[@id="passing-cards"]/div[""" + str(5) + """]""").click()
        browser.find_element_by_xpath("""//*[@id="passing-cards"]/div[""" + str(6) + """]""").click()
        browser.find_element_by_xpath("""//*[@id="passing-cards"]/div[""" + str(7) + """]""").click()
        browser.find_element_by_xpath("""//*[@id="passing-cards"]/div[""" + str(8) + """]""").click()
        browser.find_element_by_xpath("""//*[@id="passing-cards"]/div[""" + str(9) + """]""").click()
        browser.find_element_by_xpath("""//*[@id="passing-cards"]/div[""" + str(10) + """]""").click()
        browser.find_element_by_xpath("""//*[@id="passing-cards"]/div[""" + str(11) + """]""").click()
        browser.find_element_by_xpath("""//*[@id="passing-cards"]/div[""" + str(12) + """]""").click()
        browser.find_element_by_xpath("""//*[@id="passing-cards"]/div[""" + str(13) + """]""").click()
    except NoSuchElementException:
        element = browser.find_element_by_id("accordian-cards")
        print("Site Overview: " + element.text)
# print(element.text)
# print(url + " risk assessment done")


