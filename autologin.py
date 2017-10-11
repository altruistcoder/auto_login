from selenium import webdriver

import getpass



# Hackerearth credentials for login (Add your username)

username = ""

password = getpass.getpass("Password:")



# To open the browser

browser = webdriver.Firefox()



# To open link in browser

browser.get('https://www.hackerearth.com/login')



# To Login

nameElem = browser.find_element_by_id('id_login')

nameElem.send_keys(username)


passElem = browser.find_element_by_id('id_password')

passElem.send_keys(password)

 
browser.find_element_by_name('signin').click()

