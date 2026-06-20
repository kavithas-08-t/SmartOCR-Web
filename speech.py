from gtts import gTTS

def text_to_audio(
    text,
    filename,
    language
):

    tts = gTTS(
        text=text,
        lang=language
    )

    tts.save(filename)