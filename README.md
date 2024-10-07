# Recipe Recommendation System 🍽️

### Overview

The **Recipe Recommendation System** is a Flask-based project that recommends recipes based on the ingredients you have at home. It is built using a microservices architecture and integrates with the Spoonacular API to fetch recipes dynamically. The system is containerized with Docker for easy deployment and scalability.

### Features

- 🛠️ **Microservices Architecture**: Ingredients and recipe management are separated into independent services using Flask.
- 🐳 **Docker**: Each service is containerized, making it easy to deploy and scale.
- 🔍 **Recipe Recommendations**: Based on the ingredients you have, it fetches recipes dynamically using the Spoonacular API.
- 🔑 **Secure API Handling**: Environment variables are used to securely manage API keys.

### Technologies Used

- **Python 3.9**
- **Flask** for building microservices
- **Spoonacular API** for fetching recipes
- **Docker** for containerization
- **Requests** for handling API calls

### Project Structure

```
recipe_microservice/
├── ingredients_service/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── app.py
├── recipe_service/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── app.py
└── docker-compose.yml
```

### Setup Instructions

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/recipe-recommendation-system.git
   cd recipe-recommendation-system
   ```

2. Set up the environment variables:

   - Create a `.env` file in the root of the project and add your Spoonacular API key:
     ```bash
     SPOONACULAR_API_KEY=your_spoonacular_api_key
     ```

3. Build the Docker containers:

   ```bash
   docker-compose build
   ```

4. Run the containers:

   ```bash
   docker-compose up
   ```

5. To test the system, you can use the following example `curl` command:
   ```bash
   curl -X POST http://localhost:5000/ingredients -H "Content-Type: application/json" -d '{"ingredients": ["tomato", "cheese", "bread"]}'
   ```

### Future Improvements

- Adding user authentication for personalized recipe recommendations.
- Storing recipe history for better suggestions.
- Expanding the ingredient database for more diverse recipes.

### Contributing

Feel free to fork this project, submit issues, and create pull requests. Any contributions are welcome!

### License

This project is licensed under the MIT License.
