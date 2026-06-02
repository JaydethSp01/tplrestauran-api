import os
from psycopg import connect
def get_db():
    url = os.environ.get("DATABASE_URL")
    if url:
        return connect(url)
        return None
