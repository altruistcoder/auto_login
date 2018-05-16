from selenium import webdriver
import time
import getpass


# Enter your codechef credentials

username = ""
password = getpass.getpass("Password: ")


# Replace your problem code here

problem_code = 'TEST'


# Replace your submission code here

code = """
#include <iostream>
using namespace std;
int main()
{
    int n;
    while(1)
    {
        cin>>n;
        if(n==42)
            break;
        cout<<n<<endl;
    }
    return 0;
} 
"""

# To open the browser

browser = webdriver.Firefox()

# To open codechef website

browser.get('https://www.codechef.com')
time.sleep(5) # sleep function to let web components load in case of slow internet connnection

# To login into your codechef account

nameElem = browser.find_element_by_id('edit-name')
nameElem.send_keys(username)


passElem = browser.find_element_by_id('edit-pass')
passElem.send_keys(password)

browser.find_element_by_id('edit-submit').click()
time.sleep(5)

# To open problem submission page

browser.get("https://www.codechef.com/submit/" + problem_code)
time.sleep(5)


# To click on toggle button to open simple text mode

browser.find_element_by_id("edit_area_toggle_checkbox_edit-program").click()


# To submit the code

inputElem = browser.find_element_by_id('edit-program')

inputElem.send_keys(code)

browser.find_element_by_id("edit-submit").click()
