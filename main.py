from config import *
from manageXl import *
from crawlNaverNewsPage import *

if __name__ == '__main__':
    driver = setInitialDriver()
    url = setUrl("현대엔지니어링")
    driver.get(url)
    time.sleep(1)
    news_list = crawlNews(driver)
    createXl("현대엔지니어링", news_list)