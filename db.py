import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    
    def __init__(self):
        
        self.mydb = mysql.connector.connect(
            host = os.getenv('HOST'),
            user = os.getenv('USER'),
            password = os.getenv('PASSWORD'),
            database = os.getenv('DATABASE'),
        )
        self.cursor = self.mydb.cursor()

    def user_exists(self,id_user):
        
        self.cursor.execute(f'select * from users where id_user = {id_user}') 
        result = self.cursor.fetchall()
        return bool(len(result))
    
    
    def add_referal_link(self,id_user):
        
        sql = "INSERT INTO users (id_user,referal_link) VALUES (%s,%s)"
        val = (id_user,f't.me/automatic_lottery_bot?start={id_user}')
        self.cursor.execute(sql, val)
        self.mydb.commit()
        
    def add_id_referal(self,id_referal,id_user):
        
        sql = "update users set id_referal = %s where id_user = %s"
        val = (id_referal,id_user)
        self.cursor.execute(sql, val)
        self.mydb.commit()
        
    def add_user(self,id_user,lang):
        
        sql = "update users set lang = %s where id_user = %s"
        val = (lang,id_user)
        self.cursor.execute(sql, val)
        self.mydb.commit()
    
    
        
    def get_lang(self,id_user):
        
        self.cursor.execute(f'select lang from users where id_user = {id_user}')
        result = self.cursor.fetchone()[0]
        return result
    
    def add_info_user(self,array,id_user):
        
        array_val = []
        
        for i in array:
            array_val.append(i)
        
        array_val.append(id_user)
        
        sql = "update users set fullName = %s,country = %s, city = %s, address = %s, postCode = %s, phone = %s, email = %s where id_user = %s"
        val = tuple(array_val)
        self.cursor.execute(sql, val)
        self.mydb.commit()

    def check_id_referal(self,id_user):
        
        sql = f'select id_referal from users where id_user = {id_user}'
        self.cursor.execute(sql) 
        result = self.cursor.fetchone()[0]
        return result
    
    def add_payment(self,payment,id_user):
        
        sql = "INSERT INTO tickets (payment,id_user) VALUES (%s,%s)" 
        val = (payment,id_user)
        self.cursor.execute(sql, val)
        self.mydb.commit()
    
    def add_user_ticket(self,id_user,user_ticket):
        
        sql = "update tickets set user_ticket = %s where id_user = %s and user_ticket = NULL"
        val = (user_ticket,id_user)
        self.cursor.execute(sql, val)
        self.mydb.commit()
    
    def check_unique_win_ticket(self,id_user):
        
        sql = f'select win_ticket from tickets where id_user = {id_user}'
        self.cursor.execute(sql) 
        result = self.cursor.fetchall()
        return result
    
    def add_win_ticket(self,win_ticket,id_user): #ok изменить на insert!!!
        
        sql = "update tickets set win_ticket = %s where id_user = %s and win_ticket = NULL"
        val = (win_ticket,id_user)
        self.cursor.execute(sql, val)
        self.mydb.commit()
    
    def add_prize(self,amount_prize,id_user):
        
        sql = "update tickets set prize = %s where id_user = %s"
        val = (amount_prize,id_user)
        self.cursor.execute(sql, val)
        self.mydb.commit()
    
    def update_balance_user(self,id_user,prize):
        
        current_balance = self.get_balance_user(id_user)
        sql = "update users set balance = %s where id_user = %s"
        val = (prize + current_balance,id_user)
        self.cursor.execute(sql, val)
        self.mydb.commit()
    
    def get_balance_user(self,id_user):
        
        sql = f'select balance from users where id_user = {id_user}'
        self.cursor.execute(sql)
        result = self.cursor.fetchone()[0]
        return result
    
    def get_referal_link(self,id_user):
        sql = 'select referel_link from users where id_user = %s'
        val = (id_user)
        self.cursor.execute(sql,val)
        result = self.cursor.fetchone()[0]
        return result
    
    def get_jackpot_prize(self):
        
        sql = 'select prize from jackpot'
        self.cursor.execute(sql) 
        result = self.cursor.fetchall()
        return result
    
    def get_amount_user_tickets(self,id_user):
        
        sql = f'select id_ticket from tickets where id_user = {id_user}'
        self.cursor.execute(sql) 
        result = self.cursor.fetchall()
        return result
    
    
    def add_jackpot_ticket(self,id_jackpot,id_user,user_ticket):
        
        sql = "INSERT INTO jackpot_user (id_jackpot,id_user,user_ticket) VALUES (%s,%s,%s)" 
        val = (id_jackpot,id_user,user_ticket)
        self.cursor.execute(sql, val)
        self.mydb.commit()
    
    def get_date_jackpot(self):
        
        sql = 'select id_jackpot,start_time,end_time from jackpot'
        self.cursor.execute(sql) 
        result = self.cursor.fetchall()
        return result
    
    def get_all_jackpot_user(self,id_jackpot):
        
        sql = 'select id_user from jackpot where id_jackpot = %s'
        val = (id_jackpot)
        self.cursor.execute(sql,val) 
        result = self.cursor.fetchall()
        return result
    
    def get_all_data_user(self,id_user):
        sql = f'select * from users where id_user = {id_user}'
        self.cursor.execute(sql) 
        result = self.cursor.fetchall()
        return result
