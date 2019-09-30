from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import sys
from googletrans import Translator
from gtts import gTTS

def click_on_download():
    time.sleep(2)
    download_btn = driver.find_element_by_link_text("DOWNLOAD")
    download_btn.click()

def get_numbers():
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

def get_from_file():
    input_file = open(sys.argv[1], "r")
    file_content = input_file.readlines()
    translator = Translator()
    translated_text = translator.translate("monday", dest="km")

    for line in file_content:
        translated_text = translator.translate(line, dest="km")

        driver.find_element_by_tag_name("textarea").send_keys(translated_text.text)

        submit_btn = driver.find_element_by_tag_name("input")
        submit_btn.click()

        loaded = False

        while not loaded:
            try:
                click_on_download()
                print("Success - ", "mp3 downloaded")
                loaded = True
            except:
                print("Exception - ", "mp3 has not loaded yet")
                loaded = False

driver = webdriver.Chrome()
driver.get("https://soundoftext.com/")

drop_down = Select(driver.find_element_by_tag_name("select"))
drop_down.select_by_index(30)

if(len(sys.argv) == 3):
    get_numbers()
else:
    get_from_file()