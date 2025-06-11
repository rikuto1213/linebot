import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# Webドライバーを起動
driver = webdriver.Chrome()

# Webページにアクセスする関数を定義
def get_page(url):
    driver.get(url)
    return driver.page_source

# 画像をダウンロードする関数を定義
def download_image(image_url, save_path):
    response = requests.get(image_url)
    with open(save_path, 'wb') as f:
        f.write(response.content)

# 画像スクレイピングのメイン関数
def image_scraping(url, save_folder):
    # WebページにアクセスしてHTMLデータを取得
    html = get_page(url)
    
    # BeautifulSoupを使ってHTMLを解析
    soup = BeautifulSoup(html, 'html.parser')
    
    # imgタグを取得
    img_tags = soup.find_all('img')
    
    # 画像のURLを取得して保存
    for img_tag in img_tags:
        image_url = img_tag['src']
        if image_url.startswith('http'):
            # 画像のURLがフルパスである場合のみダウンロード
            image_name = image_url.split('/')[-1]
            save_path = os.path.join(save_folder, image_name)
            download_image(image_url, save_path)

# 画像スクレイピングを実行する
if __name__ == "__main__":
    target_url = 'https://west2-univ.jp/sp/index.php?t=650311'  # スクレイピング対象のURLを指定
    save_folder = 'images'  # 画像を保存するフォルダを指定
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    image_scraping(target_url, save_folder)

# Webドライバーを終了
driver.quit()