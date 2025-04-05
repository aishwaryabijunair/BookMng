from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    copies: int

class BorrowBook(BaseModel):
    title: str
    author: str

class ReturnBook(BaseModel):
    book_id: int

class DeleteBook(BaseModel):
    book_id: int