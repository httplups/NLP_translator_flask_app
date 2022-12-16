from flask import Flask, request, render_template
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer
import socket
  
# translate Chinese to English
tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M")
model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")
tokenizer.src_lang = "en"
# instanciate Flask
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hostname = socket.gethostname()
    if request.method == "GET":
        return render_template("index.html", hostname = hostname)

    input = request.get_data().decode('UTF-8')
    encoded_zh = tokenizer(input, return_tensors="pt")
    generated_tokens = model.generate(**encoded_zh, forced_bos_token_id=tokenizer.get_lang_id("pt"))
    translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    return {'translated_text': translated_text}

if __name__ == '__main__':
    # start Flask
    app.run(host="0.0.0.0", port=5000, debug=True)