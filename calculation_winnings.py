def calculation_win(id_ticket,id_win_ticket,lang):
    
    value_many_lang = {
        'ru':50,
        'en':2,
        'es':2
    }
    
    id_ticket = str(id_ticket)
    
    id_win_ticket = str(id_win_ticket)
    
    amount_resemblance = 0
    
    if(id_ticket[0:2] == id_win_ticket[0:2]):
        amount_resemblance += 1
    elif(id_ticket[2:4] == id_win_ticket[2:4]):
        amount_resemblance += 1
    elif (id_ticket[4:6] == id_win_ticket[4:6]):
        amount_resemblance += 1
    elif (id_ticket[6:8] == id_win_ticket[6:8]):
        amount_resemblance += 1
    
    if(amount_resemblance == 1):
        return value_many_lang[lang]*10/100
    elif(amount_resemblance == 2):
        return value_many_lang[lang]*40/100
    elif(amount_resemblance == 3):
        return value_many_lang[lang]*210/100
    elif(amount_resemblance == 4):
        return value_many_lang[lang]*500/100
    else:
        return 0
        