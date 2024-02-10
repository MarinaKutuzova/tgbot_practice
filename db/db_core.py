import sqlite3
db_config = {'db_name': './db/database.db'}


def select_db(query: str):
    """
    -> Метод селекта
    :param query: текст запроса
    :return: result список записей
    """
    connection = sqlite3.connect(db_config.get('db_name'))
    if connection:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()
        return result


def insert_into_db(query: str, data: tuple):
    """
    -> Метод вставки в таблицу
    :param query: текст запроса
    :param data: вставляемые значения
    :return:
    """
    connection = sqlite3.connect(db_config.get('db_name'))
    if connection:
        cursor = connection.cursor()
        print(f'{query=}')
        print(f'{data=}')
        cursor.execute(query, data)
        connection.commit()
        connection.close()
    return 0
