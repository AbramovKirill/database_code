import psycopg2
from config import host, user, password, db_name


try:
   #3 connect to exist database
   connection = psycopg2.connect(
      host=host,
      user=user,
      password=password,
      database=db_name    
   )
   connection.autocommit = True
   
   #4 создаем объект курсор the cursor for perfoming database operations
   # можем просто положить его в переменнуб ---->   cursor = connection.cursor()
   # или воспользоваться контекстным менеджером with (пример снизу)
   with connection.cursor() as cursor:
      cursor.execute(
            "SELECT version();"
      )
      print(f"Server version: {cursor.fetchone()}")

# -------------------------------------------------------------------------------------------

   # #5 создадим новый запрос на создание таблицы --- create a new table
   # with connection.cursor() as cursor:
   #    cursor.execute(
   #        """CREATE TABLE post(
   #              post_id serial PRIMARY KEY,
   #              channel_ids serial,
   #              text varchar(50) NOT NULL,
   #              date date NOT NULL,
   #              theme_ids serial);"""
   #    )
   #       #  """CREATE TABLE channel(
   #       #       channel_id serial PRIMARY KEY,
   #       #       channel_link varchar(50) NOT NULL,
   #       #       channel_name varchar(50) NOT NULL,
   #       #       from_date date NOT NULL,
   #       #       to_date date NOT NULL);"""
   #       # """CREATE TABLE theme(
   #       #       theme_id serial PRIMARY KEY,
   #       #       theme_name varchar(50) NOT NULL,
   #       #       keywords varchar(50) NOT NULL);"""
   #       # """CREATE TABLE post(
   #       #       post_id serial PRIMARY KEY,
   #       #       channel_ids serial,
   #       #       text varchar(50) NOT NULL,
   #       #       date date NOT NULL,
   #       #       theme_ids serial);"""

   #    # connection.commit()
   #    print("[INFO] Table created successfully")

# -------------------------------------------------------------------------------------------

   #6 создадим новый запрос на заполнение значений в таблице --- insert data into a table
   with connection.cursor() as cursor:
      cursor.execute(
          """INSERT INTO post (post_id, channel_ids, text, date, theme_ids) VALUES
             ('1', '1', 'text_1', '2022-02-02', '1'),
             ('2', '2', 'text_2', '2022-02-03', '2'),
             ('3', '3', 'text_3', '2022-02-04', '3');"""
      )
      # """INSERT INTO channel (channel_id, channel_link, channel_name, from_date, to_date) VALUES
      #    ('1', '@link_1', 'channel_name_1', '2022-02-02', '2022-02-05'),
      #    ('2', '@link_2', 'channel_name_2', '2022-02-03', '2022-02-06'),
      #    ('3', '@link_3', 'channel_name_3', '2022-02-04', '2022-02-07');"""
      # """INSERT INTO theme (theme_id, theme_name, keywords) VALUES
      #    ('1', 'theme_name_1', 'keywords1, keywords2, keywords3'),
      #    ('2', 'theme_name_2', 'keywords4, keywords5, keywords6'),
      #    ('3', 'theme_name_3', 'keywords2, keywords5, keywords3');"""
      # """INSERT INTO post (post_id, channel_ids, text, date, theme_ids) VALUES
      #    ('1', '1', 'text_1', '2022-02-02', '1'),
      #    ('2', '2', 'text_2', '2022-02-03', '2'),
      #    ('3', '3', 'text_3', '2022-02-04', '3');"""

   
      print("[INFO] Data was succefully inserted")
   
# -------------------------------------------------------------------------------------------
   
   # #7 вызов данных из таблицы --- get data from a table
   # with connection.cursor() as cursor:
   #    cursor.execute(
   #       """SELECT theme_name FROM theme WHERE theme_name = 'theme_name_1';"""
   #    )
   
   #    print(cursor.fetchone())

# -------------------------------------------------------------------------------------------
   
   # #8 удаление всей таблицы целиком --- delete a table
   # with connection.cursor() as cursor:
   #     cursor.execute(
   #         """DROP DATABASE test2;"""
   #     )
   
   #     print("[INFO] Table was deleted")


# 1 блок except обрабатывает ошибки
except Exception as _ex:
   print("[INFO] Error while working with PostgreSQL", _ex)
# 2 в блоке finally, мы будем закрывать наше соединение
finally:
   if connection:
      # cursor.close()  его добавляем в код если только мы добавляем курсор просто в переменную ---->   cursor = connection.cursor()
   	connection.close()
print("[INFO] PostgreSQL connection closed")