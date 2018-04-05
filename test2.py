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
aa = driver.find_element_by_xpath("//*[contains(@text,'更多')]")
bb = driver.find_element_by_xpath("//*[contains(@text,'电池')]")

arr1 = driver.find_elements_by_xpath("//*[contains(@class,'android.widget.FrameLayout')]")

for i in arr1:
    driver.drag_and_drop(bb, i)
    try:
        driver.find_element_by_xpath("//*[contains(@text,'关于手机')]").click()
        arr = driver.find_elements_by_xpath("//*[contains(@text,'5.1')]")

        for i in arr:
            if i.text == "5.1":
                print("有")
                break
        break
    except Exception as e:
        continue
#         try:
#             temp = driver.find_element_by_class_name("android.widget.ImageButton")
#             return temp
#         except NoSuchElementException as e:
#             continue
#             # return temp
#
#     raise Exception('没有找到！！！！')
# 方法二

# 方法一
# driver.scroll(bb, aa)
# time.sleep(1)
# 关于手机
# cc = driver.find_element_by_xpath("//*[contains(@text,'关于手机')]")
# cc.click()
# 5.1
# dd = driver.find_element_by_xpath("//*[contains(@text,'5.1')]")
# arr = driver.find_elements_by_xpath("//*[contains(@text,'5.1')]")
#
# for i in arr:
#     if i.text=="5.1":
#         print("有")





# ee = dd.text
# print(ee)
# if ee == 5.1:
#     print("是有5.1")
# else:
#     print("没有5.1")
