translations = {
    'en': {
        'Привет!':'Hello!',
        'Регистрация': 'Registration',
        'Покинуть лотерею':'Leave the lottery',
        'Ваше Имя и Фамилия?':'Your first and last name?',
        'Ваша страна?':'Your country?',
        'Ваш город?':'Your city?',
        'Ваш адрес?':'Your address?',
        'Ваш индеĸс?':'Your postal code?', #проверить в main
        'Ваш номер телефона?':'Your phone number?',
        'Ваш адрес электронной почты?':'Your email address?',
        'регистрация завершена!':'registration is complete!',
        'Лотерея':'Lottery',
        'Инструкция':'Instruction',
        'Поддержка':'Support',
        'Личный кабинет':'Personal account',
        'Вывести деньги':'Withdraw money',
        'Размер джекпота:':'Jackpot Size:',
        'Реферальная ссылка':'Referral link',
        'Джекпот':'Jackpot',
        'Купить билет':'Buy a ticket',
        'Оплата прошла успешно!':'The payment was successful!',
        'Отправьте число из 8-и цифр.':'Send an 8-digit number.',
        'Номер выигрышного билета:':'Winning ticket number:',
        'Ваш выигрыш:':'Your winnings:',
        'рублей':'$',
        'Назад':'Back',
        'Ваш баланс:':'Your balance:',
        'Каĸую сумму вы хотите вывести?':'What amount do you want to withdraw?',
        'Введите номер ĸарты':'Enter the card number',
        'Заявĸа принята, ожидайте ответ от поддержĸи.':'The application has been accepted, expect a response from the support.',
        'Реферальная программа':'Referral program',
        'Хочу джеĸпот':'I want a jackpot',
        'Ваш билет зарегистрирован!':'Your ticket is registered!',
        'Номер выигрышного билета:':'Winning ticket number:',
        'Регистрация билетов для участия в Джекпоте завершена!':'',
        'Вы уже зарегистрированы в лотерее!':''
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
        'Ваш адрес электронной почты?':'¿Su dirección de correo electrónico?',
        'регистрация завершена!':'inscripción completa!',
        'Лотерея':'Lotería',
        'Инструкция':'Instrucciones',
        'Поддержка':'Soporte',
        'Личный кабинет':'Área personal',
        'Вывести деньги':'Retirar dinero',
        'Размер джекпота:':'Tamaño del bote:',
        'Реферальная ссылка':'Enlace de referencia',
        'Джекпот':'Jackpot',
        'Купить билет':'Comprar un billete',
        'Оплата прошла успешно!':'¡El pago fue exitoso!',
        'Отправьте число из 8-и цифр.':'Envía un número de 8 dígitos.',
        'Номер выигрышного билета:':'Número de billete ganador:',
        'Ваш выигрыш:':'Sus ganancias:',
        'рублей':'euro',
        'Назад':'Atrás',
        'Ваш баланс:':'Su saldo:',
        'Каĸую сумму вы хотите вывести?':'¿Cuál es la cantidad que desea retirar?',
        'Введите номер ĸарты':'Introduzca el número de ĸarta',
        'Заявĸа принята, ожидайте ответ от поддержĸи.':'Declaración aceptada, espere una respuesta del apoyo.',
        'Реферальная программа':'Programa de referencia',
        'Хочу джеĸпот':'Quiero un Jackpot',
        'Ваш билет зарегистрирован!':'¡Su boleto está registrado!',
        'Номер выигрышного билета:':'Número de billete ganador:',
        'Регистрация билетов для участия в Джекпоте завершена!':'',
        'Вы уже зарегистрированы в лотерее!':''
    }#last row add
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
        