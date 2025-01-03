# TheProject

# Django API with Posts and Comments

This project is a Django-based backend API that retrieves a list of posts, each with up to three of their latest comments. The API is built using the Django REST framework and includes detailed features for handling models, serializers, and views.

## Project Structure

The project consists of the following main components:

### Directory Structure
```
backend_repo/
|— apps/
|   |— demo/
|       |— __init__.py
|       |— models.py
|       |— serializers.py
|       |— views.py
|       |— admin.py
|— demo_project/
    |— __init__.py
    |— settings.py
    |— urls.py
    |— wsgi.py
    |— asgi.py
```

### Key Files

#### `models.py`
Defines the `Post` and `Comment` models:
- **Post**: Contains fields like `id`, `text`, `timestamp`, and `user`.
- **Comment**: Contains fields like `id`, `text`, `timestamp`, `post`, and `user`.

#### `serializers.py`
Contains serializers to convert model instances into JSON format:
- **CommentSerializer**
- **PostSerializer**

#### `views.py`
Implements an API view `PostWithComments` to fetch posts along with their comments.

#### `urls.py`
Defines the routing for the API endpoints.

## API Endpoints

### GET `/api/posts/`
**Description**: Retrieves a list of posts, each with up to 3 of the latest comments.

#### Response Format
```json
[
    {
        "text": "Post text",
        "timestamp": "2023-12-27T15:00:00Z",
        "comment_count": 5,
        "user": "username",
        "comments": [
            {
                "text": "Comment text",
                "timestamp": "2023-12-27T15:10:00Z",
                "user": "commenter_username"
            },
            ... up to 3 comments ...
        ]
    }
]
```

## Installation and Setup

### Prerequisites
- Python 3.8+
- Django 4.x
- Django REST Framework

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd backend_repo
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the API at `http://127.0.0.1:8000/api/posts/`.

## Testing the API
Use tools like Postman or `curl` to test the `/api/posts/` endpoint:

### Example Test
```bash
curl -X GET http://127.0.0.1:8000/api/posts/
```

## Admin Panel
The Django admin interface is available at `http://127.0.0.1:8000/admin/` to manage posts and comments. Ensure models are registered in `admin.py`.

## Customization

### Fetch Random Comments
To fetch 3 random comments instead of the latest ones, update the query in `views.py`:
```python
comments = post.comments.order_by('?')[:3]  # Fetch 3 random comments
```

### Add Pagination
Integrate Django REST Framework's pagination to handle large datasets.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
Built using Django and Django REST Framework.


## Movie Info App Frontend
This project is a Vue.js-based frontend application built with Vite. It displays detailed movie information using data fetched from the OMDB API. The design and functionality are inspired by TMDB's interface, featuring a responsive layout, a hero section, movie details, and user interaction features.

## Features
Hero Section: Displays the movie poster, title, genre, release date, and rating with a gradient overlay.
Movie Details Section: Includes an overview, director, cast, runtime, and plot details.
Dynamic API Integration: Fetches movie data dynamically from the OMDB API.
Responsive Design: Fully responsive layout, adapting to screens of all sizes.
Modern Styling: Styled using Tailwind CSS and custom gradients.
## Table of Contents
Tech Stack
Setup Instructions
File Structure
Environment Variables
Scripts
Future Enhancements
## Tech Stack
Vue 3: Progressive JavaScript framework for building user interfaces.
Vite: Fast and modern frontend build tool.
Axios: Promise-based HTTP client for making API requests.
Tailwind CSS: Utility-first CSS framework for responsive and modern styling.
## Setup Instructions
Prerequisites
Ensure you have the following installed:

Node.js (v16 or higher)
npm or yarn
Steps
Clone the repository:

bash
Copy code
```git clone https://github.com/your-username/movie-info-app.git```
```cd movie-info-app```
```Install dependencies:``

```bash```
Copy code
```npm install```
Start the development server:

bash
Copy code
```npm run dev```
Open your browser and navigate to http://localhost:5173.

## File Structure
bash
Copy code
movie-info-app/
├── public/
├── src/
│   ├── assets/          # Static assets like images and styles
│   ├── components/      # Reusable Vue components (e.g., NavBar, MovieDetails)
│   ├── views/           # Page-specific components
│   ├── App.vue          # Root Vue component
│   ├── main.js          # Application entry point
│   └── styles.css       # Global CSS file
├── .env                 # Environment variables (API keys, etc.)
├── package.json         # Project metadata and dependencies
├── tailwind.config.js   # Tailwind CSS configuration
└── vite.config.js       # Vite configuration
## Environment Variables
The application fetches data from the OMDB API. Create a .env file in the root directory and add your API key:

env
Copy code
VITE_OMDB_API_KEY=your-api-key-here
Make sure to replace your-api-key-here with your actual OMDB API key.

Scripts
Command	Description
```npm run dev```	Starts the development server.
```npm run build```	Builds the app for production.
```npm run serve```	Serves the production build locally.
```npm run lint```	Runs the linter to check code quality.
## Future Enhancements
Add Dropdown Menus: Implement dropdown menus in the navbar for better navigation.
Search Functionality: Allow users to search for movies, TV shows, and actors.
User Authentication: Add login and sign-up functionality for personalized user experiences.
Theme Customization: Add light/dark mode toggle for improved UX.
Error Handling: Enhance error handling for API failures or network issues.
Contributing
Feel free to submit issues or pull requests to improve this project. Contributions are always welcome!



## Acknowledgments
OMDB API: For providing movie data.
TMDB: For design inspiration.
