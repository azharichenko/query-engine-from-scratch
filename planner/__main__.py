from psqlparse2 import query_to_pb


QUERY = "WITH base AS (SELECT * FROM data) SELECT * FROM base"

print(query_to_pb(QUERY))