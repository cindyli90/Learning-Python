from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import time
import common, info

def login(browser):
    
    zuora_site = 'https://apisandbox.zuora.com/login.html'
    browser.get(zuora_site)
    
    Z_info = info.ZuoraInfo()

    
    #navigate to iframe
    browser.switch_to_frame('newlogin')
    
    elem_username = browser.find_element_by_id('id_username')
    elem_username.send_keys(Z_info.username)
    elem_pwd = browser.find_element_by_id('id_password')
    elem_pwd.send_keys(Z_info.pwd)
    elem_pwd.send_keys(Keys.RETURN)
    
    # Exit iframe
    browser.switch_to.default_content()
    
def check_subscription(browser, user):
    
    #check for the page to load by finding element
    elem_subscription = common.explicit_wait_until(browser, 5, '//*[@id="m1"]/dl/dd/a[contains(.,"Subscriptions")]')
       
    assert browser.current_url == 'https://apisandbox.zuora.com/apps/home.do', \
        "Not currently on Home page"
         
    # Goes to Zuora Subscription page
    elem_subscription.click()
    
    customer_name = ''.join([user.first_name, ' ', user.last_name])
    print "Customer name: %s" % (customer_name)
    
    try:
        elem_customer = common.refresh_and_find_element(browser, '//*[contains(., "'+customer_name+'")]/a', 10)
    except NoSuchElementException:
        assert False, "Customer not found"
    
    elem_customer.click()
        
        
        
    #common.bkpoint()
    
    #refresh and check for customer name in table
    # try:
        # #elem_customer = common.refresh_and_check_text(browser, '//*[contains(text(), customer_name)]/a', customer_name)
# #        elem_customer = common.refresh_and_check_text(browser, '//*[contains(@id,"customer.customerName")]', customer_name)
    # except NoSuchElementException:
        # assert "couldn't find customer"
    
    #elem_customer.click()
#    common.bkpoint()
	
      
   
     
