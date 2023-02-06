
Как запустить:

`` git clone https://github.com/Korwys/microservice-app.git``

- Pycharm

``Settings->Project>Add_Iterpreter->Path:/src``

``pip install -r requirements.txt``


- Linux

``cd src``

``python3 -m venv venv``

`` source /venv/bin/activate``

``pip install -r requirements.txt``

``docker run -d --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres``

``python3 main.py``

``pytest -v`` - Тесты рекомендуется запускаться на свежую базу данных. Так как, тесты функционируют с основной БД и в случае добавления новых товаров, либо добавления товаров в корзину, часть тестов упадет, так как, измениться итоговый список товаров/корзины.

- Windows(см. инструкцию для Linux, только вместо 'python3' используй 'python')'

CURL:

1) Добавить новый товар

``curl -X 'POST' \
  'http://0.0.0.0:3001/api/product/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Lenovo Test Phone",
  "price": 40000
}'``

2) Поиск товара по названию

``curl -X 'POST' \
  'http://0.0.0.0:3001/api/product/search' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "keyword": "lenovo test"
}'``




