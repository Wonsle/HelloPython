"""
Day 23: 解析網頁數據
  * 使用 `BeautifulSoup` 抓取特定標籤 (如新聞標題)。
"""


import requests
from bs4 import BeautifulSoup

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
        # 建立 BeautifulSoup 物件
        soup = BeautifulSoup(html_content, 'html.parser')
        # 尋找搜尋按鈕資訊
        search_button = soup.find('input', attrs={'name': 'btnK'})
        if search_button:
            button_label = search_button.get('value')
            print(f"搜尋按鈕名稱: {button_label}")
        print(html_content[:500])  # 顯示前500個字元
    else:
        print("無法抓取網頁內容。")
