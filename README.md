# PDF-to-AudioBook
This Python script is a Text-to-Speech PDF Reader that converts the text content of a PDF file into speech. Designed for convenience and accessibility, the program uses the following modules:

1.PyPDF2 for reading and extracting text from PDF files.
2.pyttsx3 for converting the extracted text into audible speech.
3.tkinter.filedialog for providing a graphical interface to select the PDF file.

Functionality:
PDF File Selection:
Users can browse and select a PDF file through a dialog box, ensuring a simple and intuitive interface.

Text Extraction:
The script reads the PDF file page by page, extracting the text content.

Text-to-Speech Conversion:
The extracted text is converted to speech using the pyttsx3 library.

The speech rate is adjusted for clarity, with the default rate reduced for slower, more understandable speech.
Page-by-Page Narration:
The program processes all pages in sequence, reading the text aloud.

Use Cases:
E-Book Reading: Makes it easy to listen to books in PDF format.
Accessibility: Helps visually impaired users consume written content.
Hands-Free Reading: Convenient for multitasking or listening on the go.

Features:
Customizable speech rate for better comprehension.
Easy file selection through a graphical interface.
Automatic processing of all pages in the PDF.
This script offers a straightforward and efficient way to convert PDFs into spoken content, making it practical for both casual and accessibility-focused applications.

# PDF-to-AudioBook

This Python script allows you to convert text from PDF files into speech using a simple graphical interface. It is designed to provide a hands-free, accessible way to consume written content.

## Features
PDF File Selection: Easily select a PDF file using a graphical file dialog.
Text Extraction: Extracts text content from all pages of the selected PDF.
Text-to-Speech Conversion: Reads the text aloud using the `pyttsx3` text-to-speech library.
Adjustable Speech Rate: Customizable speech speed for better comprehension.

Prerequisites:
Ensure you have Python installed on your system. You’ll also need the following Python libraries:
 `pyttsx3` for text-to-speech functionality
 `PyPDF2` for reading PDF content
 `tkinter` (pre-installed with Python) for file selection dialog

Install the required libraries using:
```bash
pip install pyttsx3 PyPDF2

Code Overview
The script performs the following:

Opens a file dialog to select a PDF.
Reads the number of pages in the PDF.
Extracts text from each page using PyPDF2.
Converts the extracted text to speech using pyttsx3.
Speaks the content aloud, page by page.

Customization
Speech Rate: You can modify the speech rate in the script:

python
Copy code
rate = player.getProperty('rate')  # Get the current rate
player.setProperty('rate', rate - 75)  # Decrease the rate for slower speech
Voice Selection: You can customize the voice used for narration by changing the pyttsx3 voice properties:

python
Copy code
voices = player.getProperty('voices')
player.setProperty('voice', voices[0].id)  # Use the first available voice
Applications
E-Book Reading: Listen to books in PDF format.
Accessibility: Supports users with visual impairments.
Hands-Free Reading: Convenient for multitasking.
Future Enhancements
Add error handling for unsupported PDF formats or empty pages.
Allow users to pause, resume, or skip pages.
Support for selecting specific pages to read.
