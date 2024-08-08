**ПРОЕКТ ТРЕКЕР ПОЛЕЗНЫХ ПРИВЫЧЕК С ИСПОЛЬЗОВАНИЕМ DRF.**

**Описание**
Трекер полезных привычек. Создайте привычку и Вы будете получать уведомление о ней в телеграм


**Технологии**

- Python
- Django
- DRF
- PostgreSQL
- Redis
- Celery

**Для работы с проектом необходимо.**  
- Клонировать репозиторий на компьютер используя SSH ключ.
- Создать зависимости, выполнив команду poetry install.
- В файл .env внесите свои данные (необходимые переменные перечислены в файле .env.sample)
- создайте и примените мигации (python manage.py makemigrations, python manage.py migrate)
- установите Redis, запустите командой redis-server
- для запуска проекта наберите в терминале команду python manage.py runserver
- программе Postman, в админке зарегистрируйтесь и создайте привычки
- в терминале запустите celery worker командой:
  celery -A config worker -l INFO  # для Mac и Linux
  celery -A config worker -l INFO -P eventlet  # для Windows
- в другом терминале запустите celery beat командой:
  celery -A config beat -l info -S django
