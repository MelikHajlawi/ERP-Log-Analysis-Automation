# database.py
# This module contains functions for testing the database connection and retrieving data from SQL Server.

from sqlalchemy.exc import OperationalError
from sqlalchemy import text
from config import get_engine

# Initialize SQLAlchemy engine
engine = get_engine()

def test_connection(engine):
    """
    Tests database connection by executing a simple query.
    Prints 'Connexion réussie!' if successful.
    """
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            for row in result:
                print(row)
        print("Connexion réussie!")
    except OperationalError as e:
        print(f"Erreur de connexion : {e}")

def get_log_paths():
    """
    Fetches server, instance, database, and log path information from 'parametrage' table.
    Returns a list of tuples containing these details.
    """
    with engine.connect() as connection:
        result = connection.execute(text("SELECT serveur, instance, base, log_path FROM parametrage"))
        return result.fetchall()

def get_last_log_id():
    """
    Retrieves the maximum log_id from the 'backup_log_summary' table for tracking log entries.
    Returns 0 if no log entries exist.
    """
    with engine.connect() as connection:
        result = connection.execute(text("SELECT MAX(log_id) FROM backup_log_summary"))
        return result.scalar() or 0
 
