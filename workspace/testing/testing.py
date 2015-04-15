import common, zuora_common
import time

def testing_data(self, browser, num):
    
    new_user = common.User(False, num)
    diff_user = common.User(True, '1')
    
    new_user.new_sub.total = "$299.50"
    new_user.new_sub.tax = "$0.01"    
    
    zuora_common.login(browser)
    time.sleep(3)
    browser.get('https://apisandbox.zuora.com/apps/CustomerAccount.do?method=view&id=2c92c0fb4c75067f014c8178e79d716d')
    zuora_common.check_zuora_Invoice(self, browser, new_user)   