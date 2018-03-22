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

# 声明driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


# 获取放大镜 有content-dsc没有text，通过name获取attr
search_button = driver.find_element_by_id("com.android.settings:id/search")
print(search_button.get_attribute("name"))

# 设置title 有text没有content-dsc，通过name获取attr
setting_title = driver.find_element_by_xpath("//*[contains(@text,'设置')]")
print(setting_title.get_attribute("name"))

# 获取放大镜 有content-dsc没有text，通过text获取attr
print(search_button.get_attribute("text"))

# 设置title 有text没有content-dsc，通过text获取attr
print(setting_title.get_attribute("text"))

# 有class通过 className 获取
print(search_button.get_attribute("className"))

# 有resource-id通过 resourceId 获取
print(search_button.get_attribute("resourceId"))


