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
    
def check_zuora(self, browser, user):
    
    #check for the page to load by finding element
    elem_subscription = common.explicit_wait_until(browser, 5, '//*[@id="m1"]/dl/dd/a[contains(.,"Subscriptions")]')
       
    assert browser.current_url == 'https://apisandbox.zuora.com/apps/home.do', \
        "Not currently on Home page"
         
    # Goes to Zuora Subscription page
    elem_subscription.click()
    
    customer_name = user.comp_name
    print "Customer name: %s" % (customer_name)
    
    try:
        elem_customer = common.refresh_and_find_element(browser, '//*[contains(., "'+customer_name+'")]/a', 10)
    except NoSuchElementException:
        assert False, "Customer not found"
    
    elem_customer.click()
    
    check_zuora_Basic_Information(self, browser, user)
    check_zuora_Billing_and_Payment_Info(self, browser, user)
    check_zuora_Electronic_Payment_Methods(self, browser, user)
    check_zuora_Invoice(self, browser, user)
    
    common.verify_end(self)
    
def check_zuora_Basic_Information(self, browser, user):
    #Check Bill To
    elem_bill_to = browser.find_element_by_xpath('//*/table[@id = "basicInfo_table"]/tbody/tr/th[contains(.,"Bill")]/following-sibling::td')
    
    full_name = ''.join([user.first_name, ' ', user.last_name])
    
    if elem_bill_to.text != full_name:
        self.verify.append(("Bill To: %s does not match user name: %s") % (elem_bill_to.text, full_name))
        
def check_zuora_Billing_and_Payment_Info(self, browser, user):
        
    #Check payment term
    elem_payment_term = browser.find_element_by_id('paymentTerm')
    
    if elem_payment_term.text != 'Due Upon Receipt':
        self.verify.append(("Payment method: %s does not match 'Due Upon Receipt'") % elem_payment_term.text)

    #Check currency
    elem_currency = browser.find_element_by_id('currency')
    
    if elem_currency.text != 'USD':
        self.verify.append(("Currency: %s does not match 'USD'") % elem_currency.text)
        
    #Check payment gateway
    elem_payment_gateway = browser.find_element_by_id('paymentGateway')
    
    # if currency == USD, then payment gateway == 'Use Default Gateway'
    if (elem_currency.text == 'USD') and (elem_payment_gateway.text != 'MALWAREBYTES - USD'):
        self.verify.append(("Payment gateway: %s does not match 'MALWAREBYTES - USD'") % elem_payment_gateway.text)
        
        
def check_zuora_Electronic_Payment_Methods(self, browser, user):

    full_name = ''.join([user.first_name, ' ', user.last_name])

    #Check card number 
    elem_card_number = browser.find_elements_by_xpath('//*/th[contains(.," Card Number: ")]/following-sibling::td/span')[1]
    
    user_hidden_CC = ''.join(['*' * 12, user.new_CC.num[-4:]])

    if elem_card_number.text != user_hidden_CC:
        self.verify.append(("Card number: %s does not match user CC: %s") % (elem_card_number.text, user_hidden_CC))  
    
    #Check expiration date
    elem_exp = browser.find_elements_by_xpath('//*/th[contains(.," Expiration Date: ")]/following-sibling::td/span')[1]
    
    user_exp = ''.join([user.new_CC.month, '/', user.new_CC.year])
    
    if elem_exp.text != user_exp:
        self.verify.append(("Expiry: %s does not match user expiry: %s") % (elem_exp.text, user_exp))    
    
    #Check card holder name 
    elem_card_holder = browser.find_elements_by_xpath('//*/th[contains(.," Card Holder Name: ")]/following-sibling::td/span')[1]
    
    if elem_card_holder.text != full_name:
        self.verify.append(("Card holder: %s does not match user name: %s") % (elem_card_holder.text, full_name))
    
    #check last transaction
    elem_last_transaction = browser.find_elements_by_xpath('//*/th[contains(.," Last Transaction: ")]/following-sibling::td/span')[1]

    if elem_last_transaction.text != 'Approved':
        self.verify.append(("Last transaction: %s does not match 'Approved'") % elem_last_transaction.text)

def check_zuora_Invoice(self, browser, user):
    
    #click on invoice
    elem_invoice = browser.find_element_by_partial_link_text('INV')
    elem_invoice.click()
    
    #check invoice amount
    elem_invoice_amount = browser.find_element_by_xpath('//*/strong[contains(.,"Invoice Amount")]/following-sibling::span')
    
    if user.new_sub.total[1:] != elem_invoice_amount.text:
        self.verify.append('Invoice amount: %s does not match cart amount: %s' % (elem_invoice_amount.text, user.new_sub.total))
       
    #check payments
    elem_payments = browser.find_element_by_xpath('//*/strong[contains(.,"Payments")]/following-sibling::span')
    
    if user.new_sub.total[1:] != elem_payments.text:
        self.verify.append('Payment: %s does not match cart amount: %s' % (elem_payments.text, user.new_sub.total))
        
    #check outstanding balance
    elem_outstanding_balance = browser.find_element_by_xpath('//*/strong[contains(.,"Outstanding Balance")]/following-sibling::span')
    
    if elem_outstanding_balance.text != '0.00':
        self.verify.append('Outstanding Balance: %s is not 0.00' % elem_payments.text)    
    
    #check tax
    elem_tax = browser.find_element_by_xpath('//*[@id = "idOfTaxDetailTable"]/following-sibling::font')
    
    if user.new_sub.tax[1:] != elem_tax.text.strip():
        self.verify.append('Tax: %s does not match cart amount: %s' % (elem_tax.text, user.new_sub.tax))    