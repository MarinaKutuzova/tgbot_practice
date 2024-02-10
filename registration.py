from db.db_methods import *


def registrate_user(data: dict):
    """
    -> Записываем информацию о пользователе в БД
    :param data: словарь с данными о пользователе
    :return: 1 - пользователь зарегестрирован, 0 - успешно
    """
    if data.get('usersurname') and data.get('username') and data.get('tgid'):
        registrate_user_db(data.get('tgid'), data.get('usersurname'), data.get('username'))
    return 0




