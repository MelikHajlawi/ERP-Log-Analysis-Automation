# data_insertion.py
# This module provides a function to insert data into the SQL database with progress tracking.

from sqlalchemy.exc import IntegrityError

def insert_logs_with_progress(df, table_name, engine, chunk_size=10):
    """
    Inserts DataFrame records into SQL database in chunks to handle large datasets.
    Skips duplicate entries in case of IntegrityError.
    """
    for i in range(0, len(df), chunk_size):
        chunk = df.iloc[i:i + chunk_size]
        try:
            chunk.to_sql(name=table_name, con=engine, if_exists='append', index=False)
            print(f'Inserted chunk {i // chunk_size + 1} into {table_name}')
        except IntegrityError as e:
            print(f'IntegrityError occurred: {e.orig}. Skipping duplicate entries.')
 
