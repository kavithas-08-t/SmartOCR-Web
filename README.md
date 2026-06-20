# Smart OCR Translator & Voice Assistant

## Overview

Smart OCR Translator & Voice Assistant is a Flask-based web application that extracts text from images and PDF documents using Tesseract OCR, translates the extracted text into multiple languages, and converts the translated text into speech.

## Features

* Upload Images (PNG, JPG, JPEG)
* Upload PDF Documents
* OCR Text Extraction using Tesseract
* Multilingual Translation

  * English
  * Tamil
  * Hindi
* Text-to-Speech Conversion
* Audio Playback
* Download Audio (MP3)
* Download Translated Text
* Image Preview
* Drag & Drop Upload Interface
* Responsive Web Design

## Technologies Used

### Frontend

* HTML5
* CSS3

### Backend

* Python
* Flask

### Libraries

* pytesseract
* Pillow
* pdfplumber
* gTTS
* deep-translator

## Project Structure

SmartOCR-Web

* app.py
* ocr.py
* pdf_reader.py
* speech.py
* translator.py
* requirements.txt
* templates/

  * index.html
* static/

  * uploads/
  * audio/

## Installation

1. Clone the repository

2. Install dependencies

pip install -r requirements.txt

3. Run the application

python app.py

4. Open browser

http://127.0.0.1:5000

## Author

Akash

## Future Enhancements

* Additional Language Support
* Cloud Deployment
* User Authentication
* OCR Accuracy Improvements
* Mobile Application Version
