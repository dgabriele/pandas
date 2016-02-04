import sqlalchemy as sa


def init_test_database():
    """ Create a test users table.
    """
    engine = sa.create_engine('postgresql+psycopg2://postgres@localhost/test')
    with engine.connect() as conn:
        conn.execute("""
                     CREATE TABLE IF NOT EXISTS users (
                        id SERIAL PRIMARY KEY,
                        name TEXT,
                        age INTEGER
                     );
                     """)
        conn.execute("DELETE FROM users;")
        for args in [('daniel', 31), ('emily', 24), ('mom', 58)]:
            conn.execute("INSERT INTO users (name, age) VALUES ('{}', {});".format(*args))
    return engine
