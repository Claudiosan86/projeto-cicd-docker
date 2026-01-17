from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Projeto CI/CD do Claudio San Roman - N3 com Sucesso!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
