from getpass import getpass
from mysql.connector import connect,Error
import mysql.connector

class Database:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = 'localhost',
            user = input('Имя пользователя: '),
            password = getpass('Пароль: '),
            database = 'lottery',
        )
        self.cursor = self.mydb.cursor()

        
        

    def user_exists(self,id_user):
        with self.mydb:
            self.cursor.execute(f'select * from users where id_user = {id_user}')
            result = self.cursor.fetchall()
            return bool(len(result))
    
    def add_user(self,id_user,lang):
        with self.mydb:
            sql = "INSERT INTO users (id_user,lang) VALUES (%s, %s)"
            val = (id_user,lang)
            self.cursor.execute(sql, val)
            self.mydb.commit()
        
        
    def get_lang(self,id_user):
        with self.mydb:
            return self.cursor.execute('select lang from users where id_user = ?', (id_user)).fetchone()[0]
