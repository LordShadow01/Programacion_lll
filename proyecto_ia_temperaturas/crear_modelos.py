import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Datos de ejemplo para entrenar los modelos
celsius = np.array([-40, 0, 25, 100], dtype=float)
fahrenheit = np.array([-40, 32, 77, 212], dtype=float)
kelvin = np.array([233.15, 273.15, 298.15, 373.15], dtype=float)

# Modelo para convertir Celsius a Fahrenheit
model_f = Sequential([Dense(units=1, input_shape=[1])])
model_f.compile(optimizer='adam', loss='mean_squared_error')
model_f.fit(celsius, fahrenheit, epochs=500, verbose=0)
model_f.save('proyecto_ia_temperaturas/models/modelo_c_a_f.h5')
print('✅ Modelo Fahrenheit guardado en models/modelo_c_a_f.h5')

# Modelo para convertir Celsius a Kelvin
model_k = Sequential([Dense(units=1, input_shape=[1])])
model_k.compile(optimizer='adam', loss='mean_squared_error')
model_k.fit(celsius, kelvin, epochs=500, verbose=0)
model_k.save('proyecto_ia_temperaturas/models/modelo_c_a_k.h5')
print('✅ Modelo Kelvin guardado en models/modelo_c_a_k.h5')
