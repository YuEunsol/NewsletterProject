
import time
from urllib import parse
from selenium import webdriver
import datetime
import pprint
from openpyxl import Workbook
from openpyxl.styles import Font, Border, Side, Alignment, named_styles, Color, PatternFill
from string import ascii_uppercase
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


columns = ["언론사", "업로드 일시", "제목", "내용", "링크"]

xl_path = "C:/Users/K/Desktop/test"

today = datetime.date.today()
naver_url = "https://naver.com"
naver_news_page_url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query="