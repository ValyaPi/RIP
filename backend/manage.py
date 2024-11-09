#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.db import connections
from django.db.utils import OperationalError
import time

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rip_desk.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    if "runserver" in sys.argv:
        
        while True:
            try:
                # Проверка подключения к базе данных
                db_conn = connections['default']
                db_conn.cursor()
                break
            except OperationalError:
                print("Reconnecting to db")
                time.sleep(1)
        
        execute_from_command_line(["manage.py", "makemigrations"])
        execute_from_command_line(["manage.py", "migrate"])
        

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
