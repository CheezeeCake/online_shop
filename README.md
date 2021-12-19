# Проект онлайн-магазина
1) Для запуска проекта необходимо перейти в рабочую папку: 
   - cd online_shop 

3) Уставновим зависимости и сделаем миграции: 
   - pip install -r requirements.txt
   - python manage.py makemigrations
   - python manage.py migrate

2) Выполняем запуск серрвера: 
   - python manage.py runserver
   
3) Для просмотра админки в адресной строке дописывыем: 
   - /admin
   
### Данные для входа в админку

- логин: admin
- пароль: admin