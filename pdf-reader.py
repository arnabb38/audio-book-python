# Author : Arnab Basak

from tkinter import Tk
from tkinter.filedialog import askopenfilename
from gtts import gTTS
import PyPDF2
import os

Tk().withdraw()
filelocation = askopenfilename()

basename = os.path.basename(filelocation)

filename = os.path.splitext(basename)[0]

with open(filelocation, 'rb') as f:

    text = PyPDF2.PdfFileReader(f, strict=False)

    print(text.numPages)

    language = 'en'
    output_text = ''

    for pagenum in range (0, text.numPages):
        pageObj = text.getPage(pagenum)
        output_text = output_text + pageObj.extractText()
        output = gTTS(text=output_text, lang=language, slow=False)

    output.save(filename+".mp3")

f.close()