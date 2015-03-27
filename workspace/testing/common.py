from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def setup_user(diff, num):
    #diff is a boolean value to tell whether this user info is for the different delivery address
    #print "diff: ", diff, "num:", num
    new_user = User(diff, num)
    return new_user

def hover(browser, element):
    hover = ActionChains(browser).move_to_element(element)
    hover.perform()
    
def switch_new_window(browser):
    for handle in browser.window_handles:
        pass
    
    browser.switch_to_window(handle)    

def switch_back(browser, parent_handle):
    browser.switch_to_window(parent_handle)
    
def implicit_wait_until(browser, time, path):
    try: 
        elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="m1"]/dl/dd/a[contains(.,"Subscriptions")]')))
    except TimeoutException:
        print "Timed out, can't find element"
    
    return elem
    
class User():
    def __init__(self, diff, num):
        self.comp_name = 'Cindy is testing' 
        self.first_name = ('Diff Malware' if diff else 'Malware')
        self.last_name = 'Bytes'
        self.addr1 = '10 Almaden Blvd'
        self.city = 'San Jose'
        self.state = 'California'
        self.zipcode = '95113'
        self.country = 'United States'
        self.email = 'hydra-test-' + str(num) + '@yopmail.com'         
            

##--------------------------------------
##    IGNORE ME
##--------------------------------------

    
# def waitForElem(self,_id):
#     for i in range(10):
#        if self.element_by_id_present(_id):
#          break
#        else:
#          print"---- not yet %s" % _id
#          time.sleep(5)  
#          
# def bkpoint(msg=""):
#     import code, sys
# 
#      use exception trick to pick up the current frame
#     try:
#         raise None
#     except:
#         frame = sys.exc_info()[2].tb_frame.f_back
# 
#      evaluate commands in current namespace
#     namespace = frame.f_globals.copy()
#     namespace.update(frame.f_locals)
#     code.interact(banner="-%s>>" % msg, local=namespace)

  #  print "switched to", browser.title
    
#         ids = browser.find_elements_by_xpath('//*[id="submit-hpm-button"]/div/div/*[@class]')
#         for i in ids:
#             print i.get_attribute("class")

#        To figure out string formatting
#       billing_addr = billing_addr.replace('\n', '\\n')
#       billing_addr = billing_addr.replace('\r', '\\r')      


        #print [i for i in xrange(len(billing_addr)) if billing_addr[i] != input_addr[i]]
        
        #for x, i in enumerate(billing_addr):
            #print "input: ", i, "output: ", input_addr[x]      