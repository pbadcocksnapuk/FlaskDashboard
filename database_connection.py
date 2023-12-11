import psycopg2
from decouple import config


user = config("DB_USER")
pwd = config("DB_PASS")
host = config("DB_SERVER")
port = config("DB_PORT")
db_name = config("DB_NAME")


def pull_query(sql=None, db=None):
    """
    @param sql:
    @param db:
    @return:
    """

    if sql is None or db is None:
        raise Exception("arguments are missing")
    else:
        try:
            with psycopg2.connect(host=host, port=port, database=db_name, user=user, password=pwd) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
                    cols_data = cur.description  # extracting 1st row to get data types and column names
                    result = []
                    for row in cur:
                        result.append(row)
        # except ValueError as e :
        #     print(f"Value error occured, but the program continues to work\n{e}")
        except psycopg2.OperationalError as e:
            # Handle the specific SSL connection closure exception
            print(f"An SSL connection error occurred: {e}")
            print(f"But the program continues to work (hopefully)")
        except psycopg2.Error as e:
            print(f"Error: {e}")
            raise Exception(e)

        return cols_data, result


# def pull_large_query(sql=None, db=None):
#     """
#     @param sql:
#     @param db:
#     @return:
#     """
#     if sql is None or db is None:
#         raise Exception("arguments are missing")
#     else:
#         # Create temporary table with the data results
#         table_name = "snapanalytics.large_temp_table_" + get_random_id(10)
#         create_query = f"""--LARGE SELECT QUERY AS TABLE
#         CREATE TABLE {table_name} AS {sql}
#         """
#         try:
#             push_query(create_query, db)
#
#             result = []
#             limit = 1000000
#             offset = 0
#             result_len = 0
#             while True:
#                 select_query = f"""--LARGE SELECT QUERY DIVIDED INTO PARTS
#                 SELECT *
#                 FROM {table_name}
#                 OFFSET {offset}
#                 LIMIT {limit};
#                 """
#
#                 try:
#                     with psycopg2.connect(host=host, port=port, database=db_name, user=user, password=pwd) as conn:
#                         with conn.cursor() as cur:
#                             cur.execute(select_query)
#                             cols_data = cur.description  # extracting 1st row to get data types and column names
#
#                             for row in cur:
#                                 result.append(row)
#
#                             if result_len == len(result):
#                                 break
#                             else:
#                                 result_len = len(result)
#                                 offset += limit
#
#                 # except ValueError as e :
#                 #     print(f"Value error occured, but the program continues to work\n{e}")
#                 except psycopg2.OperationalError as e:
#                     # Handle the specific SSL connection closure exception
#                     print(f"An SSL connection error occurred: {e}")
#                     print(f"But the program continues to work (hopefully)")
#                 except psycopg2.Error as e:
#                     print(f"Error: {e}")
#                     raise Exception(e)
#         finally:
#             # remove temp table
#             drop_query = f"""
#             DROP TABLE IF EXISTS {table_name};
#             """
#             push_query(drop_query, db)
#
#         return cols_data, result


def push_query(sql=None, db=None):
    """
    @param sql:
    @param db:
    @return:
    """

    if sql is None or db is None:
        raise Exception("arguments are missing")
    else:
        try:
            with psycopg2.connect(host=host, port=port, database=db_name, user=user, password=pwd) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
        except psycopg2.Error as e:
            print(f"Error: {e}")
            raise Exception(e)
