from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup,KeyboardButton
from translation import translation_text
from db import Database

lang_menu = InlineKeyboardMarkup(row_width=3)

lang_ru = InlineKeyboardButton(text = 'Русский',callback_data='lang_ru')
lang_en = InlineKeyboardButton(text = 'English',callback_data='lang_en')
lang_es = InlineKeyboardButton(text = 'Español',callback_data='lang_es')

lang_menu.insert(lang_ru).insert(lang_en).insert(lang_es)

db1 = Database()

def main_menu(lang):
    keybord = ReplyKeyboardMarkup(resize_keyboard=True)
    
    button1 = KeyboardButton(translation_text('Регистрация',lang))
    button2 = KeyboardButton(translation_text('Покинуть лотерею',lang))
    
    keybord.add(button1,button2)
    return keybord

def next_menu(lang,id_user):
    
    keybord = ReplyKeyboardMarkup(resize_keyboard=True)
    
    lottery_button = KeyboardButton(translation_text('Лотерея',lang))
    
    instruction_button = KeyboardButton(translation_text('Инструкция',lang))
    
    support_button = KeyboardButton(translation_text('Поддержка',lang))
    
    personal_account_button = KeyboardButton(translation_text('Личный кабинет',lang))
    
    referall_link_button = KeyboardButton(translation_text('Реферальная программа',lang))
    
    jackpot_button = KeyboardButton(translation_text('Джекпот',lang))
    
    if(len(db1.get_amount_user_tickets(id_user))>= 5):
        keybord.add(jackpot_button)
    
    keybord.add(lottery_button,
                instruction_button,
                support_button,
                personal_account_button,
                referall_link_button
                )
    
    return keybord

def buy_ticket(lang):
    
    kb = InlineKeyboardMarkup(row_width=1)
    
    buy_lottery_ticket_button = InlineKeyboardButton(translation_text('Купить билет',lang),callback_data='buy')
    leave_buy_ticket_button = InlineKeyboardButton(translation_text('Назад',lang),callback_data='back')
    
    kb.add(buy_lottery_ticket_button,leave_buy_ticket_button)
    
    return kb

def withdraw_money(lang):
    kb = InlineKeyboardMarkup(row_width=1)
    
    withdraw_money_button = InlineKeyboardButton(translation_text('Вывести деньги',lang), callback_data='money')
    
    kb.add(withdraw_money_button)
    
    return kb

def wanna_jackpot(lang):
    kb = InlineKeyboardMarkup(row_width=1)
    
    jackpot_button = InlineKeyboardButton(translation_text('Хочу джекпот',lang), callback_data='jackpot')
    
    kb.add(jackpot_button)
    
    return kb

