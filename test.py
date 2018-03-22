import time
from appium import webdriver



# server 启动参数
desired_caps = {}
# 设备信息
# 平台名字
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
# 这个是可以随便写的
desired_caps['deviceName'] = '192.168.56.101:5555'
# app信息
desired_caps['appPackage'] = 'com.android.settings'
# 启动页面
desired_caps['appActivity'] = '.Settings'
#执行这个
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)




# time.sleep(2)

# driver.quit()