# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build professional REST APIs using the FastAPI framework. You will create a fully functional API with multiple endpoints, request validation, and proper HTTP methods to handle CRUD (Create, Read, Update, Delete) operations for a book management system.

## 📝 Tasks

### 🛠️	Create Basic FastAPI Application

#### Description
Set up a basic FastAPI application with a root endpoint and a health check endpoint. Install FastAPI and uvicorn server, then create your first API endpoints.

#### Requirements
Completed program should:

- Install FastAPI and uvicorn using pip
- Create a FastAPI application instance
- Implement a GET endpoint at `/` that returns a welcome message
- Implement a GET endpoint at `/health` that returns the API status
- Run the server successfully on localhost:8000


### 🛠️	Implement Book Management Endpoints

#### Description
Create a set of REST API endpoints to manage a collection of books. Use proper HTTP methods (GET, POST, PUT, DELETE) and implement data validation using Pydantic models.

#### Requirements
Completed program should:

- Define a Book model with fields: id, title, author, year, and isbn
- Implement POST `/books/` to add a new book
- Implement GET `/books/` to retrieve all books
- Implement GET `/books/{book_id}` to retrieve a specific book by ID
- Implement PUT `/books/{book_id}` to update an existing book
- Implement DELETE `/books/{book_id}` to remove a book
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Handle errors gracefully with proper error messages


### 🛠️	Add Query Parameters and Filtering

#### Description
Enhance your API by adding query parameters to filter and search books. Learn how to accept optional parameters and implement search functionality.

#### Requirements
Completed program should:

- Add optional query parameters to GET `/books/` endpoint (author, year)
- Filter books by author when `author` parameter is provided
- Filter books by publication year when `year` parameter is provided
- Support multiple filters simultaneously
- Return an empty list when no books match the filters

Example:
```
GET /books/?author=J.K. Rowling
GET /books/?year=2023
GET /books/?author=Isaac Asimov&year=1951
```
