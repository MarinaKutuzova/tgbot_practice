from db.db_methods import *
from datetime import datetime


def create_task(state_data):
    """
    -> Метод для создания заявки
    :param state_data: словарь с данными пользователя
    :return:
    """
    serviceId = get_service_id_db(state_data.get('servicename'))
    userId = get_user_id_db(state_data.get('tgid'))
    create_task_db(serviceId, datetime.now(), userId, None, state_data.get('taskdescription'), None)