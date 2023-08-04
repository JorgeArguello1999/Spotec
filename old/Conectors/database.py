import pymysql
import pymysql.cursors
import os

class connection:

    def __init__(self):
        password = os.getenv('DB_PASSWD')
        try:
            self.conn = pymysql.connect(
                host = os.getenv('DB_URL'),
                user = os.getenv('DB_USER'),
                password = f"{password}",
                db = 'natacion',
                charset='utf8mb4',
                cursorclass = pymysql.cursors.DictCursor
            )
            print("DB Connected")
        except pymysql.err.OperationalError as e:
            print("This is the error: ", e)

if __name__ == '__main__':
    conn = connection()
