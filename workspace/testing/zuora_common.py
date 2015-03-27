from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import common

def login(browser):
    
    zuora_site = 'https://apisandbox.zuora.com/login.html'
    browser.get(zuora_site)
    
    username = 'cli@malwarebytes.org'
    pwd = 'Nu7#gc4t2RDK'
    
    #navigate to iframe
    browser.switch_to_frame('newlogin')
    
    elem_username = browser.find_element_by_id('id_username')
    elem_username.send_keys(username)
    elem_pwd = browser.find_element_by_id('id_password')
    elem_pwd.send_keys(pwd)
    elem_pwd.send_keys(Keys.RETURN)
    
    #return
    browser.switch_to.default_content()
    
def check_subscription(browser, user):
    
    #check for the page to load by finding element
    elem_subscription = common.implicit_wait_until(browser, 10, '//*[@id="m1"]/dl/dd/a[contains(.,"Subscriptions")]')
    
    assert browser.current_url == 'https://apisandbox.zuora.com/apps/home.do', \
        "Not currently on Home page"
         
    elem_subscription.click()
      
   
     
