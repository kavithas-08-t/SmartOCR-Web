from flask import Flask, render_template, request, send_file
from ocr import extract_text
from pdf_reader import extract_pdf_text
from translator import translate_text
from speech import text_to_audio
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
AUDIO_FOLDER = "static/audio"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(AUDIO_FOLDER, exist_ok=True)

LANGUAGES = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi"
}


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route("/convert", methods=["POST"])
def convert():

    uploaded_file = request.files["file"]

    language = request.form["language"]

    filepath = os.path.join(
        UPLOAD_FOLDER,
        uploaded_file.filename
    )

    uploaded_file.save(filepath)

    # OCR or PDF Extraction

    if filepath.lower().endswith(".pdf"):

        text = extract_pdf_text(
            filepath
        )

    else:

        text = extract_text(
            filepath
        )

    # Translation

    translated_text = translate_text(
        text,
        language
    )

    app.config[
        "LAST_TEXT"
    ] = translated_text

    # Audio Generation

    audio_path = os.path.join(
        AUDIO_FOLDER,
        "output.mp3"
    )

    text_to_audio(
        translated_text,
        audio_path,
        LANGUAGES[language]
    )

    return render_template(
    "index.html",
    extracted_text=translated_text,
    audio_file=audio_path,
    uploaded_file=filepath,
    status="✅ Conversion Completed Successfully"
)


@app.route("/download-text")
def download_text():

    text_file = "translated_text.txt"

    with open(
        text_file,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            app.config.get(
                "LAST_TEXT",
                ""
            )
        )

    return send_file(
        text_file,
        as_attachment=True
    )


if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            5000
        )
    )

    app.run(
        host="0.0.0.0",
        port=port
    )
