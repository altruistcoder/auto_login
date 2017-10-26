from selenium import webdriver

import getpass



# Facebook credentials for login (Add your username here)

username = ""

password = getpass.getpass("Password:")



# To open the browser

browser = webdriver.Firefox()



# To open link in browser

browser.get('https://www.facebook.com')



# To Login

nameElem = browser.find_element_by_id('email')

nameElem.send_keys(username)


passElem = browser.find_element_by_id('pass')

passElem.send_keys(password)

 
browser.find_element_by_id('loginbutton').click()

