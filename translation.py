translations = {
    'en': {
        'Привет!':'Hello!',
        'Регистрация': 'Registration',
        'Покинуть лотерею':'Leave the lottery',
        'Ваше Имя и Фамилия?':'Your first and last name?',
        'Ваша страна?':'Your country?',
        'Ваш город?':'Your city?',
        'Ваш адрес?':'Your address?',
        'Ваш индеĸс?':'Your postal code?',
        'Ваш номер телефона?':'Your phone number?',
        'Ваш адрес электронной почты?':'Your email address?'
    },
    'es':{
        'Привет!': 'Hola!',
        'Регистрация': 'Registro',
        'Покинуть лотерею':'Abandonar la lotería',
        'Ваше Имя и Фамилия?':'¿Su nombre y apellido?',
        'Ваша страна?':'¿Su país?',
        'Ваш город?':'¿Tu ciudad?',
        'Ваш адрес?':'¿Su dirección?',
        'Ваш индеĸс?':'¿Su indie Postal?',
        'Ваш номер телефона?':'¿Su número de Teléfono?',
        'Ваш адрес электронной почты?':'¿Su dirección de correo electrónico?'
    }
}

def translation_text(text,lang = 'ru'):
    if lang == 'ru':
        return text
    else:
        global translations
        try:
            return translations[lang][text]
        except:
            return text
        