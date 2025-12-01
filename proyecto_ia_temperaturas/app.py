import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from flask import Flask, request, jsonify, render_template

# --- PASO 3: Cargar los modelos ---
try:
    # Asegúrate de que las rutas a los archivos .h5 sean correctas
    MODELO_F = load_model('models/modelo_c_a_f.h5')
    MODELO_K = load_model('models/modelo_c_a_k.h5')
    print("✅ Modelos de IA cargados correctamente.")
except Exception as e:
    print(f"❌ Error al cargar los modelos: {e}. ¿Están en la carpeta 'models'?")
    exit()

# Inicializar la aplicación Flask (para el paso 4)
app = Flask(__name__)

# Continúa en app.py

@app.route('/convertir', methods=['POST'])
def convertir_temperatura():
    """
    Endpoint para convertir temperaturas de Celsius a Fahrenheit y Kelvin usando modelos de IA.
    """
    # 1. Obtener los datos (debería ser un JSON con {"celsius": 25})
    try:
        data = request.get_json()
        temp_c = float(data.get('celsius'))
    except Exception:
        return jsonify({"error": "Formato de entrada inválido. Se esperaba un JSON con 'celsius'."}), 400

    # Validación extra: rango lógico de temperatura
    if not (-100 <= temp_c <= 1000):
        return jsonify({"error": "La temperatura debe estar entre -100°C y 1000°C."}), 400

    # 2. Realizar las predicciones con los modelos de IA
    celsius_input = np.array([temp_c])
    f_pred = MODELO_F.predict(celsius_input)[0][0]
    k_value = temp_c + 273.15  # Conversión directa

    resultado = {
        "celsius": float(temp_c),
        "fahrenheit": float(round(f_pred, 2)),
        "kelvin": float(round(k_value, 2))
    }
    return jsonify(resultado)

@app.route('/')
def index():
    """Sirve la página principal (el frontend)."""
    return render_template('index.html')

# Iniciar el servidor Flask
if __name__ == '__main__':
    print("\n🚀 Iniciando API y Frontend en http://127.0.0.1:5000/")
    app.run(debug=True)
