from fastapi import APIRouter, HTTPException
from scripts.models.model import BookCreate, BorrowBook, ReturnBook, DeleteBook
from scripts.utils.logging import logger
from scripts.handlers import crud

router = APIRouter()
crud = crud.CRUDOperations()

@router.get("/books")
def get_all_books():
    try:
        return crud.get_books()
    except Exception as e:
        logger.exception(f"Error fetching books: {e}")
        raise HTTPException(status_code=500, detail="An internal error occurred.")

@router.post("/books")
def add_book(book: BookCreate):
    try:
        return crud.add_book(book)
    except Exception as e:
        logger.exception(f"Error adding book: {e}")
        raise HTTPException(status_code=500, detail="An internal error occurred.")

@router.put("/books/borrow")
def borrow_book(book: BorrowBook):
    try:
        return crud.borrow_book(book)
    except Exception as e:
        logger.exception(f"Error borrowing book: {e}")
        raise HTTPException(status_code=500, detail="An internal error occurred.")

@router.put("/books/return")
def return_book(book: ReturnBook):
    try:
        return crud.return_book(book)
    except Exception as e:
        logger.exception(f"Error returning book: {e}")
        raise HTTPException(status_code=500, detail="An internal error occurred.")

@router.delete("/books/{book_id}")
def delete_book(book_id: int):
    try:
        return crud.delete_book(DeleteBook(book_id=book_id))
    except Exception as e:
        logger.exception(f"Error deleting book: {e}")
        raise HTTPException(status_code=500, detail="An internal error occurred.")
