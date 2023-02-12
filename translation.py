translations = {
    'en': {
        'Привет!':'Hello!',
        'Регистрация': 'Registration',
        'Покинуть лотерею':'Leave the lottery',
        'Ваше Имя и Фамилия?':'Your first and last name?'
    },
    'es':{
        'Привет!': 'Hola!',
        'Регистрация': 'Registro',
        'Покинуть лотерею':'Abandonar la lotería',
        'Ваше Имя и Фамилия?':'¿Su nombre y apellido?'
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
        