import selenium
from selenium import webdriver
import time

browser = webdriver.Firefox()

browser.get("http://www.nasdaq.com/markets/unusual-volume.aspx")
time.sleep(3)

#let's get all the up stocks first
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
upStocks = browser.find_elements_by_tag_name("td")
i = 0
listOfUpStocks = []
print "UP stocks"
for up in upStocks:
    i += 1
    if (i - 1) % 7 == 0:
        if up.text != "":
            listOfUpStocks.append(up.text)
for stock in listOfUpStocks:
    print stock

#let's get all the down otocks
navSwitch = browser.find_element_by_id("tab2")
navSwitch.click()
time.sleep(3)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
downStocks = browser.find_elements_by_tag_name("td")
j = 0
listOfDownStocks = []
print "---------------------------------"
print "Down stocks"
for down in downStocks:
    j += 1
    if (j - 1) % 7 == 0: 
        if down.text != "":
            listOfDownStocks.append(down.text)
for stock in listOfDownStocks:
    print stock

browser.close()
