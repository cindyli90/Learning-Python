from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

import time
import info

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

def bkpoint(msg=""):
    import code, sys

    # use exception trick to pick up the current frame
    try:
        raise None
    except:
        frame = sys.exc_info()[2].tb_frame.f_back

    #evaluate commands in current namespace
    namespace = frame.f_globals.copy()
    namespace.update(frame.f_locals)
    code.interact(banner="-%s>>" % msg, local=namespace)
    
def explicit_wait_until(browser, time, path):
    try: 
        elem = WebDriverWait(browser, time).until(EC.presence_of_element_located((By.XPATH, path)))
    except TimeoutException:
        raise NoSuchElementException ("Timed out, can't find element at %s" % path)
    
    return elem
    
def refresh_and_find_element(browser, xpath, sec):    
    # Refreshes the page and check if an element exists
    
    # number of seconds between checks
    interval = 5
    
    # While there is still time left to check
    while sec:
        print "refreshing..."
        browser.refresh()
        
        try:
            elem = browser.find_element_by_xpath(xpath)
        except NoSuchElementException:
            print "not found yet"
            sec -= interval
        else:
            print "%s found!" % (elem.text)
            return elem
            
        time.sleep(interval)
        
    #if exit loop without finding element, means element not found
    raise NoSuchElementException

def verify_end(self):
    #checks if verify is empty, if not empty, asserts and shows verification errors
    
    assert not self.verify, \
        "One or more verifies failed, see above:" 
     
  

    
    # def refresh_and_check_text(browser, xpath, text):    
    # # Refreshes the page and check for an element

    # sec_to_check = 60 # last time we had an issue with Zuora updating, it took about 8 minutes to refresh
    
    # rounds = 1
    # # While there is still time left to check
    # while sec_to_check:
    
        # #check list of elements, have to re-lookup every time because elements get stale
        # elem_list = browser.find_elements_by_xpath(xpath)

        # print "Round %d\n" % (rounds)
        # rounds += 1
        
        # #search list for text, return if found
        # for elem in elem_list: 
            # if elem.text == text:
                # print "%s found!" % (elem.text)
                # return elem
            # else:
                # print "%s, didn't match" % (elem.text)
                
        # #time.sleep(60)
        # sec_to_check -= 60
        
        # browser.refresh()
        
    # raise NoSuchElementException
    
    
    
class User():
    def __init__(self, diff, num):
     
        self.comp_name = 'Cindy is Testing' 
        self.first_name = ('Diff Malware' if diff else 'Malware')
        self.last_name = 'Bytes'
        self.addr1 = '10 Almaden Blvd'
        self.city = 'San Jose'
        self.state = 'California'
        self.zipcode = '95113'
        self.country = 'United States'
        self.email = 'hydra-test-' + str(num) + '@yopmail.com'         
        
        # instantiate a new sub
        self.new_sub = Subscription()
        self.new_CC = info.CCInfo()
        
class Subscription():
    def __init__(self):
        self.product_qty_unitPrice = [] #list of tuples (product, qty, unit price)
        self.tax = ''
        self.total = ''
    
    def print_sub(self):
        for x,y,z in self.product_qty_unitPrice:
            print "prod: %s \tqty: %s \tunit price: %s" % (x, y, z)
        print "tax:\t%s" % self.tax
        print "total:\t %s" % self.total
        
        
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