from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder='css') 

# Lugares peligrosos predeterminados
dangerous_locations = [
    {"latitud": -13.418813, "longitud": -76.126554},
    {"latitud": -13.420731, "longitud": -76.139994},
    {"latitud": -13.420090, "longitud": -76.143088}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_danger_locations')
def get_danger_locations():
    return jsonify(dangerous_locations)

@app.route('/add_danger_location', methods=['POST'])
def add_danger_location():
    data = request.get_json()
    latitud = data['latitud']
    longitud = data['longitud']
    dangerous_locations.append({'latitud': latitud, 'longitud': longitud})
    return jsonify({'message': 'Lugar peligroso agregado exitosamente.'})

@app.route('/check', methods=['POST'])
def check_location():
    data = request.get_json()
    latitud = float(data['latitud'])
    longitud = float(data['longitud'])
    return jsonify({'latitud': latitud, 'longitud': longitud})

if __name__ == '__main__':
    app.run(debug=True)
