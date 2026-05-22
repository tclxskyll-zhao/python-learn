
from selenium import webdriver
from time import sleep

#无可视化界面
from selenium.webdriver.chrome.options import Options
#规避检测
from selenium.webdriver import ChromeOptions

#实现无可视化操作
chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')


# 基本防检测设置
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

bro=webdriver.Chrome(options=chrome_options)
bro.get("https://www.taobao.com")
print(bro.page_source)
sleep(5)
bro.quit()