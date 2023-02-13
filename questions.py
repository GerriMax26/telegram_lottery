def registrations(count):
    
    TYPLE_QUESTIONS = ('Ваше Имя и Фамилия?','Ваша страна?','Ваш город?','Ваш адрес?','Ваш индекс?','Ваш номер телефона?','Ваш адрес электронной почты?')
    if(count<=6):
        return TYPLE_QUESTIONS[count]

