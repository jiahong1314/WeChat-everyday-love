from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('randomCall.html')

if __name__ == '__main__':
    app.run()
