import random
from db import Database
db2 = Database()

def generation_win_ticket(id_user):
    while(True):
        
        random_number = random.randint(10000000,99999999)
        array_win_ticket = db2.check_unique_win_ticket(id_user)
        if(random_number not in array_win_ticket):
            db2.add_win_ticket(random_number,id_user)
            break
        
    return random_number        