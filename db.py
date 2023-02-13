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
            self.cursor.execute(f'select * from users where id_user = {id_user}')
            result = self.cursor.fetchall()
            return bool(len(result))
    
    def add_user(self,id_user,lang):
            sql = "INSERT INTO users (id_user,lang) VALUES (%s, %s)"
            val = (id_user,lang)
            self.cursor.execute(sql, val)
            self.mydb.commit()
        
        
    def get_lang(self,id_user):
        self.cursor.execute(f'select lang from users where id_user = {id_user}')
        result = self.cursor.fetchone()[0]
        return result
    
    def add_info_user(self,array,id_user,lang):
        array_val = []
        
        for i in array:
            array_val.append(i)
        
        array_val.append(id_user)
        
        array_val.append(lang)
        
        sql = "update users set fullName = %s,country = %s, city = %s, address = %s, postCode = %s, phone = %s, email = %s where id_user = %s and lang = %s"
        #update users set fullName = 'Maksim',country = 'Россия', city = 'Санкт-Петербург', address = 'Среднерогатская', postCode = 444444, phone = '89538320891', email = '@yandex.ru' where id_user = 1 and lang = 'en';
        val = tuple(array_val)
        self.cursor.execute(sql, val)
        self.mydb.commit()

    
    def get_fullName_user(self):
        pass