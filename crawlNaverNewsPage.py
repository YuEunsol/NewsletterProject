from config import *

from selenium import webdriver
import time

def setInitialDriver():
    driver = webdriver.Chrome('chromedriver')
    driver.get(naver_url)
