import json
import time
import Test
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import DesiredCapabilities, ActionChains


caps = DesiredCapabilities.CHROME
webdriver = webdriver.Chrome("./chromedriver")
webdriver.get("https://www.baidu.com/")
webdriver.maximize_window()

ActionChains(webdriver).move_to_element(webdriver.find_element(By.LINK_TEXT, "更多")).perform()
time.sleep(1)


#<a class="img-spacing" href="http://fanyi.baidu.com/" target="_blank" name="tj_fanyi"><img src="https://dss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/topnav/newfanyi-da0cea8f7e.png"><div class="s-top-more-title c-font-normal c-color-t">翻译</div></a>
# webdriver.find_element(By.LINK_TEXT, "翻译").click()
#换一种方式获取元素 点击
webdriver.find_element(By.CSS_SELECTOR, "a[name='tj_fanyi']").click()

time.sleep(1)
#<div class="iZoMFioL"><span class="f9WVaz_4"></span></div>
#鼠标移动到当前div
ActionChains(webdriver).move_to_element(webdriver.find_element(By.CSS_SELECTOR, "div.iZoMFioL")).perform()
time.sleep(1)
#点击鼠标左键
ActionChains(webdriver).click().perform()
#点击当前div
# webdriver.find_element(By.CSS_SELECTOR, "div.iZoMFioL").click()
#跳转到上一个页面
#webdriver.back()
#跳转到下一个页面
#关闭当前页面
webdriver.close()
#关闭上个页面

time.sleep(50)

webdriver.quit()


