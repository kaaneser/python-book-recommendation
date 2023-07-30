# Book Recommendation System 📚

This repository contains a Python web application that recommends books based on user queries using the Google Books API. The application allows users to search for books by title, genre, or a simple query and provides random book recommendations from the query result.

## Prerequisites

Before running the web application, make sure you have the following prerequisites:

- Python 3 installed
- Flask module installed (you can install it using `pip install Flask`)
- requests module installed (you can install it using `pip install requests`)

## Usage

To run the web application, follow these steps:

1. Clone the repository to your local machine.
2. Open a command-line interface.
3. Navigate to the cloned repo's directory.
4. Run the following command:
```python app.py```
5. Open your web browser and visit `http://127.0.0.1:5000/`.
6. Enter your book title, genre, or a simple query in the provided input fields.
7. Click on the "Get Recommendation" button.
8. The web application will retrieve book recommendations based on your query and display them along with book details, including the book title, author, image, retail price (if available), and a "Buy Now" link (if available).

## To-Do's 🏁

1. Improve error handling for invalid queries and API responses.
2. Enhance the web application's user interface with more appealing design and responsiveness.
3. Implement unit tests for different components of the web application.
4. Add support for pagination to handle large result sets from the Google Books API.
5. Explore options to incorporate authentication if necessary to access certain API endpoints.
6. Optimize code modularity and organization.
7. Implement caching mechanism to store and reuse book data for faster responses.
8. Allow users to view more details about a book by clicking on its title or image.
9. Add a search history feature to remember previous queries.