from flask import Flask, jsonify

main = Flask(__name__)

@main.route('/personas', methods=['GET'])
def obtener_personas():
    # Lista de nombres de personas
    lista_personas = ["Carro", "Moto", "Bmw", "Mazda", "Spark"]
    # Convertir la lista a JSON y devolverla
    return jsonify(lista_personas)

if __name__ == '__main__':
    main.run(debug=True)
