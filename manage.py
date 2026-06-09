#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sqlite3
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')
    print("hello bro it api here")
    
    # try:
    #     db = sqlite3.connect("testcc.db")
    #     db_cursor = db.cursor()
    # except ConnectionError as con_err:
    #     raise ConnectionError (
    #         con_err
    #     )
    # print("database connected")
    # db_cursor.execute("SELECT * FROM employee")
    # row = db_cursor.fetchall()
    # for i in row:
    #     print(i)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
