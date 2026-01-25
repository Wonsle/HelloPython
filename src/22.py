"""
Day 22: 網路爬蟲基礎 (Web Scraping)**
  * 使用 `requests` 抓取網頁 HTML。
"""

import requests

def fetch_webpage(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

if __name__ == "__main__":
    url = "https://www.google.com"
    html_content = fetch_webpage(url)
    if html_content:
        print("網頁內容抓取成功！")
        print(html_content[:500])  # 顯示前500個字元
    else:
        print("無法抓取網頁內容。")
