"""
Enunciado:
Desarrolla una aplicación web con Flask que demuestre diferentes formas de acceder a la
información enviada en las solicitudes HTTP. Esta aplicación te permitirá entender cómo
procesar diferentes tipos de datos proporcionados por los clientes.

Tu aplicación debe implementar los siguientes endpoints:

1. `GET /headers`: Devuelve los encabezados (headers) de la solicitud en formato JSON.
   - Muestra información como User-Agent, Accept-Language, etc.

2. `GET /browser`: Analiza el encabezado User-Agent y devuelve información sobre:
   - El navegador que está usando el cliente
   - El sistema operativo
   - Si es un dispositivo móvil o no

3. `POST /echo`: Acepta cualquier tipo de datos y devuelve exactamente los mismos datos
   en la misma forma que fueron enviados. Debe manejar:
   - JSON
   - Datos de formulario (form data)
   - Texto plano

4. `POST /validate-id`: Valida un documento de identidad según estas reglas:
   - Debe recibir un JSON con un campo "id_number"
   - El ID debe tener exactamente 9 caracteres
   - Los primeros 8 caracteres deben ser dígitos
   - El último carácter debe ser una letra
   - Devuelve JSON indicando si es válido o no

Esta actividad te enseñará cómo acceder y manipular datos de las solicitudes HTTP,
una habilidad fundamental para crear APIs robustas y aplicaciones web interactivas.
"""

from flask import Flask, jsonify, request
import re

def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    @app.route('/headers', methods=['GET'])
    def get_headers():
        """
        Devuelve los encabezados (headers) de la solicitud en formato JSON.
        Convierte el objeto headers de la solicitud en un diccionario.
        """
        # Implementa este endpoint:
        # 1. Accede a los encabezados de la solicitud usando request.headers
        # 2. Convierte los encabezados a un formato adecuado para JSON
        # 3. Devuelve los encabezados como respuesta JSON



    @app.route('/browser', methods=['GET'])
    def get_browser_info():
        """
        Analiza el encabezado User-Agent y devuelve información sobre el navegador,
        sistema operativo y si es un dispositivo móvil.
        """
        # Implementa este endpoint:
        # 1. Obtén el encabezado User-Agent de request.headers
        # 2. Analiza la cadena para detectar:
        #    - El nombre del navegador (Chrome, Firefox, Safari, etc.)
        #    - El sistema operativo (Windows, macOS, Android, iOS, etc.)
        #    - Si es un dispositivo móvil (detecta cadenas como "Mobile", "Android", "iPhone")
        # 3. Devuelve la información como respuesta JSON
        pass

    @app.route('/echo', methods=['POST'])
    def echo():
        """
        Devuelve exactamente los mismos datos que recibe.
        Debe detectar el tipo de contenido y procesarlo adecuadamente.
        """
        # Implementa este endpoint:
        # 1. Detecta el tipo de contenido de la solicitud con request.content_type
        # 2. Según el tipo de contenido, extrae los datos:
        #    - Para JSON: usa request.get_json()
        #    - Para form data: usa request.form
        #    - Para texto plano: usa request.data
        # 3. Devuelve los mismos datos con el mismo tipo de contenido
        pass

    @app.route('/validate-id', methods=['POST'])
    def validate_id():
        """
        Valida un documento de identidad según reglas específicas:
        - Debe tener exactamente 9 caracteres
        - Los primeros 8 caracteres deben ser dígitos
        - El último carácter debe ser una letra
        """
        # Implementa este endpoint:
        # 1. Obtén el campo "id_number" del JSON enviado
        # 2. Valida que cumpla con las reglas especificadas
        # 3. Devuelve un JSON con el resultado de la validación
        pass

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
