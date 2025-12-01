document.getElementById('conversionForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Detiene el envío normal del formulario

    const celsius = document.getElementById('celsiusInput').value;

    // La URL debe coincidir con el endpoint de tu API en app.py
    const API_URL = 'http://127.0.0.1:5000/convertir';

    fetch(API_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ celsius: parseFloat(celsius) })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Error HTTP: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        // Actualizar la interfaz de usuario con los resultados de la API
        document.getElementById('resultFahrenheit').textContent = data.fahrenheit;
        document.getElementById('resultKelvin').textContent = data.kelvin;
    })
    .catch(error => {
        console.error('Error al llamar a la API:', error);
        alert('Hubo un error al conectar con la API: ' + error.message);
    });
});