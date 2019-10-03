import requests
import sys
from googletrans import Translator

input_file = open(sys.argv[1], "r")
file_content = input_file.readlines()
translator = Translator()

for line in file_content:
    translated_text = translator.translate(line, dest="km")
    url="https://translate.google.com/translate_tts?ie=UTF-8&tl=km&client=tw-ob&q=" + translated_text.text
    print(url)
    doc = requests.get(url)
    
    filename = "files/" + line.rstrip() + ".mp3"
    filename = filename.replace(" ", "_")
    with open(filename, "wb") as f:
        f.write(doc.content)