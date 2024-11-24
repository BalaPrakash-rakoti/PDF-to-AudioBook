import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename
def read_pdf():
    book = askopenfilename(title="Select PDF", filetypes=[("PDF files", "*.pdf")])
    pdfreader = PyPDF2.PdfReader(book)
    pages = len(pdfreader.pages)
    player = pyttsx3.init()
    rate = player.getProperty('rate')
    player.setProperty('rate', rate - 75)
    for num in range(pages):
        page = pdfreader.pages[num]
        text = page.extract_text()
        player.say(text)# Speak the text
    player.runAndWait()
read_pdf()