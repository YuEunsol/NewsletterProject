
import time
from urllib import parse
from selenium import webdriver
import datetime
import pprint
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



naver_url = "https://naver.com"
naver_news_page_url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query="