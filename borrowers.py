"""This is borrowers module
In this module am use database"""
from collections import namedtuple
from context_manager_database import Database
Entity = namedtuple('Entity', 'email name item date_return_at')


class Borrowers:
    """Class borrower
    Methods: set_up database - crate empty table
    Methods: get_borrows_by_return - Get all borrowers from database, who deadlines is end.
    Methods:  add_borrows - add borrowers to database
    """
    @staticmethod
    def set_up_database(set_connect):
        """
        Create table in file database
        :param set_connect: handle to connection database
        :type set_connect: connect
        """
        with Database(set_connect) as database:
            database.cursor.execute("""
            CREATE TABLE borrows (id INTEGER PRIMARY KEY AUTOINCREMENT, Email TEXT NOT NULL, Name TEXT NOT NULL, 
            Item Text NOT NULL, Return_at DATE NOT NULL)""")

    @staticmethod
    def get_borrows_by_return(get_connect, return_at):
        """
        Get all borrowers from database, who deadlines is end
        :param get_connect: handle to connection database
        :type get_connect: connect
        :param return_at: present date
        :type return_at: '2023-01-01'
        :return: email , name, date_return_at
        :rtype: namedtuple
        """
        entity = []
        with Database(get_connect) as database:
            database.cursor.execute("""
            SELECT Email, Name, Return_at WHERE Return_at < ?
            """, (return_at,))
            for email, name, item, date_return_at in database.cursor.fetchall():
                entity.append(Entity(email, name, item, date_return_at))
            return entity

    @staticmethod
    def add_borrows(add_connect, email, name, item, return_at):
        """
        Method to add borrows
        :param add_connect: sqlite
        :type add_connect: str
        :param email: email
        :type email: str
        :param name: name of borrows
        :type name:  name of borrows
        :param item: name of item
        :type item:  str
        :param return_at: data when have to return
        :type return_at:  str eg. '2023-02-25'
        """
        with Database(add_connect) as database:
            database.cursor.execute("SELECT id FROM borrows")
            try:
                actual_id = int(max(database.cursor.fetchall())[0])
                if actual_id > 0:
                    count = actual_id + 1
            except ValueError:
                count = 1

            database.cursor.execute("""
            INSERT INTO borrows VALUES (?, ? ,? ,?, ?)""", (count, email, name, item, return_at))

    @staticmethod
    def remove_borrows(add_connect, name, item):
        """
        Method to remove borrows
        :param add_connect: sqlite
        :type add_connect:  sqlite
        :param name:        name of borrows to remove from database
        :type name:         str
        :param item:        name of return item
        :type item:         str
        """
        with Database(add_connect) as database:
            database.cursor.execute('''DELETE FROM borrows \
            WHERE Name = ? AND Item = ?''', (name, item))
