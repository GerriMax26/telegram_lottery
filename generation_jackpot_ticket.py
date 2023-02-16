import random
from datetime import date

def generation_win_ticket():
    
    today = date.today()
    if(today[5:len(today)] == '12-31'):
        win_ticket = random.randint(10000000,99999999)
        return win_ticket

#Что-то добавить