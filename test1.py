# utf-8
import time
from appium import webdriver

# server 启动参数

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
# 输入框输入中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

aa = driver.find_element_by_xpath("//*[contains(@resource-id,'com.android.settings:id/search')]")
aa.click()
bb = driver.find_element_by_xpath("//*[contains(@text,'搜索…')]")
bb.send_keys("s")
arr = driver.find_elements_by_id("com.android.settings:id/title")
for i in arr:
    print(i.text)
print(len(arr))
# aa.send_keys("无线")
#