from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

english_chatbot = ChatBot("ChatterBot", storage_adapter="chatterbot.storage.SQULAdapter")

trainer = ChatterBotCorpusTrainer(english_chatbot)
trainer.train("chatterbot.corpus.english")

@app.route("/")

def home():
    return render_template("index.html")

@app.route("/get")

def get_bot_response():
    userText = request.args.get('msg')
    return str(english_chatbot.get_response(userText))

if __name__ == '__main__':
    app.run()
