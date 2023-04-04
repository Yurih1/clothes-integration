import pymysql
import os


class Connection:
    
    #TODO: Passar essa solução para SQLAlchemy e refatoras os repositories
    
    def conn(self):
        try:
            db_connection = pymysql.connect(
                host=os.environ['DB_HOST'],
                user=os.environ['DB_USER'],
                password=os.environ['DB_PASS'],
                database=os.environ['DB_NAME'],
                cursorclass=pymysql.cursors.DictCursor
            )

        except pymysql.Error as e:
            print(f'Erro ao conectar ao database: {e}')
        
        return db_connection

    def execute(self, query):
        conn = self.conn()
        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()
            conn.close()

        return result

    def insert(self, query):
        conn = self.conn()
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()
            conn.close()
