@app.route('/cantinho')
@login_necessario
def cantinho():
    nome = session.get('usuario_nome')

    visitas = session.get('visitas_cantinho', 0)
    visitas += 1
    session['visitas_cantinho'] = visitas

visitas = session.get('visitas_cantinho', 0)
visitas += 1
session['visitas_cantinho'] = visitas

    return render_template(
        'cantinho.html',
        nome='nome',
        cor='Preto',
        linguagem='Python',
        frase='A prática leva à perfeição.',
        visitas=visitas
    )
<p>Você visitou esse cantinho {{ visitas }} vez(es) hoje.</p>

