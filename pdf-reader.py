from gtts import gTTS
import PyPDF2
import os

input_file = open('RH_StudyGuide_V2.pdf', 'rb')

text = PyPDF2.PdfFileReader(input_file)

pages = text.numPages
print(pages)

pageObj = text.getPage(6)
print(pageObj.extractText())

language = 'en'

output = gTTS(text=text, lang=language, slow=False)

# output.save("output.mp3")

# os.system("rhythmbox output.mp3") #for Linux based system

# os.system("./output.mp3") #for Linux based system

# os.system("start output.mp3") #for Windows based system