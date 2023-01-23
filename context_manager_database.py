"""This is my own context manager to database"""


class Database:
    """This is class of context manager."""
    def __init__(self, connection):
        self.connection = connection
        self.cursor = None

    def __enter__(self):
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if isinstance(exc_val, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()

        self.connection.close()
