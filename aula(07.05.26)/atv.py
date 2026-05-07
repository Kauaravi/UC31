from flask import Flask, render_template

app = Flask(__name__)

# Dados das pizzas
pizzas = {
    "calabresa": "calabresa.jpg",
    "margherita": "margherita.jpg",
    "frango": "frango.png"
}

@app.route("/pizzaria/<sabor>")
def pizzaria(sabor):

    # Verifica se o sabor existe
    if sabor in pizzas:
        return render_template(
            "pizza.html",
            sabor=sabor.capitalize(),
            imagem=pizzas[sabor]
        )

    return "<h1>Sabor não disponível!</h1>"

app.run(debug=True)