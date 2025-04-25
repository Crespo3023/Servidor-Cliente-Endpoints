from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "<h1> Página principal </h1>"


@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        
        "version de prueba": "8",
        "Usuario": "Jankarlos Crespo"
    })

@app.route("/mensaje", methods=["POST"])
def mensaje():
    data= request.get_json()
    if not data or "mensaje" not in data:
        return jsonify({"Se encontro un error": "El mensaje no ha sido proporcionado"}), 400
    
    mensaje_usuario = data["mensaje"]
    respuesta = f"Mensaje recibido gracias: {mensaje_usuario}"
    return jsonify({"respuesta": respuesta}), 200   

      


if __name__ == '__main__':
    app.run(debug=True)