translations = {
    'en': {
        'Привет!':'Hello!',
        'Регистрация': 'Registration',
        'Покинуть лотерею':'Leave the lottery'
    },
    'es':{
        'Привет!': 'Hola!',
        'Регистрация': 'Registro',
        'Покинуть лотерею':'Abandonar la lotería'
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
        