from flask import Flask, abort

app = Flask(__name__)

@app.route('/operacao/<tipo>/<int:op1>/<int:op2>')
def operacao(tipo, op1, op2):
    if tipo == 'sum':
        resultado = op1 + op2
        mensagem = f"A soma de {op1} e {op2} é {resultado}."
    elif tipo == 'sub':
        resultado = op1 - op2
        mensagem = f"A subtração de {op1} por {op2} é {resultado}."
    elif tipo == 'mult':
        resultado = op1 * op2
        mensagem = f"A multiplicação de {op1} por {op2} é {resultado}."
    elif tipo == 'div':
        if op2 == 0:
            return "Não é possível dividir por zero.", 400
        resultado = op1 / op2
        mensagem = f"A divisão de {op1} por {op2} é {resultado}."
    else:
        abort(404)
    return mensagem

if __name__ == '__main__':
    app.run(debug=True)