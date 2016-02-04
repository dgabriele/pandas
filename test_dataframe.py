""" Pandas DataFrame Examples
    http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe

    - A dataframe is a 2D table-like data structure.
    - The positions or names of the row is called the "index".
"""

import pandas as pd

from db_utils import init_test_database


engine = init_test_database()
with engine.connect() as conn, conn.begin():
    users = pd.read_sql_table('users', conn)

    # you can index each columns like so.

    names = users['name']

    # the result is also an instance of DataFrame.

    print('These are the names:')
    print(names)
