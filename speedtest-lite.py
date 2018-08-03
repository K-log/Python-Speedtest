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
    # Connect to the given URL and return the source code of the page.
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
    # Search throught the page's source HTML to find the speed test value.
    try:
        print('Parsing webpage source...')
        soup = BeautifulSoup(page_source, "html.parser")
        speed_value = soup.find('div', attrs={'class': 'speed-results-container'})
    except:
        print('Failed to parse webpage source...')
        speed_value = -1
    return speed_value

def calc_speed(url):
    # Get the current download three times and average it to get a more accurate value.

    first = int(find_elements(render_page(url)).string)
    second = int(find_elements(render_page(url)).string)
    third = int(find_elements(render_page(url)).string)

    return ( (first + second + third) / 3 )

if __name__ == "__main__":
    target_url = "http://fast.com"
    
    print("Your current download speed is: " + str(calc_speed(target_url)) + "Mbps!")