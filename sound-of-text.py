from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("https://soundoftext.com/")
driver.find_element_by_tag_name("textarea").send_keys("Hello")

drop_down = Select(driver.find_element_by_tag_name("select"))
drop_down.select_by_index(30)

submit_btn = driver.find_element_by_tag_name("input")
submit_btn.click()

time.sleep(2)
#element = WebDriverWait(driver, 20).until( EC.element_to_be_clickable((By.LINK_TEXT, "DOWNLOAD")))
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "DOWNLOAD")))

download_btn = driver.find_element_by_link_text("DOWNLOAD")
#print(download_btn.get_attribute("href"))
download_btn.click()
##print(download_btn)
