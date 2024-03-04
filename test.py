import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'plugins.always_open_pdf_externally': True
})

service = Service(executable_path="#")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://arxiv.org/list/astro-ph.GA/new')

element = driver.find_element(By.XPATH, '//span[@class="list-identifier"]/a[contains(@title, "Download PDF")]')
pdf_url = element.get_attribute("href")

print(pdf_url)

current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_path = f"current_time_{current_time}.pdf"

response = requests.get(pdf_url)

with open(file_path, "wb") as f:
    f.write(response.content)

print("PDF downloaded successfully.")
time.sleep(10)