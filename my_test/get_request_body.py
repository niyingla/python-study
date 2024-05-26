import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



import json

def process_browser_log_entry(entry):
    response = json.loads(entry['message'])['message']
    return response

def  get_response_url(driver, url):
    result = []
    # 获取浏览器日志
    browser_log = driver.get_log('performance')
    # 获取所有的message 部分
    events = [process_browser_log_entry(entry) for entry in browser_log]
    # 过滤出Network.responseReceived的事件
    events = [event for event in events if 'Network.responseReceived' in event['method']]
    for event in events:
        # 找到包含response的event['params']
        if 'response' in event['params'] and 'url' in event['params']['response']:
            #包含指定路径的请求地址
            if url in event['params']['response']['url']:
                #
                request_id = event['params']['requestId']
                response_body = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': request_id})
                body = response_body["body"]
                result.append(body)

    return result

caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}  # 开启performance日志
options = webdriver.ChromeOptions()
driver = webdriver.Chrome("./chromedriver", desired_capabilities=caps, options=options)
driver.implicitly_wait(10)
driver.get("https://www.dangdang.com/")
driver.maximize_window()

element = driver.find_element(By.ID, "key_S")
time.sleep(1)
element.send_keys("理想国")

element1 = driver.find_element(By.CSS_SELECTOR, ".search .button")
time.sleep(1)

element1.click()
result = get_response_url(driver, 'https://search.dangdang.com/Standard/Search/Extend/hosts/api/get_json.php')
print(result)
driver.quit()