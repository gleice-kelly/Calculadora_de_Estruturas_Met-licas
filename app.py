
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    length = data['length']
    width = data['width']
    material = data['material']

    # Definir densidade dos materiais (kg/m³)
    if material == 'aço':
        density = 7850  # Densidade do aço
    elif material == 'alumínio':
        density = 2700  # Densidade do alumínio
    else:
        return jsonify({"error": "Material desconhecido"}), 400

    # Cálculo do volume aproximado da estrutura (exemplo simplificado)
    thickness = 0.1  # Espessura padrão
    volume = length * width * thickness

    # Cálculo do peso
    weight = volume * density

    return jsonify({'weight': weight})

if __name__ == '__main__':
    app.run(debug=True)
