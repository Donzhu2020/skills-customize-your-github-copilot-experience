# FastAPI REST API Starter Code
# Complete this code to build a book management API

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# TODO: Define the Book model using Pydantic BaseModel
# Fields: id (int), title (str), author (str), year (int), isbn (str)
class Book(BaseModel):
    pass  # Replace with your implementation


# In-memory database (list to store books)
books_db: List[Book] = []


# TODO: Implement root endpoint
@app.get("/")
async def root():
    pass  # Replace with your implementation


# TODO: Implement health check endpoint
@app.get("/health")
async def health_check():
    pass  # Replace with your implementation


# TODO: Implement endpoint to get all books (with optional filters)
@app.get("/books/")
async def get_books(
    author: Optional[str] = None,
    year: Optional[int] = None
):
    pass  # Replace with your implementation


# TODO: Implement endpoint to get a specific book by ID
@app.get("/books/{book_id}")
async def get_book(book_id: int):
    pass  # Replace with your implementation


# TODO: Implement endpoint to create a new book
@app.post("/books/", status_code=201)
async def create_book(book: Book):
    pass  # Replace with your implementation


# TODO: Implement endpoint to update an existing book
@app.put("/books/{book_id}")
async def update_book(book_id: int, book: Book):
    pass  # Replace with your implementation


# TODO: Implement endpoint to delete a book
@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    pass  # Replace with your implementation


# To run this application, use the command:
# uvicorn starter-code:app --reload
