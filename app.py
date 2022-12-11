from flask import Flask, request, render_template
from transformers import pipeline

# load model
pipe = pipeline("translation", model="t5-small")

# instanciate Flask
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    input = request.get_data().decode('UTF-8')
    translated_text =  pipe(input)[0]['translation_text']
    return translated_text

if __name__ == '__main__':
    # start Flask
    app.run(debug=True)