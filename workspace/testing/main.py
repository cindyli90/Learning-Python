import unittest
import mwbtest_portal_checks
import mwbtest_self_serve_purchase_MBAM
import prod_self_serve_purchase_MBAM

#https://gist.github.com/dariodiaz/3104601
# def highlight(element):
#     """Highlights (blinks) a Selenium Webdriver element"""
#     driver = element._parent
#     def apply_style(s):
#         driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
#                               element, s)
#     original_style = element.get_attribute('style')
#     apply_style("background: yellow; border: 2px solid red;")
#     time.sleep(.3)
#     apply_style(original_style)
    
if __name__ == '__main__':

    sighTestSuite = unittest.TestSuite()
    sighTestSuite.addTest(mwbtest_self_serve_purchase_MBAM.MwbtestSelfServePurchaseMBAM('test_mwbtest_self_serve_purchase_MBAM'))
    
    #suite = unittest.TestLoader().loadTestsFromTestCase(mwbtest_self_serve_purchase_MBAM.MwbtestSelfServePurchaseMBAM)
    unittest.TextTestRunner().run(sighTestSuite)
    