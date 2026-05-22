from unittest import result

import requests
from lxml import etree

xml="""
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周大强</nick>
        <nick id="10010">周芷若</nick>
        <nick class="jay">周杰伦</nick>
        <nick class="jolin">蔡依林</nick>
        <div>
            <nick>惹了</nick>
        </div>
    </author>
    <partner>
        <nick id="ppc">胖胖陈</nick>
        <nick id="ppbc">胖胖不陈</nick>
    </partner>
</book>
"""
#针对 xml 语言进行解析
et=etree.XML(xml)

#result=et.xpath("/book") #提取整个 book 标签的对象
# result=et.xpath("/book/author/nick") #表示的是寻找标签的子标签
# result=et.xpath("/book/author/nick/text()")[0] #提text（）取标签中的文本信息
# result=et.xpath("/book//nick") #寻找 book标签的子孙后代的 nick标签
# result=et.xpath("/book/*/nick/text()") # * 通配符 可以匹配所有的标签
# result=et.xpath("/book/author/nick[@class='jay']/text()") #[] 表示属性筛选 @属性名=值 find("Nick":attrs={"属性值”：“jay”})
#result=et.xpath("/book/author/nick/@id")  #这里最后一个/后面的 @属性值 可以直接拿到属性的 值
#print(result)


