import sqlite3
from pathlib import Path


def init_db():
    global db, cursor
    db = sqlite3.connect(Path(__file__).parent.parent/'db.sqlite3')
    cursor = db.cursor()

def create_tables():
    cursor.execute(
        '''
        DROP TABLE IF EXISTS product
        '''
    )
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS product (
            productId INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price INTEGER,
            picture TEXT
            )
        '''
    )
    db.commit()

def shoes_tables():
    cursor.execute(
        '''
        INSERT INTO product (name, price, picture)
        VALUES ('Кроссовки', 1214, 'images/Кроссовки.jpg'),
                ('Ботинки', 3407, 'images/Ботинки.jpg'),
                ('Лоферы', 1989, 'images/Лоферы.jpg'),
                ('Кеды', 1644, 'images/Кеды.jpg'),
                ('Сабо', 510, 'images/Сабо.jpg')
        '''
    )
    db.commit()

def t_shirts_tables():
    cursor.execute(
        '''
        INSERT INTO product (name, price, picture)
        VALUES ('Мужские футболки', 621, 'images/Мужские.jpg'),
                ('Женские футболки', 658, 'images/Женские.jpg'),
                ('Детские футболки для мальчиков', 674, 'images/Детские.jpg'),
                ('Детские футболки для девочек', 596, 'images/Детские2.jpg')
        '''
    )
    db.commit()

def trousers_tables():
    cursor.execute(
        '''
        INSERT INTO product (name, price, picture)
        VALUES ('Джоггеры', 2439, 'images/Джоггеры.jpg'),
                ('Джинсы', 2626, 'images/Джинсы.jpg'),
                ('Классические брюки', 1255, 'images/Классические.jpg'),
                ('Спортивные брюки', 1470, 'images/Спортивные.jpg')
        '''
    )
    db.commit()

def jackets_tables():
    cursor.execute(
        '''
        INSERT INTO product (name, price, picture)
        VALUES ('Бомберы', 3423, 'images/Бомбер.jpg'),
                ('Кожаные куртки', 2335, 'images/Кожаные.jpg'),
                ('Демисезонные куртки', 4579, 'images/Демисезонные.jpg'),
                ('Зимние куртки', 9485, 'images/Зимние.jpg')
        '''
    )
    db.commit()

def get_products():
    cursor.execute('''SELECT * FROM product''')
    return cursor.fetchall()


if __name__ == "__main__":
    init_db()
    create_tables()
    shoes_tables()
    t_shirts_tables()
    trousers_tables()
    jackets_tables()
    get_products()