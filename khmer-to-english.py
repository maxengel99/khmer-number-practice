import os
from googletrans import Translator

for filename in os.scandir("files"):
    translator = Translator()
    translated_text = translator.translate(filename.name[:-4], dest="en")
    print(translated_text.text)
    dst = "files/" + translated_text.text + ".mp3"
    os.rename("files/" + filename.name, dst)