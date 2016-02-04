""" Pandas IO Examples
    http://pandas.pydata.org/pandas-docs/stable/io.html
"""

import pandas as pd

from db_utils import init_test_database


engine = init_test_database()
with engine.connect() as conn, conn.begin():
    # read the whole table into a Pandas DataFrame object
    # see: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_sql_table.html
    data = pd.read_sql_table('users', conn)
    print('-' * 60)
    print(data)

    # read the result table of a query into a DataFrame
    # see: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_sql_query.html
    query = 'SELECT name, age FROM users WHERE age < 50'
    data = pd.read_sql_query(query, conn)
    print('-' * 60)
    print(data)

    # write DataFrame object back to users table
    # see: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_sql.html
    data.to_sql('users', conn, chunksize=1000, if_exists='append', index=False)
    data = pd.read_sql_table('users', conn)
    print('-' * 60)
    print(data)



