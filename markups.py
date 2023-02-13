from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup,KeyboardButton
from translation import translation_text
lang_menu = InlineKeyboardMarkup(row_width=3)

lang_ru = InlineKeyboardButton(text = 'Русский',callback_data='lang_ru')
lang_en = InlineKeyboardButton(text = 'English',callback_data='lang_en')
lang_es = InlineKeyboardButton(text = 'Español',callback_data='lang_es')

lang_menu.insert(lang_ru).insert(lang_en).insert(lang_es)


def main_menu(lang):
    keybord = ReplyKeyboardMarkup(resize_keyboard=True)
    
    button1 = KeyboardButton(translation_text('Регистрация',lang))
    button2 = KeyboardButton(translation_text('Покинуть лотерею',lang))
    
    keybord.add(button1,button2)
    return keybord

def next_menu(lang):
    
    keybord = ReplyKeyboardMarkup(resize_keyboard=True)
    
    lottery_button = KeyboardButton(translation_text('Лотерея',lang))
    
    instruction_button = KeyboardButton(translation_text('Инструкция',lang))
    
    support_button = KeyboardButton(translation_text('Поддержка',lang))
    
    personal_account_button = KeyboardButton(translation_text('Личный кабинет',lang))
    
    withdraw_money_button = KeyboardButton(translation_text('вывести деньги',lang))
    
    jackpot_size_button = KeyboardButton(translation_text('Размер джекпота',lang))
    
    referall_link_button = KeyboardButton(translation_text('Реферальная ссылка',lang))
    
    jackpot_button = KeyboardButton(translation_text('Джекпот',lang))
    
    keybord.add(lottery_button,
                instruction_button,
                support_button,
                personal_account_button,
                withdraw_money_button,
                jackpot_size_button,
                referall_link_button,
                jackpot_button)
    return keybord