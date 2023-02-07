Как запустить:

`` git clone https://github.com/Korwys/microservice-app.git``

``cd src``

``python3 -m venv venv`` For Linux
``python -m venv venv`` For Windows

``source /venv/bin/activate`` For Linux
`` .\venv\Scripts\activate`` For Windows

``pip install -r requirements.txt``

``docker run -d --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres``

``python3 main.py`` For Linux
``python main.py`` For Windows

``pytest -v`` - Тесты рекомендуется запускаться на свежую базу данных. Так как, тесты завязаны с основной БД и в
случае добавления новых товаров, либо добавления товаров в корзину, часть тестов упадет, так как, измениться итоговый
список товаров/корзины.


CURL:

1) Добавить новый товар

``curl -X 'POST' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{ "name": "Lenovo", "price": 909090 }' 'http://0.0.0.0:8080/api/product/' ``

2) Поиск товара по названию:

``curl -X 'POST' -H 'accept: application/json' -H 'Content-Type: application/json' -d'{"keyword":"lenovo","price_sorted":"default","name_sorted": "default"}' 'http://0.0.0.0:8080/api/product/search' ``

3) Добавить товар в корзину:

``curl -X 'POST' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"product": 10,"quantity": 1}' 'http://0.0.0.0:8080/api/cart/add' ``

4) Изменить количество товара в корзине:

``curl -X 'PATCH' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"product": 10,"quantity": 120}' 'http://0.0.0.0:8080/api/cart/update_quantity' ``

5) Получить список товаров в корзине:

``curl -X 'GET' -H 'accept: application/json' 'http://0.0.0.0:8080/api/cart/' ``

