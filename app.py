from flask import Flask, render_template, Response, request, redirect, url_for
from bot import main

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('welcome.html')

@app.route("/command/", methods=['POST'])
def handle_data():
    command = request.form['commandInput']
    sentence = request.form['sentenceInput']
    main(command, sentence)
    return render_template('welcome.html', message=command)

if __name__ == "__main__":
    app.run()
