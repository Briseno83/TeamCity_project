import selenium
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(r"C:\Users\ivanb\Documents\Matrix\Term3\Scripting\Test_Case\Drivers\chromedriver.exe")


def loginTest (a, b):
    # create webdriver object
    #driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(r"C:\Users\ivanb\Documents\Matrix\Term3\Scripting\Test_Case\Drivers\chromedriver.exe")
    driver.get("https://demo.guru99.com/V4/")
    driver.find_element("name","uid").send_keys(a)
    driver.find_element("name","password").send_keys(b)
    driver.find_element("name","btnLogin").send_keys(Keys.ENTER)
    try:
        driver.maximize_window()
        time.sleep(8)
        print("pass")
    except:
        print("fail")
        driver.quit()


    driver.quit()

loginTest("mngr439902","yhUzatu")
loginTest("mngr439902"," ere")
loginTest("mngr43","u")

driver = webdriver.Chrome(r"C:\Users\ivanb\Documents\Matrix\Term3\Scripting\Test_Case\Drivers\chromedriver.exe")
driver.get("https://demo.guru99.com/V4/")
driver.find_element("name","uid").send_keys("mngr439902")
driver.find_element("name","password").send_keys("yhUzatu")
driver.find_element("name","btnLogin").send_keys(Keys.ENTER)


driver.find_element(By.LINK_TEXT,"Edit Customer").click()
#driver.execute_script("document.getElementById('gpt_unit_/24132379/INTERSTITIAL_DemoGuru99_0').style.display='none'")
driver.find_element(By.LINK_TEXT,"Edit Customer").click()
driver.maximize_window()
driver.find_element("name","cusid").send_keys("51500")
driver.find_element("name","AccSubmit").send_keys(Keys.ENTER)
time.sleep(15)
driver.quit()

driver = webdriver.Chrome(r"C:\Users\ivanb\Documents\Matrix\Term3\Scripting\Test_Case\Drivers\chromedriver.exe")
driver.get("https://demo.guru99.com/V4/")
driver.find_element("name","uid").send_keys("mngr439902")
driver.find_element("name","password").send_keys("yhUzatu")
driver.find_element("name","btnLogin").send_keys(Keys.ENTER)


driver.find_element(By.LINK_TEXT,"Edit Customer").click()
#driver.execute_script("document.getElementById('gpt_unit_/24132379/INTERSTITIAL_DemoGuru99_0').style.display='none'")
driver.find_element(By.LINK_TEXT,"Edit Customer").click()
driver.maximize_window()
driver.find_element("name","cusid").send_keys("51584")
driver.find_element("name","AccSubmit").send_keys(Keys.ENTER)
driver.find_element("name","sub").send_keys(Keys.ENTER)
time.sleep(15)
driver.quit()

driver = webdriver.Chrome(r"C:\Users\ivanb\Documents\Matrix\Term3\Scripting\Test_Case\Drivers\chromedriver.exe")
driver.get("https://demo.guru99.com/V4/")
driver.find_element("name","uid").send_keys("mngr439902")
driver.find_element("name","password").send_keys("yhUzatu")
driver.find_element("name","btnLogin").send_keys(Keys.ENTER)


driver.find_element(By.LINK_TEXT,"Edit Customer").click()
#driver.execute_script("document.getElementById('gpt_unit_/24132379/INTERSTITIAL_DemoGuru99_0').style.display='none'")
driver.find_element(By.LINK_TEXT,"Edit Customer").click()
driver.maximize_window()
driver.find_element("name","cusid").send_keys("51584")
driver.find_element("name","AccSubmit").send_keys(Keys.ENTER)
driver.find_element("name","addr").send_keys("1077 rue woodside Montreal")
driver.find_element("name","city").send_keys("Montreal")
driver.find_element("name","state").send_keys("Quebec")
driver.find_element("name","pinno").send_keys("23456")
driver.find_element("name","telephoneno").send_keys("5143339999")
driver.find_element("name","emailid").send_keys("kuhhhy@gmail.com")
driver.find_element("name","password").send_keys("67854")
driver.find_element("name","sub").send_keys(Keys.ENTER)
time.sleep(15)
driver.quit()