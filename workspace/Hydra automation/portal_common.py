from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

def select_qty(browser, qty):
    elem_qty = browser.find_element_by_id('cart_subscription_attributes_cart_items_attributes_0_charges_attributes_1_quantity')
    elem_qty.clear()
    elem_qty.send_keys(qty)
    elem_cont = browser.find_element_by_xpath('//*[@id="product-footer"]/div/button')
    elem_cont.click()
   
def billing_info(browser, comp_name, first_name, last_name, addr1, city, state, zipcode, country, email):

    elem_comp_name = browser.find_element_by_id('cart_customer_info_attributes_company_name')
    elem_comp_name.send_keys(comp_name)
    
    elem_first_name = browser.find_element_by_id('cart_customer_info_attributes_billing_address_attributes_first_name')
    elem_first_name.send_keys(first_name)
    
    elem_last_name = browser.find_element_by_id('cart_customer_info_attributes_billing_address_attributes_last_name')
    elem_last_name.send_keys(last_name)
    
    elem_addr1 = browser.find_element_by_id('cart_customer_info_attributes_billing_address_attributes_address')
    elem_addr1.send_keys(addr1)
    
    elem_city = browser.find_element_by_id('cart_customer_info_attributes_billing_address_attributes_city')
    elem_city.send_keys(city)
    
    Select(browser.find_element_by_name("cart[customer_info_attributes][billing_address_attributes][country]")).select_by_visible_text(country)
    #elem_country = browser.find_element_by_xpath("//*[contains(text(),'"+country+"')]")
    #elem_country.click()
    
    #browser.implicitly_wait(30) #need to give it a second or 2 to load the next dropdown
    
    Select(browser.find_element_by_name("cart[customer_info_attributes][billing_address_attributes][state]")).select_by_visible_text(state)
        
    #elem_state = browser.find_element_by_xpath("//*[@value='"+state+"']")
    #elem_state.click() 
        
    elem_zipcode = browser.find_element_by_id('cart_customer_info_attributes_billing_address_attributes_zip')
    elem_zipcode.send_keys(zipcode)
    
    elem_email = browser.find_element_by_id('cart_customer_info_attributes_billing_address_attributes_email')
    elem_email.send_keys(email)
    
    elem_confirm_email = browser.find_element_by_id('cart_customer_info_attributes_billing_address_attributes_confirm_email')
    elem_confirm_email.send_keys(email)
    
    # click on continue
    elem_cont = browser.find_element_by_xpath('//*[@id="address-footer"]/div/button')
    elem_cont.click()

def payment_info(browser, CC, CC_CVV, CC_month, CC_year):
    
    # entering iframe
    browser.switch_to.frame("z_hppm_iframe")
    
    # give a little time for the frame to load
    #browser.implicitly_wait(2)

    time.sleep(2) #not sure why I need this, without it, the iframe refreshes after all the text has been inputed in it.

    #WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element_value((By.XPATH, '//*[@id="hpm-container"]/div[1]/h2'),'Payment Information'))

    elem_CC = browser.find_element_by_xpath('//*[@id="HostedPaymentMethod_CreditCard_creditCardNumber"]')
    elem_CC.send_keys(CC)
    
    elem_CC_month = browser.find_element_by_xpath("//*[@value='"+CC_month+"']")
    elem_CC_month.click()
    
    elem_CC_year = browser.find_element_by_xpath("//*[@value='"+CC_year+"']")
    elem_CC_year.click()
    
    elem_CC_CVV = browser.find_element_by_name('field_cardSecurityCode')
    elem_CC_CVV.send_keys(CC_CVV)
    
    # come out of iframe
    browser.switch_to.default_content()
      
    elem_cont_payment = browser.find_element_by_xpath('//*[@id="submit-hpm-button"]/div/div/button')
    elem_cont_payment.click()
    

def review_your_data(browser):
    #give time for processing
    time.sleep(3)
    
    elem_confirm_sub = browser.find_element_by_id('cart_subscription_attributes_confirm_subscription')
    elem_confirm_sub.click()
    
    elem_buy_now = browser.find_element_by_xpath('//*[@id="buy-now-button"]/div/div/button')
    elem_buy_now.click()
  
        
def portal_activate(browser):
    
#   try:
#       WebDriverWait(browser,10).until(EC.visibility_of_element_located(), message)
            
    update_pwd = 'Anotherpass1'
    
    elem_update_pwd = browser.find_element_by_id("password_password")
    elem_update_pwd.send_keys(update_pwd)
     
    elem_update_pwd_confirm = browser.find_element_by_id("password_confirm_password")
    elem_update_pwd_confirm.send_keys(update_pwd)
     
    elem_submit = browser.find_element_by_xpath('//*[@id="login-form"]/div[2]/form/div[4]/button')
    elem_submit.click()
    
#     try:
#         elem_update_pwd = WebDriverWait(browser, 10).until(EC.presence_of_element_located(browser.find_element_by_xpath('//*[@href="/verifyEmail"]')))
#         elem_update_pwd.click()
#     finally:
#         browser.quit()
        
#     elem_here_link = browser.find_element_by_xpath('//*[@href="/verifyEmail"]')
#     elem_here_link.click()
    
#     try:
#         elem_update_pwd = WebDriverWait(browser, 10).until(EC.presence_of_element_located(browser.find_element_by_id("password_password")))
#         elem_update_pwd.sendKeys(update_pwd)
#         
#         elem_update_pwd_confirm = browser.find_element_by_id("password_confirm_password")
#         elem_update_pwd_confirm.sendKeys(update_pwd)
#         
#         elem_submit = browser.find_element_by_xpath('//*[@id="login-form"]/div[2]/form/div[4]/button')
#         elem_submit.click()
#         
#     finally:
#         browser.quit()
              
    
def portal_purchase(browser):
    
    qty = '10'
    
    comp_name = 'Cindy is testing'
    first_name = 'Malware'
    last_name = 'Bytes'
    addr1 = '10 Almaden Blvd'
    city = 'San Jose'
    state = 'California'
    zipcode = '95113'
    country = 'United States'
    num = 2
    email = 'hydra-test-'+ str(num) +'@yopmail.com'
    

    CC = ""
    CC_CVV = "489"
    CC_month = "07"
    CC_year = "2015"
    
    select_qty(browser, qty)
    billing_info(browser, comp_name, first_name, last_name, addr1, city, state, zipcode, country, email)      
    payment_info(browser, CC, CC_CVV, CC_month, CC_year)
    
       
def portal_link_generator(bool_prod, product):
    
    if bool_prod:
        return "https://shop.malwarebytes.org/carts/" + product
    else: 
        return "http://mwbtest.herokuapp.com/carts/" + product