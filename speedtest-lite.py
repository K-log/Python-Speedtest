import json
import io
import sys
import os
import time
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def render_page(url):
    options = Options()
    options.set_headless(headless=True)
    driver = webdriver.Chrome(chrome_options=options)
    print("Connecting to URL...")
    driver.get(url)
    print("Waiting for page contents to load...\n(Should take about 10 seconds)")
    time.sleep(10)
    print("Web page content retrieval successful!")
    ret = driver.page_source
    print('Closing browser...')
    driver.close()
    return ret 


def find_elements(page_source):
    try:
        print('Parsing webpage source...')
        soup = BeautifulSoup(page_source, "html.parser")
        speed_value = soup.find('div', attrs={'class': 'speed-results-container'})
    except:
        print('Failed to parse webpage source...')
        speed_value = -1
    return speed_value


if __name__ == "__main__":
    target_url = "http://fast.com"
    page = render_page(target_url)
    contents = find_elements(page)
    print("Your current download speed is: " + contents.string + "Mbps!")