from deep_translator import GoogleTranslator

LANGUAGE_CODES = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi"
}

def translate_text(
    text,
    language_name
):

    target_language = LANGUAGE_CODES[
        language_name
    ]

    translated_text = GoogleTranslator(
        source="auto",
        target=target_language
    ).translate(text)

    return translated_text