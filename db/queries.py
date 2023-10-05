import sqlite3
from pathlib import Path
from pprint import pprint
from bot import bot


def init_db():
    global db, cursor
    db = sqlite3.connect(Path(__file__).parent.parent/'db.sqlite3')
    cursor = db.cursor()

def create_tables():
    cursor.execute(
        '''
        DROP TABLE IF EXISTS admin_id
        '''
    )
    cursor.execute(
        '''
        DROP TABLE IF EXISTS product
        '''
    )
    cursor.execute(
        '''
        DROP TABLE IF EXISTS category
        '''
    )
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS admin_id (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        adminid INTEGER
        )
        '''
    )
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS subscribers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        userid INTEGER
        )
        '''
    )
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS Category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
        '''
    )
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS product (
            productId INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price FLOAT,
            picture TEXT,
            categoryId INTEGER,
            FOREIGN KEY (categoryId) REFERENCES Category (id)
            )
        '''
    )
    db.commit()

def admin_id_tables():
    cursor.execute(
        '''
        INSERT INTO admin_id (adminid)
        VALUES (1074911421)
        '''
    )
def products_tables():
    cursor.execute(
        '''
        INSERT INTO Category (name)
        VALUES ('Обувь'), ('Футболки'), ('Брюки'), ('Куртки')
        '''
    )
    cursor.execute(
        '''
        INSERT INTO product (name, price, picture, categoryId)
        VALUES ('Кроссовки', 1214.0, '/images/Кроссовки.jpg', 1),
                ('Ботинки', 3407.0, '/images/Ботинки.jpg', 1),
                ('Лоферы', 1989.0, '/images/Лоферы.jpg', 1),
                ('Кеды', 1644.0, '/images/Кеды.jpg', 1),
                ('Сабо', 510.0, '/images/Сабо.jpg', 1),
                ('Мужские футболки', 621.0, '/images/Мужские.jpg', 2),
                ('Женские футболки', 658.0, '/images/Женские.jpg', 2),
                ('Детские футболки для мальчиков', 674.0, '/images/Детские.jpg', 2),
                ('Детские футболки для девочек', 596.0, '/images/Детские2.jpg', 2),
                ('Джоггеры', 2439.0, '/images/Джоггеры.jpg', 3),
                ('Джинсы', 2626.0, '/images/Джинсы.jpg', 3),
                ('Классические брюки', 1255.0, '/images/Классические.jpg', 3),
                ('Спортивные брюки', 1470.0, '/images/Спортивные.jpg', 3),
                ('Бомберы', 3423.0, '/images/Бомбер.jpg', 4),
                ('Кожаные куртки', 2335.0, '/images/Кожаные.jpg', 4),
                ('Демисезонные куртки', 4579.0, '/images/Демисезонные.jpg', 4),
                ('Зимние куртки', 9485.0, '/images/Зимние.jpg', 4)
        '''
    )
    db.commit()

def get_products():
    cursor.execute(
        '''
        SELECT p.name, c.name FROM product p JOIN category c ON p.categoryId = c.id
        '''
    )
    return cursor.fetchall()


def get_product_by_category(category_id):
    cursor.execute(
        '''
        SELECT * FROM product WHERE categoryId = :c_id
        ''',
        {'c_id': category_id},
    )
    return cursor.fetchall()

def save_user(user_id):
        cursor.execute(
            '''
        INSERT INTO subscribers (userid)
        VALUES (:user_id)
        ''',
    {'user_id': user_id},
    )

async def send_reminder(user_id: int):
    cursor.execute(
        '''
        SELECT * FROM login_id WHERE userid = :s_id
        ''',
        {"s_id": user_id},
    )
    await bot.send_message(user_id, 'Занятие по "Python" начнётся через 5 минут')
    db.commit()


if __name__ == "__main__":
    init_db()
    create_tables()
    products_tables()
    admin_id_tables()
    pprint(get_product_by_category())
