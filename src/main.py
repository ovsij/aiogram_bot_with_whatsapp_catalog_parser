from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys

try:
    if sys.argv[1]:
        with open(sys.argv[1], 'r', encoding='utf8') as f:
            groups = [group.strip() for group in f.readlines()]
except IndexError:
    print('Please provide the group name as the first argument.')

with open('msg.txt', 'r', encoding='utf8') as f:
    msg = f.read()

options = webdriver.ChromeOptions()
options.add_argument('--allow-profiles-outside-user-dir')
options.add_argument('--enable-profile-shortcut-manager')
options.add_argument(r'user-data-dir=.\User')
options.add_argument('--profile-directory=Profile 1')
options.headless = True

browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

browser.maximize_window()

try:
    browser.get('https://web.whatsapp.com/catalog/393427688947')
    print('start')
    print(browser)
    for i in range(1, 100):
        try:
            item_xpath = f'//*[@id="app"]/div/div/div[6]/span/div/span/div/div[2]/div[2]/div/div/div/div[{i}]/div/div/div[2]/div[1]/div/span'
            item = WebDriverWait(browser, 500).until(
                EC.presence_of_element_located((By.XPATH, item_xpath))
            )
            item.click()
            #'//*[@id="app"]/div/div/div[6]/span/div/span/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[2]/div[1]/div/span'
            #'//*[@id="app"]/div/div/div[6]/span/div/span/div/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div/span'
            title_xpath = '//*[@id="app"]/div/div/div[6]/span/div/span/div/div[2]/div/div[3]/div[1]/span'
            title = WebDriverWait(browser, 500).until(
                EC.presence_of_element_located((By.XPATH, title_xpath))
            ).text.replace(' ', '_').replace('/', '_')

            print(title)
            time.sleep(1)

            img_xpath = '//*[@id="app"]/div/div/div[6]/span/div/span/div/div[2]/div/div[2]/div/div[1]/div[1]/div/img'
            img = WebDriverWait(browser, 500).until(
                EC.presence_of_element_located((By.XPATH, img_xpath))
            ).screenshot(f"images/{i}_{title}.png")
            time.sleep(1)

            btn_back_xpath = '//*[@id="app"]/div/div/div[6]/span/div/span/div/header/div/div[1]/div/span'
            btn_back = WebDriverWait(browser, 500).until(
                EC.presence_of_element_located((By.XPATH, btn_back_xpath))
            )
            btn_back.click()
        except:
            break

    
except Exception as ex:
    print(ex)
finally:
    browser.quit()

"""
for group in groups:
    search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'

    search_box = WebDriverWait(browser, 500).until(
        EC.presence_of_element_located((By.XPATH, search_xpath))
    )

    search_box.clear()

    time.sleep(1)

    pyperclip.copy(group)

    search_box.send_keys(Keys.SHIFT, Keys.INSERT)  # Keys.CONTROL + "v"

    time.sleep(2)

    group_xpath = f'//span[@title="{group}"]'
    group_title = browser.find_element_by_xpath(group_xpath)

    group_title.click()

    time.sleep(1)

    input_xpath = '//div[@contenteditable="true"][@data-tab="1"]'
    input_box = browser.find_element_by_xpath(input_xpath)

    pyperclip.copy(msg)
    input_box.send_keys(Keys.SHIFT, Keys.INSERT)  # Keys.CONTROL + "v"
    input_box.send_keys(Keys.ENTER)
"""
