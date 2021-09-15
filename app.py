import requests
from flask import Flask, render_template, request

import pandas as pd

#instancia o meu app no servidor
app = Flask(__name__)

@app.route('/ibge/', methods = ['POST'])
def getCEP():
   #cep = request.args.get("cep")
    cep = request.form.get("cep")
    url = "https://viacep.com.br/ws/" + cep + "/json/"
    dados = requests.get(url)
    return dados.json()

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
