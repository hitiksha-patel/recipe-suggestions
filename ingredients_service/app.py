from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

RECIPE_SERVICE_URL = "http://recipe_service:5001/get_recipes"  # Recipe service URL (inside Docker)

@app.route('/ingredients', methods=['POST'])
def handle_ingredients():
    data = request.json
    ingredients = data.get('ingredients')

    if not ingredients:
        return jsonify({'error': 'No ingredients provided'}), 400

    # Forward ingredients to Recipe Service
    response = requests.post(RECIPE_SERVICE_URL, json={'ingredients': ingredients})

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({'error': 'Failed to fetch recipes'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
