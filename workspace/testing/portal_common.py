from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
import common, info

def select_qty(browser, qty):

    elem_qty = browser.find_element_by_id('cart_subscription_attributes_cart_items_attributes_0_charges_attributes_1_quantity')
    elem_qty.clear()
    elem_qty.send_keys(qty)
    elem_cont = browser.find_element_by_xpath('//*[@id="product-footer"]/div/button')
    elem_cont.click()
   
def billing_info(browser, click, user):

    elem_comp_name = browser.find_element_by_id('cart_customer_info_attributes_company_name')
    elem_comp_name.send_keys(user.comp_name)
    
    elem_first_name = browser.find_element_by_id('cart_customer_info_attributes_billing_address_attributes_first_name')
    elem_first_name.send_keys(user.first_name)
    
    elem_last_name = browser.find_element_by_id('cart_customer_info_attributes_billing_address_attributes_last_name')
    elem_last_name.send_keys(user.last_name)
    
    elem_addr1 = browser.find_element_by_id('cart_customer_info_attributes_billing_address_attributes_address')
    elem_addr1.send_keys(user.addr1)
    
    elem_city = browser.find_element_by_id('cart_customer_info_attributes_billing_address_attributes_city')
    elem_city.send_keys(user.city)
    
    Select(browser.find_element_by_name("cart[customer_info_attributes][billing_address_attributes][country]")).select_by_visible_text(user.country)
    elem_abbr_country = browser.find_element_by_xpath('//*[@name = "cart[customer_info_attributes][billing_address_attributes][country]"]/option[contains(text(),"'+user.country+'")]')    
    user.abbr_country = elem_abbr_country.get_attribute("value")
    
    #elem_country = browser.find_element_by_xpath("//*[contains(text(),'"+country+"')]")
    #elem_country.click()
    
    #browser.implicitly_wait(30) #need to give it a second or 2 to load the next dropdown
    
    Select(browser.find_element_by_name("cart[customer_info_attributes][billing_address_attributes][state]")).select_by_visible_text(user.state)
        
    #elem_state = browser.find_element_by_xpath("//*[@value='"+state+"']")
    #elem_state.click() 
        
    elem_zipcode = browser.find_element_by_id('cart_customer_info_attributes_billing_address_attributes_zip')
    elem_zipcode.send_keys(user.zipcode)
    
    elem_email = browser.find_element_by_id('cart_customer_info_attributes_billing_address_attributes_email')
    elem_email.send_keys(user.email)
    
    elem_confirm_email = browser.find_element_by_id('cart_customer_info_attributes_billing_address_attributes_confirm_email')
    elem_confirm_email.send_keys(user.email)
   
    if click: 
        # click on continue
        elem_cont = browser.find_element_by_xpath('//*[@id="address-footer"]/div/button')
        elem_cont.click()

def diff_delivery_info(browser, click, user):
    
    diff_delivery_info_checkbox = browser.find_element_by_id('cart_customer_info_attributes_shipping_address_attributes_check_different')
    diff_delivery_info_checkbox.click()
    
    elem_diff_first_name = browser.find_element_by_id('cart_customer_info_attributes_shipping_address_attributes_first_name')
    elem_diff_first_name.send_keys(user.first_name)
    elem_diff_last_name = browser.find_element_by_id('cart_customer_info_attributes_shipping_address_attributes_last_name')
    elem_diff_last_name.send_keys(user.last_name)
    elem_diff_addr1 = browser.find_element_by_id('cart_customer_info_attributes_shipping_address_attributes_address')
    elem_diff_addr1.send_keys(user.addr1)
    elem_diff_city = browser.find_element_by_id('cart_customer_info_attributes_shipping_address_attributes_city')
    elem_diff_city.send_keys(user.city)
    Select(browser.find_element_by_name('cart[customer_info_attributes][shipping_address_attributes][country]')).select_by_visible_text(user.country)
    Select(browser.find_element_by_name('cart[customer_info_attributes][shipping_address_attributes][state]')).select_by_visible_text(user.state)
    elem_diff_zip = browser.find_element_by_id('cart_customer_info_attributes_shipping_address_attributes_zip')
    elem_diff_zip.send_keys(user.zipcode)
    elem_diff_email = browser.find_element_by_id('cart_customer_info_attributes_shipping_address_attributes_email')
    elem_diff_email.send_keys(user.email)
    elem_diff_confirm_email = browser.find_element_by_id('cart_customer_info_attributes_shipping_address_attributes_confirm_email')
    elem_diff_confirm_email.send_keys(user.email)
    
    if click:
        elem_continue_btn = browser.find_element_by_xpath('//*[@id = "address-footer"]/div/button')
        elem_continue_btn.click()
    
    
