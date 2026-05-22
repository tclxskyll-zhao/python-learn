from pyquery import PyQuery
# 有关 PyQuery 库学习-类似前端的 JQuery 使用 css选择器进行选择
# html = """
#     <ul>
#         <li class="aaa"><a href="http://www.goole.com">谷歌</a></li>
#         <li class="aaa"><a href="http://www.baidu.com">百度</a></li>
#         <li class="bbb" id="qq"><a href="http://www.qq.com">腾讯</a></li>
#         <li class="bbb"><a href="http://www.444.com">4</a></li>
#     </ul>
# """
#
# # p=PyQuery(html)
# # print(type(p))  # 这里的p的类型并不是字符串类型
#
# # a=p("a") #这里可以得到包括 a标签的所有内容
# # print(a)
#
# #链式操作
# # a=p("li")("a")
# # a=p("li a")
# # print(a)
#
# # a=p(".aaa a") #筛选的class为 aaa 且包含a标签的部分
# # print(a)
#
# # href=p("#qq a").attr("href") # #id id选择器qq，挑选 atter标签中的属性
# # text=p("#qq a").text() #筛选对应标签中的文本
# # print(href,text)
#
# # 注意 这里的 p("li a").attr("href") 只会匹配出第一个符合条件的结果
# # href=p("li a").attr("href")
# # print(href)
#
# #想要匹配所有的符合条件的结果
# # its=p("li a").items()
# # for item in its:
# #     herf=item.attr("href")
# #     text=item.text()
# #     print(herf,text)
#
# #

# div="""
# <div><span>我爱你</span></div>
# """
#
# p=PyQuery(div)
# html=p("div").html()
# text=p("div").text()
# print(html)  #全都要
# print(text)  #去除所有 html 标签只要文本内容


html="""
<HTML>
<div class="aaa">哒哒哒</div>
<div class="bbb">嘟嘟嘟</div> 
</HTML>
"""

p=PyQuery(html)
# p("div.aaa").after("""<div class="ccc">哈哈哈</div>""")
# p("div.aaa").append("""<span>周杰伦</span>""")
# p("div.aaa").attr("class","ccc")
# p("div.bbb").attr("id","1234")
p("div.bbb").remove() #删除标签
print(p)








