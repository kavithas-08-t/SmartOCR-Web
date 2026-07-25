# Smart OCR Translator & Voice Assistant

A Flask-based web application that extracts text from images and PDF files using OCR, translates the extracted text into multiple languages, and converts the translated text into speech.

---

## Features

- Extract text from Images (PNG, JPG, JPEG)
- Extract text from PDF documents
- OCR using Tesseract OCR
- Translate text into multiple languages
  - English
  - Tamil
  - Hindi
- Convert translated text into speech
- Audio playback
- Download translated text
- Download generated audio (MP3)
- Drag & Drop file upload
- Image preview
- Responsive design (Desktop & Mobile)
- Docker support
- Deployed on Render

---

## Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### Libraries
- pytesseract
- Pillow
- pdfplumber
- deep-translator
- gTTS

### Deployment
- Docker
- GitHub
- Render

---

## Project Structure

```
SmartOCR-Web/
│
├── app.py
├── ocr.py
├── pdf_reader.py
├── translator.py
├── speech.py
├── requirements.txt
├── Dockerfile
│
├── templates/
│   └── index.html
│
└── static/
    ├── uploads/
    └── audio/
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/SmartOCR-Web.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

### Open in Browser

```
http://127.0.0.1:5000
```

---

## Live Demo

(https://smartocr-web-0zh5.onrender.com)

---

## Future Enhancements

- Support more languages
- Speech-to-Text
- AI Text Summarization
- User Authentication
- OCR History
- Mobile App Version

---

## Author

**Akash**

Final Year - Computer Science and Business Systems (CSBS)
