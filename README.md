# Проект онлайн-магазина

## Руководство по запуску проекта:

1) Для запуска проекта необходимо активировать виртуальное окружение:
   - `python3 -m venv venv`
   - `source venv/bin/activate`  

2) Перейти в рабочую папку:
   - `cd online_shop` 

3) Установить зависимости и сделать миграции: 
   - `pip install -r requirements.txt`
   - `python manage.py migrate`

4) Выполить запуск сервера: 
   - `python manage.py runserver`
   
5) Для просмотра админки в адресной строке дописать: 
   - /admin
   
### Данные для входа в админку

- логин: admin
- пароль: admin

## Руководство по запуску проекта через Docker:

1) Необходимо собрать и запустить контейнер с приложением:  
   - `docker build -t online_shop .`
   - `docker run -it -p 8000:8000 online_shop:latest`

2) Перейти по адресу http://127.0.0.1:8000/ или http://localhost:8000/