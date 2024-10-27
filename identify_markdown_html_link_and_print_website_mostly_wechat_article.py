import re
import os
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


# Step 1: 读取Markdown文件并提取链接和标题
def extract_urls_and_titles_from_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    # 使用正则表达式提取Markdown链接标题和URL
    pattern = re.compile(r'\[(.*?)\]\((https://\S+)\)')  # 处理所有以 https:// 开头的链接
    links = pattern.findall(content)
    return links

# 页面滚动函数
def scroll_page(driver, scroll_count=20, scroll_pause_time=1):
    for _ in range(scroll_count):
        # 模拟按下 Page Down
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(scroll_pause_time)

# Step 2: 设置Selenium，访问链接并保存为PDF
def capture_pdf_from_urls(links, output_dir):
    # 打印设置
    settings = {
        "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": ""
        }],
        "selectedDestinationId": "Save as PDF",
        "version": 2,
        "isHeaderFooterEnabled": False,
        "isLandscapeEnabled": True,
        "isCssBackgroundEnabled": True,
        "mediaSize": {
            "height_microns": 297000,
            "name": "ISO_A4",
            "width_microns": 210000,
            "custom_display_name": "A4 210 x 297 mm"
        },
    }
    prefs = {
        'printing.print_preview_sticky_settings.appState': json.dumps(settings),
        'savefile.default_directory': output_dir  # PDF输出路径
    }

    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument('--enable-print-browser')
    chrome_options.add_argument('--kiosk-printing')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-extensions')

    # 初始化浏览器驱动
    driver = webdriver.Chrome(options=chrome_options)

    for index, (title, url) in enumerate(links, start=1):
        '''
        if index<=140:
            continue
        '''

        driver.get(url)
        driver.maximize_window()
        time.sleep(3)  # 等待页面加载，确保内容完全展示

        # 检测是否为微信链接并处理迁移页面
        if "mp.weixin.qq.com" in url:
            try:
                migration_notice = driver.find_element(By.XPATH, "//*[contains(text(), '该公众号已迁移')]")
                if migration_notice:
                    access_article_button = driver.find_element(By.XPATH, "//*[contains(text(), '访问文章')]")
                    access_article_button.click()
                    time.sleep(3)  # 等待页面跳转
            except:
                print(f"No migration detected for {url}")

        # 模拟按下 Page Down 20 次
        scroll_page(driver, scroll_count=20)

        '''
        if '.pdf' not in url and 'https://leetcode-cn.com' not in url:
            # 等待所有图像加载完成
            WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.TAG_NAME, "img")))
        '''

        # Step 4: 打印并保存为PDF
        pdf_name = f"{index:02d}_{title}.pdf"
        driver.execute_script(f'document.title="{pdf_name}"; window.print();')
        time.sleep(10)  # 等待打印完成
        driver.refresh()
        time.sleep(3)

        print(f"Saved PDF as {pdf_name}")

    driver.close()

# 使用示例
markdown_path = 'C:/Users/chenguanbin/OneDrive - hust.edu.cn/_工作/八股文/cpp-learning/README.md'
output_directory = 'C:/Users/chenguanbin/OneDrive - hust.edu.cn/_工作/八股文/cpp_learning_pdf_files'

# 创建输出目录
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# 提取链接和标题并保存PDF
links = extract_urls_and_titles_from_markdown(markdown_path)
capture_pdf_from_urls(links, output_directory)
