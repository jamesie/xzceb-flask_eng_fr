from machinetranslation import translator
from flask import Flask, render_template, request
from machinetranslation import translator
import json

app = Flask("Web Translator", static_folder="templates")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return translator.englishToFrench(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return translator.frenchToEnglish(textToTranslate)

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    render_template('index.html')
    return

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
