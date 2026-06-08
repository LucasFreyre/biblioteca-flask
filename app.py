from flask import Flask, render_template
import dados

app = Flask(__name__)

@app.route("/")
def index():
    livros = dados.carregar_do_arquivo()
    return render_template("index.html", livros=livros)

if __name__ == "__main__":
    app.run(debug=True)