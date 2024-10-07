from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")  # Replace with your API key
SPOONACULAR_API_URL = "https://api.spoonacular.com/recipes/findByIngredients"

@app.route('/get_recipes', methods=['POST'])
def get_recipes():
    data = request.json
    ingredients = data.get('ingredients')

    if not ingredients:
        return jsonify({'error': 'No ingredients provided'}), 400

    # Call Spoonacular API
    response = requests.get(SPOONACULAR_API_URL, params={
        'ingredients': ','.join(ingredients),
        'number': 5,
        'ranking': 1,
        'apiKey': SPOONACULAR_API_KEY
    })

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({'error': 'Failed to fetch recipes'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
