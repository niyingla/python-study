from selenium import webdriver

# 启动浏览器并打开一个网页
driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.example.com")

# 打开一个新的窗口
driver.execute_script("window.open('https://www.google.com');")

# 获取所有窗口的句柄
window_handles = driver.window_handles

# 切换到第二个窗口
driver.switch_to.window(window_handles[1])

# 在第二个窗口中进行操作
# ...

# 切换回第一个窗口
driver.switch_to.window(window_handles[0])

# 在第一个窗口中进行操作
# ...

# 关闭浏览器
driver.quit()