# config.py
# This module sets up the database connection configuration and returns an SQLAlchemy engine.

from sqlalchemy import create_engine

# Database server details
SERVER = 'confid'
DATABASE = 'confid'

# Connection string for SQL Server using Trusted Connection
CONNECTION_STRING = (
    f"mssql+pyodbc://@{SERVER}/{DATABASE}?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes"
)

def get_engine():
    """
    Initializes and returns a SQLAlchemy engine for database connection.
    """
    return create_engine(CONNECTION_STRING)
 
