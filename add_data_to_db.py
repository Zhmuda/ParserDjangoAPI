import psycopg2
import pandas as pd
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Подключение к базе данных PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
)

# Создание курсора для выполнения SQL-запросов
cur = conn.cursor()

# SQL-запрос для создания таблицы
create_table_query = '''
CREATE TABLE IF NOT EXISTS myapp_cinema (
    data_order INTEGER,
    full_name TEXT,
    objects_of_examination TEXT,
    city TEXT,
    fo TEXT,
    e_mail TEXT,
    order_date TIMESTAMP,
    order_number INTEGER,
    status TEXT
);
'''

# Выполнение SQL-запроса для создания таблицы
cur.execute(create_table_query)

# Создание курсора для выполнения SQL-запросов
cur = conn.cursor()

# Чтение данных из Excel-файла
df = pd.read_excel("data-experts.xlsx")

# Загрузка данных в базу данных
for index, row in df.iterrows():
    cur.execute(
        """
        INSERT INTO myapp_cinema (data_order, full_name, objects_of_examination, city, fo, e_mail, order_date, order_number, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (row['data.order'], row['data.full_name'], row['data.objects_of_examination'], row['data.city'], row['data.fo'],
         row['data.e_mail'], row['data.order_date'], row['data.order_number'], row['data.status'])
    )

# Завершение транзакции и закрытие соединения
conn.commit()
cur.close()
conn.close()