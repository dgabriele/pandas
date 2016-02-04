As I understand it, the Pandas workflow is like this:

1. Read data from a file, SQL database, or other source, creating an initial set of DataFrames. A DataFrame is a 2D datastructure in pandas.
2. Transform initial DataFrames -- either in-place or through one or more intermediate DataFrames -- into a final DataFrame.
3. Write said final DataFrame back to a file or SQL database table.
