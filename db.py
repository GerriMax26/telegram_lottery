from getpass import getpass
from mysql.connector import connect,Error

try:
    with connect(
        host = 'localhost',
        user = input('Имя пользователя: '),
        password = getpass('Пароль: '),
        database = 'lottery',
    ) as connection:
        print(connection)
except Error as e:
    print(e)
    
