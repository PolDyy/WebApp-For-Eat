# WebApp-For-Eat
### находится в разработке

Данное приложение является одной из двух составляющих проекта For Eat.  
Его основная цель - формирование заказа клиентом и передача данных заказа в telegram-бота.
______________________

## Запуск проекта

1) Клонировать репозиторий и перейти в него в командной строке:
`git init`

`git clone https://github.com/PolDyy/WebApp-For-Eat.git`

2) Cоздать и активировать виртуальное окружение в корне проекта:

`python -m venv venv`

`source venv/Scripts/activate` или `source venv/bin/activate`


3) Установить зависимости:

`python -m pip install --upgrade pip`

`pip install -r requirements.txt`

4) Создаем файл .env на основе env_example.txt

5) Активируйте докерконтейнер:

   `docker compose up -d --build`

6) Все готов к запуску! 

Файл запуска приложения: app/runner.py  
