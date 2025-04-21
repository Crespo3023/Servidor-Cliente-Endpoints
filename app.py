from flask import Flask, request, jsonify

app = Flask(__name__)

mensajes = []

@app.route("/", methods=["GET"])
def home():
    return "<h1> Página principal </h1>"


@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        
        "version de prueba": "7",
        "Usuario": "Jankarlos Crespo"
    })

@app.route("/mensaje", methods=["GET", "POST"])
def mensaje():
    if request.method == "GET":
        return jsonify({"mensajes": mensajes})

    if request.method == "POST":
        data = request.json
        if not data or "mensaje" not in data:
            return jsonify({"Se encontro un error": "El mensaje no ha sido proporcionado"}), 400

        mensajes.append(data["mensaje"])
        return jsonify({"respuesta": f"Mensaje recibido correctamente: '{data['mensaje']}'"}), 201

if __name__ == '__main__':
    app.run(debug=True)