def payment_info(browser, user):
    
    # entering iframe
    browser.switch_to.frame("z_hppm_iframe")
    
    # give a little time for the frame to load
    #browser.implicitly_wait(2)

    time.sleep(2) #not sure why I need this, without it, the iframe refreshes after all the text has been inputed in it.

    #WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element_value((By.XPATH, '//*[@id="hpm-container"]/div[1]/h2'),'Payment Information'))

    elem_CC = browser.find_element_by_xpath('//*[@id="HostedPaymentMethod_CreditCard_creditCardNumber"]')
    elem_CC.send_keys(user.new_CC.num)
    
    elem_CC_month = browser.find_element_by_xpath("//*[@value='"+user.new_CC.month+"']")
    elem_CC_month.click()
    
    elem_CC_year = browser.find_element_by_xpath("//*[@value='"+user.new_CC.year+"']")
    elem_CC_year.click()
    
    elem_CC_CVV = browser.find_element_by_name('field_cardSecurityCode')
    elem_CC_CVV.send_keys(user.new_CC.CVV)
    
    # come out of iframe
    browser.switch_to.default_content()
      
    elem_cont_payment = browser.find_element_by_xpath('//*[@id="submit-hpm-button"]/div/div/button')
    elem_cont_payment.click()
    

def review_your_data(browser, user):
    #give time for processing
    time.sleep(3)
    
    elem_confirm_sub = browser.find_element_by_id('cart_subscription_attributes_confirm_subscription')
    elem_confirm_sub.click()
    
    elem_buy_now = browser.find_element_by_xpath('//*[@id="buy-now-button"]/div/div/button')
    elem_buy_now.click()
    
    common.explicit_wait_until(browser, 15, '//*[contains(text(), "Thank you for your order!")]')
    
    #take down all the info for the subscription
    elem_qty = browser.find_elements_by_xpath('//*/div[@class = "per-product-qty"]/p/span')[1]
    elem_product = browser.find_element_by_xpath('//*/div[@class = "product-title"]/p/b')
    elem_unitPrice = browser.find_element_by_xpath('//*/div[@class = "per-product-price"]/p/span')
    elem_tax = browser.find_elements_by_xpath('//*/span[@class = "tax ng-binding"]')[1]
    elem_total = browser.find_element_by_xpath('//*/span[@class = "totalprice ng-binding"]')
    
    #saving all the cart purchase information
    user.new_sub.product_qty_unitPrice.append((elem_product.text, elem_qty.text, elem_unitPrice.text))
    user.new_sub.tax = elem_tax.text
    user.new_sub.total = elem_total.text
    
    print "Cart Purchased: "
    user.new_sub.print_sub()
        
def portal_activate(browser):
    
#   try:
#       WebDriverWait(browser,10).until(EC.visibility_of_element_located(), message)
            
    update_pwd = 'Anotherpass1'
    
    elem_here_link = browser.find_element_by_xpath('//*[@href="/verifyEmail"]')
    elem_here_link.click()
    
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
              
    
def portal_purchase(browser, user, qty):
    
    user.new_sub.qty = qty
    
    select_qty(browser, qty)
    billing_info(browser, True, user)      
    payment_info(browser, user)
    review_your_data(browser, user)
  #  portal_activate(browser)
    
       
def portal_link_generator(bool_prod, product):
    
    if bool_prod:
        return "https://shop.malwarebytes.org/carts/" + product
    else: 
        return "http://mwbtest.herokuapp.com/carts/" + product