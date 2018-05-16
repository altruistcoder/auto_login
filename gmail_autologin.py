from selenium import webdriver
import getpass
import time


username = "" # Enter your username here

password = getpass.getpass("Enter your Password: ")


# For opening the browser

browser = webdriver.Firefox()

browser.get('https://www.google.com/')

time.sleep(5)


# Login

browser.find_element_by_xpath('/html/body/nav/div/a[2]').click()

time.sleep(2)

nameElem = browser.find_element_by_xpath('//*[@id="identifierId"]')

nameElem.send_keys(username)

browser.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()

time.sleep(2)

passElem = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')

passElem.send_keys(password)
 
browser.find_element_by_xpath('//*[@id="passwordNext"]/content/span').click()

