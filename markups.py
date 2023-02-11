from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup,KeyboardButton
from translation import translation_text
lang_menu = InlineKeyboardMarkup(row_width=3)

lang_ru = InlineKeyboardButton(text = 'Русский',callback_data='lang_ru')
lang_en = InlineKeyboardButton(text = 'English',callback_data='lang_en')
lang_es = InlineKeyboardButton(text = 'Español',callback_data='lang_es')

lang_menu.insert(lang_ru).insert(lang_en).insert(lang_es)


def main_menu(lang):
    keybord = ReplyKeyboardMarkup(resize_keyboard=True)
    
    button1 = KeyboardButton(translation_text('Регистарция'),lang)
    button2 = KeyboardButton(translation_text('Покинуть лотерею'),lang)
    
    keybord.add(button1,button2)
    return keybord