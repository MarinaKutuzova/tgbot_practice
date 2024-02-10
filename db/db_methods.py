from db.db_core import *


def check_user_db(tgId):
    """
    -> Проверяем существует ли пользователь с таким tgId
    :param
    :return: возвращаем список найденных пользователей
    """
    return select_db(f'select * from users where tgId = {tgId}')


def registrate_user_db(tgId, userSurname, userName):
    """
    -> Регистрируем пользователя
    :param userSurname: Имя пользователя
    :param userName: Фамилия пользователя
    """
    insert_into_db('insert into users (tgId, userSurname, userName) VALUES (?, ?, ?)',
                   (tgId, userSurname, userName))


def get_services_db():
    """
    -> Получение сервисов для заявок
    :return: список сервисов
    """
    services_list = []
    services = select_db('select serviceName from services')
    for service in services:
        services_list.append(service[0])
    return services_list


def get_user_id_db(tgId):
    """
    -> Процедура для получения Id пользователя
    :param tgId: - тут и так все понятно :)
    :return: userId
    """
    return select_db(f'select Id from users where tgId = {tgId}')[0][0]


def get_service_id_db(serviceName):
    """
    -> Процедура для получения Id сервиса
    :param service_name: имя сервиса
    :return: serviceId
    """
    return select_db(f'select Id from services where serviceName = "{serviceName}"')[0][0]


def create_task_db(serviceId, createDate, creatorId, executorid, taskDescription, statusId):
    """
    -> Процедура для добавления заявки в таблицу
    :param serviceId: id сервиса
    :param createDate: дата создания заявки
    :param creatorId: id создателя заявки
    :param executorid: id исполнителя заявки
    :param taskDescription: Описание заявки
    :param statusId: Id статуса
    :return:
    """
    insert_into_db(
        'insert into tasks (serviceId, createDate, creatorId, executorid, taskDescription, statusId) VALUES (?, ?, ?, '
        '?, ?, ?)',
        (serviceId, createDate, creatorId, executorid, taskDescription, statusId))


def get_tasklist_db(tgid):
    """
    -> Процедура для получения списка заявок
    :param tgid:
    :return:
    """
    query = f"""select t.Id, serviceName, createDate, userName || ' ' || userSurname as fullName, taskDescription 
            from tasks t, users u, services s
            where 1=1
            and t.serviceId = s.Id
            and t.creatorId = u.Id
            and u.tgId = {tgid}"""
    return select_db(query)



