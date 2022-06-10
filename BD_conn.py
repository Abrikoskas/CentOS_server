import psycopg2 as pg


# def bd_func(settings):
#     def retry_decorator(func):
#         def _wrapper(*args, **kwargs):
#             try:
#                 with pg.connect(dbname=settings['dbname'], user=settings['user'],
#                                 password=settings['password'], host=settings['host']) as conn:
#                     with conn.cursor() as cursor:
#                         func(*args, **kwargs, cursor=cursor)
#             except Exception as e:
#                 return f"Connection to db failed, {e}"
#         return _wrapper
#     return retry_decorator
#
#
# def decorator(func):
#     def _wrapper(*args, **kwargs):
#         data = func(*args, **kwargs)
#     return _wrapper
def get_cursor():
    conn = pg.connect(dbname='ISAK', user='postgres', password='0801', host='localhost')
    conn.autocommit = True
    cursor = conn.cursor()
    return cursor


def get_data(cursor):
    cursor.execute(f"SELECT * FROM public.main")
    return cursor.fetchall()


def add_data(cursor, data):
    return cursor.execute(f'INSERT INTO public.main("Name", phone_number) VALUES (\'{data[0]}\', \'{data[1]}\');')
