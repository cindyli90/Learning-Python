from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

def login(browser):
       
    browser.get('https://test.salesforce.com/')
    assert 'salesforce.com - Customer Secure Login Page' == browser.title, \
        "title not the same"
    
    elem_uid = browser.find_element_by_name('username') #find username
    elem_uid.send_keys('sfdc_qa@malwarebytes.org.fullsand')
    
    elem_uid = browser.find_element_by_name('pw')  # Find password
    elem_uid.send_keys('fESs0vSN%4&J')

    elem_uid.send_keys(Keys.RETURN)
    
    

def new_account(browser):
    
    login(browser)
    