import random
from db import Database
db = Database()

def generation_win_ticket(id_user,id_ticket):
    random_number = random.randint(10000000,99999999)
    #Проверка, что такого номера нет в БД
    db.add_win_ticket(id_user,random_number,id_ticket)
    
    return random_number