from scripts.utils.sql_utils import DatabaseUtility
from scripts.models.model import BookCreate, BorrowBook, ReturnBook, DeleteBook
from scripts.utils.logging import logger


class CRUDOperations:
    def __init__(self):
        self.db_util = DatabaseUtility()

    def close(self):
        self.db_util.close()

    def add_book(self, book: BookCreate):
        try:
            self.db_util.insert_record("books", book.model_dump())
            logger.info("Book added: %s", book.title)
            return {"message": "Book added successfully", "title": book.title}
        except Exception as e:
            logger.error("Error adding book: %s", e)
            return {"error": "Failed to add book"}


    def get_books(self):
        try:
            books = self.db_util.get_records("books")
            logger.info("Fetched %d books", len(books))
            return {"message": "Books fetched successfully", "data": books}

        except Exception as e:
            logger.error("Error fetching books: %s", e)
            return {"error": "Failed to fetch books"}


    def borrow_book(self, book: BorrowBook):
        try:
            result = self.db_util.update_record("books", "copies = copies - 1", "title = %s AND author = %s AND copies > 0",
                (book.title, book.author)
            )
            if result:
                logger.info("Book borrowed: %s by %s", book.title, book.author)
                return {"message": "Book borrowed successfully", "title": book.title}
            else:
                logger.warning("Book not available for borrowing: %s by %s", book.title, book.author)
                return {"error": "Book not available"}
        except Exception as e:
            logger.error("Error borrowing book: %s", e)
            return {"error": "Failed to borrow book"}

    def return_book(self, book: ReturnBook):
        try:
            self.db_util.update_record("books", "copies = copies + 1", "book_id = %s", (book.book_id,))
            logger.info("Book returned: ID %s", book.book_id)
            return {"message": "Book returned successfully", "book_id": book.book_id}
        except Exception as e:
            logger.error("Error returning book: %s", e)
            return {"error": "Failed to return book"}

    def delete_book(self, book: DeleteBook):
        try:
            self.db_util.delete_record("books", "book_id = %s", (book.book_id,))
            logger.info("Book deleted: ID %s", book.book_id)
            return {"message": "Book deleted successfully", "book_id": book.book_id}
        except Exception as e:
            logger.error("Error deleting book: %s", e)
            return {"error": "Failed to delete book"}

