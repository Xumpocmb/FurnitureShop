# Furniture Shop
01-31
Добро пожаловать в проект "Furniture Shop" – веб-приложение, разработанное с использованием Django 5.0 и Python 3.11 для создания удобного и приятного опыта покупок мебели для дома.

## Установка

1. Убедитесь, что у вас установлен Python 3.11.
2. Склонируйте репозиторий: `git clone https://github.com/Xumpocmb/FurnitureShop.git`
3. Перейдите в директорию проекта: `cd FurnitureShop`
4. Установите зависимости: `pip install -r requirements.txt`
5. for postgresql: `sudo apt install libpq5`

## БД
`sudo -i -u postgres`
`pasql`
`CREATE DATABASE FS_shop;`
`createuser --interactive`
`psql -d fs_shop -U xumpocmb`
`python3 manage.py loaddata fixtures/products.json`
`python3 manage.py loaddata fixtures/categories.json`
`DROP DATABASE fs_shop;`

## Запуск

1. Примените миграции: `python manage.py migrate`
2. Создайте административного пользователя: `python manage.py createsuperuser`
3. Запустите сервер разработки: `python manage.py runserver`

После этого, вы сможете открыть веб-браузер и перейти по адресу http://localhost:8000/ для доступа к приложению.

## Основные возможности

- Просмотр каталога мебели для дома.
- Фильтрация товаров по различным критериям.
- Добавление товаров в корзину.
- Оформление заказа с использованием корзины.
- Административный интерфейс для управления товарами и заказами.

## Технологии

- Django 5.0
- Python 3.11
- HTML, CSS, JavaScript (Bootstrap для стилей)
- SQLite (может быть изменено на другую базу данных)

## Вклад

Если у вас есть идеи или предложения по улучшению проекта, не стесняйтесь создавать issues или делать pull requests. Ваш вклад приветствуется!

## Лицензия

Этот проект распространяется под лицензией [MIT](LICENSE).

© 2023 FurnitureShop
