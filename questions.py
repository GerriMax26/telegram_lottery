def registrations(count):
    
    TUPLE_QUESTIONS_REGISTRATION = ('Ваше Имя и Фамилия?','Ваша страна?','Ваш город?','Ваш адрес?','Ваш индекс?','Ваш номер телефона?','Ваш адрес электронной почты?')
    if(count<=6):
        return TUPLE_QUESTIONS_REGISTRATION[count]

def withdraw_money(count):
    TUPLE_QUESTIONS_WITHDRAW_MONEY = ('Какую сумму вы хотите вывести?','Введите номер карты')
    if(count <=1):
        return TUPLE_QUESTIONS_WITHDRAW_MONEY[count]