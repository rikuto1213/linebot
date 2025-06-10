from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://west2-univ.jp/sp/menu.php?t=650311")#立命の食堂のURLでおけ

images = driver.find_elements(By.TAG_NAME, "img")

#print(f"find{len(images)}pictures.")画像タグ

