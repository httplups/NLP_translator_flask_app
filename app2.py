from flask import Flask, request, render_template
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
# from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer
import socket
  
tokenizer = AutoTokenizer.from_pretrained("unicamp-dl/translation-pt-en-t5")

model = AutoModelForSeq2SeqLM.from_pretrained("unicamp-dl/translation-pt-en-t5")

# pten_pipeline = pipeline('text2text-generation', model=model, tokenizer=tokenizer)

# instanciate Flask
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hostname = socket.gethostname()
    if request.method == "GET":
        return render_template("index.html", hostname = hostname)

    input = request.get_data().decode('UTF-8')
    encoded_zh = tokenizer("translate Portuguese to English: " + input, return_tensors="pt")
    generated_tokens = model.generate(**encoded_zh)
    
    translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    # translated_text = pten_pipeline("translate Portuguese to English: " + input)[0]['generated_text']
    return {'translated_text': translated_text}

if __name__ == '__main__':
    # start Flask
    app.run(host="0.0.0.0", port=5000, debug=True)