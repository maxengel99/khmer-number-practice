from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import sys

def click_on_download():
    time.sleep(2)
    download_btn = driver.find_element_by_link_text("DOWNLOAD")
    download_btn.click()

driver = webdriver.Chrome()
driver.get("https://soundoftext.com/")

drop_down = Select(driver.find_element_by_tag_name("select"))
drop_down.select_by_index(30)

begin_num = int(sys.argv[1])
end_num = int(sys.argv[2]) + 1

for i in range(begin_num, end_num):
    driver.find_element_by_tag_name("textarea").send_keys(str(i))

    submit_btn = driver.find_element_by_tag_name("input")
    submit_btn.click()

    loaded = False

    while not loaded:
        try:
            click_on_download()
            print("Success - ", str(i), "mp3 downloaded")
            loaded = True
        except Exception as e:
            print("Exception - ", str(i), "mp3 has not loaded yet")
            loaded = False
