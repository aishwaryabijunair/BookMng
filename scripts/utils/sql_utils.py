import psycopg2
from psycopg2 import OperationalError
from psycopg2.extras import RealDictCursor
from scripts.configurations.configurations import Database
from scripts.utils.logging import setup_logger

logger = setup_logger(name="util_func")

class DatabaseConnection:
    def __init__(self):
        """Constructor: Initialize database connection."""
        try:
            self.conn = psycopg2.connect(
                dbname=Database.database_name,
                user=Database.username,
                password=Database.password,
                host=Database.host,
                port=Database.port
            )
            self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)
            logger.info(f"Connected to database {Database.database_name}")
        except OperationalError as e:
            logger.error(f"Database connection failed: {e}")
            raise Exception(f"Database connection failed: {e}")
        except Exception as e:
            logger.error("Unexpected error occurred", exc_info=True)
            raise Exception(f"Unexpected error during connection: {e}")

    def close(self):
        """Destructor: Close cursor and connection."""
        if hasattr(self, 'cursor') and self.cursor:
            self.cursor.close()
        if hasattr(self, 'conn') and self.conn:
            self.conn.close()
            logger.info("Database connection closed.")



class DatabaseUtility:
    def __init__(self):
        self.db = DatabaseConnection()

    def close(self):
        self.db.close()

    def get_records(self, table: str, condition: str = None, params: tuple = ()):
        """Retrieve records from any table with optional conditions."""
        try:
            query = f"SELECT * FROM {table}"
            if condition:
                query += f" WHERE {condition}"
            self.db.cursor.execute(query, params)
            return self.db.cursor.fetchall()
        except Exception as e:
            logger.error(f"Error fetching records from {table}: {e}")
            return None

    def insert_record(self, table: str, data: dict):
        """Insert a new record into any table."""
        try:

            query = f"INSERT INTO {table} ({', '.join(data.keys())}) VALUES ({', '.join(['%s'] * len(data))})"
            self.db.cursor.execute(query, tuple(data.values()))
            self.db.conn.commit()
            return self.db.cursor.fetchone()
        except Exception as e:
            logger.error(f"Error inserting record into {table}: {e}")
            return None

    def update_record(self, table: str, updates: str, condition: str, params: tuple):
        """Update records in any table based on conditions."""
        try:
            query = f"UPDATE {table} SET {updates} WHERE {condition} RETURNING *"
            self.db.cursor.execute(query, params)
            self.db.conn.commit()
            return self.db.cursor.fetchone()
        except Exception as e:
            logger.error(f"Error updating record in {table}: {e}")
            return None

    def delete_record(self, table: str, condition: str, params: tuple):
        """Delete records from any table based on conditions."""
        try:
            query = f"DELETE FROM {table} WHERE {condition} RETURNING *"
            self.db.cursor.execute(query, params)
            self.db.conn.commit()
            return self.db.cursor.fetchone()
        except Exception as e:
            logger.error(f"Error deleting record from {table}: {e}")
            return None
