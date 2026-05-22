import requests
from bs4 import BeautifulSoup

# 1. 定义基础域名 (注意：只保留域名，不要带后面的路径和参数)
base_domain = "https://www.aigei.com"  # 修正点1：只保留域名
search_url = "https://www.aigei.com/s?q=%E4%BC%98%E7%BE%8E%E5%9B%BE%E5%BA%93"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
    "cookie":"gei_d_u=0d336d2fa8d74c91bf7ec29e813591cd; gei_d_1=d9e38d327d1093e8d7ebcb20ba7902ebd44bfc777b0e34e44ceda1ab4bf508d2359902a88c716a04f2add2ecddba4c0502eb01e84b7128c85eff3bbc8326cd72; hhhssi1ill1i=34d0a991afad770a2505701acc9abc57; oOO0OO0oOO00oo0o=true; SESSION=c108853d-82c5-4db1-b1e3-9c3cfdf149af; Hm_lvt_0e0ebfc9c3bdbfdcaa48ccbc43e864f9=1775621377; HMACCOUNT=D966E6B86F19EF04; OooOO000oOOO00o=5c399c6eb93e4b9288121bd2ecebffe8; wueiornjk234kj=df45a2b3e99e4b299b84891c93ed153b; Hm_lpvt_0e0ebfc9c3bdbfdcaa48ccbc43e864f9=1775623546; SERVERID=98d9647cdfadc76703e3b0e814607a21|1775623547|1775621371"
    # 修正点2：暂时移除Cookie，如果被拦截再考虑添加，通常爬虫不需要浏览器的完整Cookie
}

# 2. 获取搜索列表页
resp = requests.get(url=search_url, headers=headers)
resp.encoding = "utf-8"

main_page = BeautifulSoup(resp.text, "html.parser")

# 3. 寻找图片链接
# 根据网页结构，图片通常在 <img> 标签里，或者点击的 <a> 标签里。
# 你之前用 title="二次元女仆少女" 是对的，但我们需要找的是包含这个 title 的 <a> 标签
a_tag = main_page.find("a", attrs={"title": "二次元女仆少女"})

if a_tag:
    # 4. 拼接正确的详情页 URL
    # a_tag.get("href") 返回的是类似 "/item/xxx" 的相对路径
    detail_url = base_domain + a_tag.get("href") # 修正点3：使用 base_domain 拼接
    print(f"详情页地址: {detail_url}")
    
    # 5. 请求详情页 (其实这一步可以省略，因为我们直接找图片源地址)
    # 但是为了演示流程，我们继续
    resp_detail = requests.get(url=detail_url, headers=headers)
    resp_detail.encoding = "utf-8"
    
    detail_page = BeautifulSoup(resp_detail.text, "html.parser")
    
    # 6. 在详情页中找到高清图片的 URL
    # 根据网页 HTML 分析，图片通常在 class="big-img" 或者直接是 <img> 标签
    # 这里我们尝试找常见的 img 标签
    img_tag = detail_page.find("img", attrs={"class": "big-img"}) # 尝试找大图类
    
    # 如果找不到特定 class，尝试找所有非透明占位图的 img
    if not img_tag:
        # 简单粗暴：找所有宽度较大的图片，或者排除 gif 图片（通常是小图标）
        all_imgs = detail_page.find_all("img")
        for img in all_imgs:
            src = img.get("src")
            # 简单过滤：排除 data:image 开头的内联图和 gif 格式的图标
            if src and "data:image" not in src and src.endswith(".jpg") or src.endswith(".png"):
                img_url = src
                # 如果是相对协议，补全
                if img_url.startswith("//"):
                    img_url = "https:" + img_url
                break
    else:
        img_url = img_tag.get("src")
    
    # 手动补全协议
    if img_url.startswith("//"):
        img_url = "https:" + img_url
    
    print(f"图片直链: {img_url}")

    # 7. 下载图片
    # 注意：headers 中可能需要 referer 才能下载
    headers["Referer"] = detail_url 
    img_data = requests.get(img_url, headers=headers).content
    
    # 保存
    with open("二次元女仆少女.jpg", "wb") as f:
        f.write(img_data)
    print("✅ 图片下载完成！")

else:
    print("❌ 未找到指定标题的链接，请检查网页结构是否变化或标题是否完全匹配。")
