import datetime

from config import *


def setInitialDriver():
    chrome_options = Options()
    chrome_options.add_argument('headless')
    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()), options=chrome_options)
    driver.back()

    return driver

def setUrl(keyword):
    url = naver_news_page_url
    url = url + parse.quote(keyword)
    url = url + "&nso=so%3Ar%2Cp%3A1d"

    return url

def crawlNews(driver):
    news_list = []
    while True:
        # 뉴스 리스트
        news_box_list = driver.find_elements(By.CSS_SELECTOR, '#main_pack > section > div > div.group_news > ul > li')

        for news_box in news_box_list:
            news_box_id = news_box.get_attribute("id")

            press = findPress(driver, news_box_id)
            upload_time = findUploadTime(driver, news_box_id)
            title = findNewsTitle(driver, news_box_id)
            contents = findContents(driver, news_box_id)
            link = findLink(driver, news_box_id)

            print(title)
            print(press)
            print(upload_time)
            print(contents)
            print(link)

            news_dict = {"title" : title,
                         "press" : press,
                         "upload time" : upload_time,
                         "contents" : contents,
                         "link" : link}

            news_list.append(news_dict)

        next_button = driver.find_element(By.XPATH, '//*[@id="main_pack"]/div[2]/div/a[2]')
        next_button_clickable = True if next_button.get_attribute("aria-disabled") == "false" else False

        if next_button_clickable is True:
            next_button.click()
        else:
            pprint.pprint(news_list)
            print(f"뉴스가 총 {len(news_list)}개 스크랩 되었습니다.")
            return news_list


def findPress(driver, news_box_id):
    # 언론사 명
    press_selector = f'#{news_box_id} > div.news_wrap.api_ani_send > div > div.news_info > div.info_group > a.info.press'
    press = driver.find_element(By.CSS_SELECTOR, press_selector).get_attribute("innerText")
    press = press.replace("언론사 선정", "")

    return press

def findUploadTime(driver, news_box_id):
    # 게시 일시
    upload_time_selector = f'#{news_box_id} > div > div > div.news_info > div.info_group > span'
    upload_time_before_group = driver.find_elements(By.CSS_SELECTOR, upload_time_selector)
    for each in upload_time_before_group:
        upload_time_before = each.get_attribute("innerText")
        if "전" in upload_time_before:
            break
    if "시간 전" in upload_time_before:
        elapsed_time = int(upload_time_before.replace("시간 전", ""))
        now = datetime.datetime.now()
        upload_time = now - datetime.timedelta(hours=elapsed_time)
        upload_time = upload_time.strftime('%Y-%m-%d %H시 경')
    elif "분 전" in upload_time_before:
        elapsed_time = int(upload_time_before.replace("분 전", ""))
        now = datetime.datetime.now()
        upload_time = now - datetime.timedelta(minutes=elapsed_time)
        upload_time = upload_time.strftime('%Y-%m-%d %H시 경')

    return upload_time

def findNewsTitle(driver, news_box_id):
    # 뉴스 타이틀
    try:
        title_selector = f'//*[@id="{news_box_id}"]/div[1]/div/div[2]/a[2]'
        title = driver.find_element(By.XPATH, title_selector).get_attribute("innerText")

        return title
    except:
        title_selector = f'//*[@id="{news_box_id}"]/div[1]/div/div[2]/a'
        title = driver.find_element(By.XPATH, title_selector).get_attribute("innerText")

        return title

def findContents(driver, news_box_id):
    # 뉴스 내용
    contents_selector = f'//*[@id="{news_box_id}"]/div/div/div[2]/div/div/a'
    contents = driver.find_element(By.XPATH, contents_selector).get_attribute("innerText")

    return contents

def findLink(driver, news_box_id):
    # 뉴스 링크
    link_selector = f'//*[@id="{news_box_id}"]/div/div/div[2]/a[1]'
    link = driver.find_element(By.XPATH, link_selector).get_attribute("href")

    return link


driver = setInitialDriver()
url = setUrl("현대 엔지니어링")
driver.get(url)
time.sleep(1)
news_list = crawlNews(driver)
