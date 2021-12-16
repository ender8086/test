import time
from selenium import webdriver

webbrowser = webdriver.Chrome()
webbrowser.get("WEBSITE")
element = webbrowser.find_element_by_id("ID_USERNAME")
element.send_keys("USERNAME")
element = webbrowser.find_element_by_id("ID_PASSWORD")
element.send_keys("PASSWORD")
element = webbrowser.find_element_by_xpath('ENTER/SIGN IN BUTTON').click()
time.sleep(10)
webbrowser.get("ACCESS ANOTHER PAGE INSIDE THE WEBSITE")
#it could be some dashboard
try:
    text = webbrowser.find_element_by_name("some element").text
    print(text)
    except:
    #still trying to figure out the correct way of handling specific selenium exceptions
    print ("Unable to locate element")





