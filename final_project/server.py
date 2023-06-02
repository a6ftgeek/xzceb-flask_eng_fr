"""Simple Flask Translator Example"""
from machinetranslation import translator
import json
from flask import Flask, render_template, request

app = Flask("Web Translator")

@app.route("/englishToFrench")
def e2f():
    """get text from request"""
    text_to_translate = request.args.get('textToTranslate')
    """translate text"""
    translated_text = english_to_french(text_to_translate)
    return translated_text

@app.route("/frenchToEnglish")
def f2e():
    """get text from request"""
    text_to_translate = request.args.get('textToTranslate')
    """translate text"""
    translated_text = french_to_english(text_to_translate)
    return translated_text

@app.route("/")
def renderIndexPage():
    """Serves the index page"""
    return app.send_static_file('/index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
