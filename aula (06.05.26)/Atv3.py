from flask import Flask, send_file, abort

app = Flask(__name__)

@app.route('/arearestrita/<int:id>')
def area_restrita(id):
    if id == 1:
        return send_file('cadeado_fechado.png', mimetype='cadeado_fechado.png')
    elif id == 2:
        return send_file('cadeado_aberto.png', mimetype='cadeado_aberto.png')
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)