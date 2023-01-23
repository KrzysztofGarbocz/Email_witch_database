"""This is borrowers module
In this module am use database"""

from collections import namedtuple
from context_manager_database import Database
Entity = namedtuple('Entity', 'email name date_return_at')


def set_up_database(connect):
    """
    Create table in file database
    :param connect: handle to connection database
    :type connect: connect
    """
    with Database(connect) as database:
        database.cursor.execute("""
        CREATE TABLE borrows (id INTEGERS PRIMARY KEY AUTOINCREMENT, Email TEXT NOT NULL, Name TEXT NOT NULL, 
        Return_at DATE NOT NULL)""")


def get_borrows_by_return(connect, return_at):
    """
    Get all borrowers from database, who deadlines is end.
    :param connect: handle to connection database
    :type connect: connect
    :param return_at: present date
    :type return_at: '2023-01-01'
    :return: email , name, date_return_at
    :rtype: namedtuple
    """
    entity = []
    with Database(connect) as database:
        database.cursor.execute("""
        SELECT Email, Name, Return_at WHERE Return_at < ?
        """, (return_at,))
        for email, name, date_return_at in database.cursor.fetchall():
            entity.append(Entity(email, name, date_return_at))
        return entity
