#使用 Selenium 完成对于淘宝的操作
from selenium import webdriver
#导入 动作链 动作
from selenium.webdriver import ActionChains
from time  import sleep

from selenium.webdriver.common import action_chains

bro=webdriver.Chrome()
bro.get("https://www.taobao.com/")

# #标签定位
# search_input=bro.find_element("id","q")
# search_input.send_keys("mac")
#
# #点击搜索按钮
# button=bro.find_element("class name","btn-search")
# button.click()
#
# #执行一组js命令  对搜索页面进行下拉
# bro.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# sleep(2)
#
#
# sleep(5)
# bro.quit()


#如果定位的元素在 iframe 中
#必须先要使用 switch_to_frame(id) 切换标签
div="#标签"
act=ActionChains(bro)
act.click_and_hold(div) #长按点击并保持
act.move_by_offset(17,0) #移动像素
act.perform() #让动作链立即执行
act.release() #释放动作链