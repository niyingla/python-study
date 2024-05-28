
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, ActionChains
from SlideMatch import *
from selenium.webdriver.common.by import By
from lxml import etree
import requests
import time
import random
import os


class Test():
    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_argument('--disable-blink-features=AutomationControlled')
        self.driver = webdriver.Chrome(options=option)
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
        count = 30 + int(distance / 2)
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


    # 网易测试
    def wy_test(self):

        url = 'https://www.autoengine.com/'        # Chrome浏览器

        self.driver.get(url=url)
        self.driver.maximize_window()

        #js_button = 'q=document.body.scrollTop=500'

        # 执行js，滑动到最底部
        #self.driver.execute_script(js_button)
        #<div class="account-center-switch-button switch-switch false account">密码登录<span class="bar" style="background: rgb(13, 75, 255);"></span></div>
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//div[@class="account-center-switch-button switch-switch false account"]').click()
        time.sleep(1.3)
        #<input class="ace-input ace-ui-input-default" type="number" status="" fill-type="" name="mobile" autocomplete="mobile" vpattern="^1[23456789][0-9]{9}$" pattern="[0-9]*" fieldname="请输入手机号码" required="" placeholder="请输入手机号码" max="11" label="" title="请输入手机号码">
        self.driver.find_element(By.XPATH,'//input[@name="mobile"]').send_keys('18877686797')
        #<input class="ace-input ace-ui-input-default" type="password" status="" fill-type="" fieldname="请输入密码" required="" pattern="" max="20" name="password" autocomplete="password" label="" placeholder="请输入密码" title="请输入密码" style="padding-right: 16px;">
        self.driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('12345678')
        #<span class="check-box-icon"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 48 48"><defs><path id="check_svg__a" d="M0 0h48v48H0z"></path></defs><g fill-rule="evenodd"><mask id="check_svg__b" fill="#fff"><use xlink:href="#check_svg__a"></use></mask><use fill="#FFF" fill-opacity=".01" xlink:href="#check_svg__a"></use><path fill-rule="nonzero" d="M10.414 22.586a2 2 0 0 0-2.828 2.828l10 10a2 2 0 0 0 2.828 0l20-20a2 2 0 0 0-2.828-2.828L19 31.172l-8.586-8.586z"></path></g></svg></span>
        self.driver.find_element(By.XPATH,'//span[@class="check-box-icon"]').click()
        #<button class="ace-ui-btn account-center-action-button active ace-ui-btn-primary" title="" style="background: rgba(13, 75, 255, 0.4);" disabled="">登录</button>
        self.driver.find_element(By.XPATH,'//button').click()
        time.sleep(3)
        #<img class="captcha-verify-image" src="https://p9-catpcha.byteimg.com/tos-cn-i-188rlo5p4y/909f7a72421543298d45a2102c3c4e13~tplv-188rlo5p4y-2.jpeg" alt="basicImg" id="captcha_verify_image" crossorigin="anonymous">
        #<iframe src="https://rmc.bytedance.com/verifycenter/captcha/v2?from=iframe&amp;fp=verify_lwprv4sd_OozBuIBP_XLcx_4QBZ_9EOc_1CYR7gjD2xoJ&amp;env=%7B%22screen%22%3A%7B%22w%22%3A1920%2C%22h%22%3A1080%7D%2C%22browser%22%3A%7B%22w%22%3A1920%2C%22h%22%3A1032%7D%2C%22page%22%3A%7B%22w%22%3A1920%2C%22h%22%3A531%7D%2C%22document%22%3A%7B%22width%22%3A1920%7D%2C%22product_host%22%3A%22www.autoengine.com%22%2C%22vc_version%22%3A%221.0.0.60%22%2C%22maskTime%22%3A1716886079382%2C%22h5_check_version%22%3A%223.8.0%22%7D&amp;aid=301068&amp;app_name=acweb&amp;host=%2F%2Fverify.zijieapi.com&amp;lang=zh&amp;theme=%7B%22half_cn_OkBtnBgColor%22%3A%22%230D4BFF%22%7D&amp;verify_data=%7B%22code%22%3A%2210000%22%2C%22from%22%3A%22shark_admin%22%2C%22type%22%3A%22verify%22%2C%22version%22%3A%221%22%2C%22region%22%3A%22cn%22%2C%22subtype%22%3A%22slide%22%2C%22ui_type%22%3A%22%22%2C%22detail%22%3A%22z0lHtaO-q3P13YM8kj9ronIk1LPMj90EY*TD6HL6OZWRM2GjGNGq0ZLQXPEQTQ-SMSC9ojaF9t9mfDoqYhK7aRksdoc5jzKCV9IA*WtA3*NcgLJOHK08wWJkcrC-BjEuYNOqP*LOcJWcEyvbiztyyqNq7ruJVI3791jvDUxGGrJkLwp1WI19F12F3*0mMTAnn7XEqGQ63WSCzSKMSKomQ0vcFMldKQlO7357QILYInobfuK7A97DCEL*cslQLoVA-mQwALEa8eSAoEqAldqJyQ5UBw4ADAU-zDHRyWNPaT-dnb0lSKrFzLU-pNcdnsNblVbO8YyQQkLFSNWzJXnwGmCzb5Vyj2EzRH2ecthVixr1IvKOGXRvYpeAE0irEQF-kgxbPdk18Rn5Ms9z%22%2C%22verify_event%22%3A%22tt_user_pwd_login%22%2C%22fp%22%3A%22verify_lwprv4sd_OozBuIBP_XLcx_4QBZ_9EOc_1CYR7gjD2xoJ%22%2C%22server_sdk_env%22%3A%22%7B%5C%22idc%5C%22%3A%5C%22lf%5C%22%2C%5C%22region%5C%22%3A%5C%22CN%5C%22%2C%5C%22server_type%5C%22%3A%5C%22passport%5C%22%7D%22%2C%22log_id%22%3A%22202405281648008AD679FCA948D2D5263A%22%2C%22is_assist_mobile%22%3Afalse%2C%22is_complex_sms%22%3Afalse%2C%22identity_action%22%3A%22%22%2C%22identity_scene%22%3A%22%22%2C%22verify_scene%22%3A%22passport%22%2C%22login_status%22%3A0%2C%22aid%22%3A0%2C%22mfa_decision%22%3A%22%22%7D" style="border: none; display: block; visibility: visible; border-radius: 6px; overflow: hidden; position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%); width: 380px; height: 384px;"></iframe>
        self.driver.switch_to_frame(self.driver.find_element(By.XPATH,'//iframe'))
        html = self.driver.page_source
        html = etree.HTML(html)
        full_image_path_url = html.xpath('//img[@class="captcha-verify-image"]/@src')[0]
        slider_image_path_url = html.xpath('//img[@class="captcha-verify-image-slide"]/@src')[0]
        distence = get_distance(full_image_path_url, slider_image_path_url)
        print("滑动距离----",distence)

        #<div class="captcha-slider-btn" slot="dragger"><svg class="captcha-slider-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 22 20"><path fill="#B3B5B7" d="M21.7 10.2l-11.6 9c-.2.2-.5.1-.7-.1-.1-.1-.1-.2-.1-.3v-4.5c0-.3-.2-.5-.5-.5H.7c-.3 0-.5-.2-.5-.5V6.4c0-.3.2-.5.5-.5h8.1c.3 0 .5-.2.5-.5V.8c0-.3.2-.5.5-.5.1 0 .2 0 .3.1l11.6 9c.2.2.2.5 0 .8.1-.1 0 0 0 0z"></path></svg></div>
        source = self.driver.find_element(By.XPATH,'//div[@class="captcha-slider-btn"]')

        action = ActionChains(self.driver)

        action.click_and_hold(source)
        a = 0
        for x in self.generate_tracks(distence):
            action.move_by_offset(xoffset=x[0] - a, yoffset=x[1])
            a = x[0]
        action.release().perform()
        time.sleep(10)

        self.driver.quit()


if __name__ == '__main__':
    a = Test()
    a.wy_test()

    # coordinate_onnx = onnx_model_main("1.png")
    # drow_rectangle(coordinate_onnx, "1.png")


