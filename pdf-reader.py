from gtts import gTTS
import PyPDF2

input_file = open('RH_StudyGuide_V2.pdf', 'rb')

text = PyPDF2.PdfFileReader(input_file)

print(text.numPages)

language = 'en'
output_text = ''

for pagenum in range (0, text.numPages):
    pageObj = text.getPage(pagenum)
    output_text = output_text + pageObj.extractText()
    output = gTTS(text=output_text, lang=language, slow=False)

output.save("output.mp3")