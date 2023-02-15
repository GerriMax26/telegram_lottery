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
        self.cursor.execute(f'select * from users where id_user = {id_user}') #Проверить
        result = self.cursor.fetchall()
        return bool(len(result))
    
    def add_user(self,id_user,lang):
        sql = "INSERT INTO users (id_user,lang) VALUES (%s, %s)" #Проверить
        val = (id_user,lang)
        self.cursor.execute(sql, val)
        self.mydb.commit()
        
        
    def get_lang(self,id_user):
        self.cursor.execute(f'select lang from users where id_user = {id_user}') #Проверить
        result = self.cursor.fetchone()[0]
        return result
    
    def add_info_user(self,array,id_user,lang): #Проверить!!!
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

    def add_payment(self,payment):
        
        sql = "INSERT INTO tickets (payment) VALUES (%s)" #Проверить
        val = (payment)
        self.cursor.execute(sql, val)
        self.mydb.commit()
    
    def add_user_ticket(self,id_user,user_ticket):
        
        sql = "update tickets set user_ticket = %s where id_user == %s"
        val = (user_ticket,id_user)
        self.cursor.execute(sql, val)
        self.mydb.commit()
    
    def add_win_ticket(self,win_ticket,id_user):
        
        sql = "update tickets set win_ticket = %s where id_user == %s"
        val = (win_ticket,id_user)
        self.cursor.execute(sql, val)
        self.mydb.commit()
    
    def add_prize(self,amount_prize,id_user):
        
        sql = "update tickets set prize = %s where id_user == %s"
        val = (amount_prize,id_user)
        self.cursor.execute(sql, val)
        self.mydb.commit()
    
    def get_balance_user(self,id_user):
        
        sql = 'select balance from users where id_user == %s'
        val = (id_user)
        self.cursor.execute(sql,val)
        result = self.cursor.fetchone()[0]
        return result
    
    
    def update_balance_user(self,id_user,prize):
        
        current_balance = self.get_balance_user(id_user)
        sql = "update user set balance = %s where id_user == %s"
        val = (prize + current_balance,id_user)
        self.cursor.execute(sql, val)
        self.mydb.commit()
        
    def add_referal_link(self,id_user): #ПРОВЕРИТЬ
        
        sql = "INSERT INTO users (referal_link) VALUES (%s)"
        val = (f't.me/automatic_lottery_bot?start={id_user}')
        self.cursor.execute(sql, val)
        self.mydb.commit()
    
    def add_id_referal(self,id_referal): #Записываем в БД от кого пришел человек
        sql = "INSERT INTO users (id_referal) VALUES (%s)"
        val = (id_referal)
        self.cursor.execute(sql, val)
        self.mydb.commit()