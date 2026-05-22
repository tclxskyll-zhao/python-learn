import requests
from bs4 import BeautifulSoup
import time
import random

# 安全提示：在实际项目中，建议将 Cookie 放在环境变量或配置文件中，不要硬编码在代码里提交到 Git
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36', # 调整为较稳定的版本
    'Cookie': 'bid=R_gu8ixI1A8; ll="118371"; __utma=30149280.816520309.1724738905.1770536236.1774331977.5; __utmc=30149280; __utmz=30149280.1774331977.5.2.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; __utmt_douban=1; __utma=223695111.134321609.1774332182.1774332182.1774332182.1; __utmb=223695111.0.10.1774332182; __utmc=223695111; __utmz=223695111.1774332182.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1774332182%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=3868e523b8dd8ccb.1774332182.; _pk_ses.100001.4cf6=1; ap_v=0,6.0; _vwo_uuid_v2=DF2EB41F597BA7E2F4B580B7296FC4A17|7ca35e9b5aaf865872eeadfb96e850f8; dbcl2="268216418:C4S95jCm1vQ"; ck=PfGb; push_noty_num=0; push_doumail_num=0; frodotk_db="2001ee5be70c17266005cb13b5244572"; __yadk_uid=Brn0dAmP9HVxLTH9DqzOOksWx27oiO5R; __utmv=30149280.26821; __utmb=30149280.20.9.1774332253327'
}

def get_movie_page(start):
    url = f'https://movie.douban.com/top250?start={start}&filter='
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        # 检查状态码
        if response.status_code != 200:
            print(f"请求失败，状态码: {response.status_code}")
            return None
            
        # 简单的反爬检测：如果返回内容太短或包含验证字样
        if len(response.text) < 2000 or "验证" in response.text:
            print("警告：可能触发了反爬验证，请检查 Cookie 是否过期。")
            return None
            
        return response.text
        
    except Exception as e:
        print(f"发生网络错误: {e}")
        return None

def parse_movies(html_content):
    if not html_content:
        return []
    
    soup = BeautifulSoup(html_content, 'html.parser')
    movie_list = soup.find('ol', class_='grid_view')
    
    if not movie_list:
        print("未找到电影列表，页面结构可能已变更。")
        return []

    movies = []
    for item in movie_list.find_all('li'):
        try:
            # 提取标题 (有些电影有副标题，在 span[class='title'][1] 中)
            title_tag = item.find('div', class_='hd').find('span', class_='title')
            title = title_tag.string.strip() if title_tag else "未知标题"
            
            # 提取评分
            rating_tag = item.find('span', class_='rating_num')
            rating = rating_tag.string.strip() if rating_tag else "N/A"
            
            # 提取评价人数
            stars_div = item.find('div', class_='star')
            comments = "0人评价"
            if stars_div:
                # 评价人数通常在最后一个 span 标签里
                spans = stars_div.find_all('span')
                if len(spans) >= 4:
                    comments = spans[3].string.strip()
            
            movies.append({
                'title': title,
                'rating': rating,
                'comments': comments
            })
        except Exception as e:
            continue
            
    return movies

if __name__ == '__main__':
    # 示例：抓取第 2 页 (start=25)
    start_offset = 0
    print(f"正在抓取第 {start_offset // 25 + 1} 页数据...")
    
    html = get_movie_page(start_offset)
    
    if html:
        data = parse_movies(html)
        print("-" * 30)
        for idx, movie in enumerate(data, 1):
            print(f"{idx}. 《{movie['title']}》 | 评分: {movie['rating']} | {movie['comments']}")
        print("-" * 30)
        print(f"共抓取到 {len(data)} 部电影。")
    else:
        print("抓取失败，未能获取有效数据。")

    # 礼貌延时
    time.sleep(random.uniform(1, 2))