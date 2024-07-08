from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def calcular_horas_pert(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    estimado = (a + 4 * b + c) / 6
    intervalo_confianza = (c - a) / 6
    return estimado, intervalo_confianza

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roles')
def roles():
    return render_template('roles.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.json
    a = data['a']
    b = data['b']
    c = data['c']
    estimado, intervalo = calcular_horas_pert(a, b, c)
    intervalo = round(intervalo, 0)
    estimado = round(estimado, 0)
    probable = estimado + intervalo
    return jsonify({"estimado": estimado, "intervalo": intervalo , "probable": probable})

if __name__ == '__main__':
    app.run(debug=True)
