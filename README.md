**Структура кода**

![image](https://github.com/MarinaKutuzova/tgbot_practice/assets/129587090/596487df-1cae-4461-8a38-4d6f61ec6199)
1. db включает в себя:
   - database.db - БД
   - db_core.py - Методы для select, insert с SQLite(добавьте Update)
   - db_methods.py - Методы для взаимодействия с БД в рамках предметной области
2. main.py - содержит основную логику работы с ботом (диспатчер, хендлеры)
3. registration.py - методы для регистрации
4. services.py - методы для работы с сервисами
5. task.py - методы для работы с заявками

**Начало работы**
1. Создайте виртуальное окружение проекта и выполните pip install requirements.txt для установки необходимы зависимостей
2. В корне проекта создайте файл .env и поместите свой токен с префиксом TOKEN=ВАШ ТОКЕН
3. Для получения архитектуры БД откройте database.db в поддерживаемом редакторе ( например, DB Browser for SQLite )

**Полезные ссылки**
1. Ссылка на презентацию - https://docs.google.com/presentation/d/1Fb_Am8ln0HdKN3y42yssVmCu8uwB4NK0LkJngDF0uu0/edit?usp=sharing
2. Установка DB Browser for SQLite - https://sqlitebrowser.org/dl/
3. Документация aiogram - https://aiogram.dev/

**Результат работы**

![img-0437_bFl78XSF](https://github.com/MarinaKutuzova/tgbot_practice/assets/129587090/3366ec56-6f08-4793-ad37-cd5d4e608b40)


