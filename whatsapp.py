from selenium import webdriver
import time
import pyautogui
from selenium.webdriver.common.keys import Keys

def doit(trigger):
    contact = "name"  # contact name to send message
    name = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    name.send_keys(contact)
    time.sleep(2)
    pyautogui.click(165, 450)
    if(trigger is not None):
        time.sleep(trigger)
    message = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')

    for _ in range(0, 5): # count of messages to send
        message.send_keys("Testing Automation...This is computer generated text")     # custom message to send
        message.send_keys(Keys.RETURN)

path="user-data-dir=C:\\Users\\User1\\AppData\\Local\\Google\\Chrome\\User Data\\Whatsapp"      #path where session info you want to store
options=webdriver.ChromeOptions()
options.add_argument(path)

driver = webdriver.Chrome("C://Webdriver//chromedriver.exe",options=options)  # path where chromedriver.exe is installed
driver.maximize_window()

driver.get("https://web.whatsapp.com/")
time.sleep(8)
try:
    doit()

    '''XML path used for navigation through the HTML structure of the page
    XPath can be used for both HTML and XML documents to find the location of any element on a webpage using HTML DOM structure'''
except:
    doit(2)


driver.close()
exit(1)


