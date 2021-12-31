from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def main():
    return "Jakiś tekst"

@app.route('/index/')
def index():
    return render_template('index.html')
