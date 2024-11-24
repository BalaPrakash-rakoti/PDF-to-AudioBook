# PDF-to-AudioBook
This Python script allows you to convert text from PDF files into speech using a simple graphical interface. It is designed to provide a hands-free, accessible way to consume written content.

## Features
- **PDF File Selection**: Easily select a PDF file using a graphical file dialog.
- **Text Extraction**: Extracts text content from all pages of the selected PDF.
- **Text-to-Speech Conversion**: Reads the text aloud using the `pyttsx3` text-to-speech library.
- **Adjustable Speech Rate**: Customizable speech speed for better comprehension.

## Prerequisites
Ensure you have Python installed on your system. You’ll also need the following Python libraries:
- `pyttsx3` for text-to-speech functionality
- `PyPDF2` for reading PDF content
- `tkinter` (pre-installed with Python) for file selection dialog

Install the required libraries using:

pip install pyttsx3 PyPDF2

Code Overview:

The script performs the following:

Opens a file dialog to select a PDF.
Reads the number of pages in the PDF.
Extracts text from each page using PyPDF2.
Converts the extracted text to speech using pyttsx3.
Speaks the content aloud, page by page.
