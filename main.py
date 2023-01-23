"""Main assembly mail and database"""
import sqlite3
import datetime
from borrowers import Borrowers
import sender_mail


if __name__ == '__main__':

    connection = sqlite3.connect('database.db')
    obj = Borrowers()
    borrow = obj.get_borrows_by_return(connection, datetime.datetime.today().strftime('%Y-%m-%d'))
    for email, name, item, return_at in borrow:
        sender_mail.Sender().send(email, name, item, return_at)
