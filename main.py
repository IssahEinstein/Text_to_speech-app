import pyttsx3
from PyPDF2 import PdfReader
from tkinter.filedialog import askopenfile

# Open file dialog
book = askopenfile(mode="rb")

if book:  # Ensure a file was selected
    pdfreader = PdfReader(book)
    pages = len(pdfreader.pages)

    # Initialize text-to-speech engine once
    player = pyttsx3.init()

    for num in range(pages):
        page = pdfreader.pages[num]
        text = page.extract_text()

        if text.strip():  # Ensure text is not empty
            player.say(text)

    player.runAndWait()
else:
    print("No file selected.")
