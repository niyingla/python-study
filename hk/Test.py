
from selenium import webdriver
from selenium.webdriver import ActionChains
from SlideMatch import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from lxml import etree
import time
import random
import json


class Test():
    def __init__(self):
        option = webdriver.ChromeOptions()
        # 无头模式
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 它被用于标记一个浏览器是否被自动化工具（如 Selenium）控制。如果这个特性被启用，网站可以检测到这个浏览器实例是被自动化工具控制的。
        option.add_argument('--disable-blink-features=AutomationControlled')
        option.binary_location = r'D:\workTool\Application\chrome.exe'
        caps = DesiredCapabilities.CHROME
        caps['goog:loggingPrefs'] = {'performance': 'ALL'}
        self.driver = webdriver.Chrome(executable_path=r'D:/workTool/Application/chromedriver.exe',desired_capabilities=caps, options=option)
        self.driver.implicitly_wait(10)

    def __ease_out_expo(self, sep):
        if sep == 1:
            return 1
        else:
            return 1 - pow(2, -10 * sep)

    def generate_tracks(self, distance):
        """
        根据滑动距离生成滑动轨迹
        :param distance: 需要滑动的距离
        :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
            x: 已滑动的横向距离
            y: 已滑动的纵向距离, 除起点外, 均为0
            t: 滑动过程消耗的时间, 单位: 毫秒
        """

        if not isinstance(distance, int) or distance < 0:
            raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
        # 初始化轨迹列表
        slide_track = [
            [random.randint(-50, -10), random.randint(-50, -10), 0],
            [0, 0, 0],
        ]
        # 共记录count次滑块位置信息
        count = 5 #0 + int(distance / 2)
        # 初始化滑动时间
        t = random.randint(50, 100)
        # 记录上一次滑动的距离
        _x = 0
        _y = 0
        for i in range(count):
            # 已滑动的横向距离
            x = round(self.__ease_out_expo(i / count) * distance)
            # 滑动过程消耗的时间
            t += random.randint(10, 20)
            if x == _x:
                continue
            slide_track.append([x, _y, t])
            _x = x
        slide_track.append(slide_track[-1])
        return slide_track



    def auto_engine_test(self):
        url = 'https://www.autoengine.com/'        # Chrome浏览器
        self.driver.get(url=url)
        self.driver.maximize_window()
        time.sleep(1)
        # 点击账号密码登录
        self.driver.find_element(By.XPATH,'//div[@class="account-center-switch-button switch-switch false account"]').click()
        time.sleep(1.3)
        # 输入账号密码
        self.driver.find_element(By.XPATH,'//input[@name="mobile"]').send_keys('17656309270')
        # 输入密码
        self.driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('Xchl2526666.')
        # 选中客户协议
        self.driver.find_element(By.XPATH,'//span[@class="check-box-icon"]').click()
        # 点击登录
        self.driver.find_element(By.XPATH,'//button').click()
        time.sleep(3)
        # 获取滑动弹框
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'//iframe'))
        html = self.driver.page_source
        html = etree.HTML(html)
        # 获取背景图和滑块图
        full_image_path_url = html.xpath('//img[@class="captcha-verify-image"]/@src')[0]
        slider_image_path_url = html.xpath('//img[@class="captcha-verify-image-slide"]/@src')[0]
        # 获取滑动距离
        distance = get_distance(full_image_path_url, slider_image_path_url)

        # 滑动按钮获取
        slider_btn = self.driver.find_element(By.XPATH, '//div[@class="captcha-slider-btn"]')
        # 滑动
        self.move_to_distance(distance, slider_btn)
        time.sleep(5)
        #切换当前网址
        self.driver.get('https://www.autoengine.com/jdc/industry/live/screen?isHideSiderMemu=1&isHideHeader=1&room_id=7478603243621337892')
        #睡两秒
        time.sleep(5)
        url_response = self.get_response_url('https://www.autoengine.com/motor/dealer/jdc_saas/live/data/screen?__method=window.fetch')
        print(url_response)
        #dealer/jdc_saas/live/data/screen
        # 退出
        self.driver.quit()

    def move_to_distance(self, distance, slider_btn):
        action = ActionChains(self.driver)
        # 按住滑块
        action.click_and_hold(slider_btn)
        a = 0
        for x in self.generate_tracks(distance):
            # 分次移动滑块
            action.move_by_offset(xoffset=x[0] - a, yoffset=x[1])
            a = x[0]
        # 执行动作
        action.release().perform()

    @staticmethod
    def process_browser_log_entry(entry):
        response = json.loads(entry['message'])['message']
        return response

    def get_response_url(self, url):
        result = []
        # 获取浏览器日志
        browser_log = self.driver.get_log('performance')
        # 获取所有的message 部分
        events = [Test.process_browser_log_entry(entry) for entry in browser_log]
        # 过滤出Network.responseReceived的事件
        events = [event for event in events if 'Network.responseReceived' in event['method']]
        for event in events:
            # 找到包含response的event['params']
            if 'response' in event['params'] and 'url' in event['params']['response']:
                #包含指定路径的请求地址
                if url in event['params']['response']['url']:
                    #
                    request_id = event['params']['requestId']
                    response_body = self.driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': request_id})
                    body = response_body["body"]
                    result.append(body)

        return result

if __name__ == '__main__':
    a = Test()
    a.auto_engine_test()


