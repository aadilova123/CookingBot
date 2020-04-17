import shelve

import telebot
import sqlite3
from telebot import types



TOKEN = '795813628:AAGfh-sl1k1wMf-t8OjC5GUVHksEtTnAI0g'
MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'

bot = telebot.TeleBot(TOKEN)

markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=False,row_width=1)
btn_categories = types.KeyboardButton('Категории')
btn_fav = types.KeyboardButton('Избранные')
btn_search = types.KeyboardButton('Поиск')
btn_recipes = types.KeyboardButton('Рецепты')
# btn_settings = types.KeyboardButton('Настройки',callback_data = 'settings')
# btn_support = types.KeyboardButton('Назад')

markup_menu.add(btn_search,btn_recipes,btn_categories,btn_fav)
@bot.message_handler(commands=['recipes'])
def start(mess):
    chat_id = mess.chat.id
    db = shelve.open('shelve')
    db[str(chat_id)] = 'init'
    db.close()
    markup = types.ReplyKeyboardMarkup()
    btn_a = types.KeyboardButton('A')
    btn_b = types.KeyboardButton('B')
    markup.add(btn_a, btn_b)
    bot.send_message(chat_id, 'Привет', reply_markup = markup)
@bot.message_handler(func=lambda mess: mess.text=='B' and mess.content_type=='text')
def b(mess):
    chat_id = mess.chat.id
    db = shelve.open('shelve')
    state = db[str(chat_id)]
    if state != 'init':
        start(mess)#или какая-нибудь функция
    else:
        db[str(chat_id)] = 'B'
        db.close()
        markup = types.ReplyKeyboardMarkup()
        btn_hint = types.KeyboardButton('Подсказка')
        markup.add(btn_hint)
        bot.send_message(chat_id, 'B', reply_markup = markup)
@bot.message_handler(func=lambda mess: mess.text=='A' and mess.content_type=='text')
def a(mess):
    chat_id = mess.chat.id
    db = shelve.open('shelve')
    state = db[str(chat_id)]
    if state != 'init':
        start(mess)#или какая-нибудь функция
    else:
        db[str(chat_id)] = 'A'
        db.close()
        markup = types.ReplyKeyboardMarkup()
        btn_hint = types.KeyboardButton('Подсказка')
        markup.add(btn_hint)
        bot.send_message(chat_id, 'A', reply_markup = markup)
@bot.message_handler(func=lambda mess: mess.text == 'Подсказка' and mess.content_type == 'text')
def hint(mess):
    chat_id = mess.chat.id
    db = 'shelve'.open('db')
    state = db[str(chat_id)]
    if state == 'init':
        pass
    elif state == 'B':
        bot.send_message(chat_id, 'hint B')
    elif state == 'A':
        bot.send_message(chat_id, 'hint A')
@bot.message_handler(commands=['register'])
def register(m):
    conn = sqlite3.connect('db.db')
    cid = m.chat.id
    cur = conn.cursor()
    cur.execute("Create table User (	id INTEGER PRIMARY KEY,"
                " first_name TEXT NOT NULL,"
                "last_name TEXT NOT NULL)")
    user_data = m.text
    # cur.execute("insert into User values ('user_data')")
    conn.commit()
    conn.close()
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id,"Привет,друг) Я Бот-Кухонная книга! Найди интересующий тебя рецепт \nчерез - Поиск, также со мной ты научишься готовить самые изысканные блюда начиная с простых до самых сложнейших!", reply_markup = markup_menu )

@bot.message_handler(commands=['settings'])
def send_sett(message):
  keyboard2 = types.InlineKeyboardMarkup()
  rele1 = types.InlineKeyboardButton(text="1t", callback_data="1")
  rele2 = types.InlineKeyboardButton(text="2t", callback_data="2")
  rele3 = types.InlineKeyboardButton(text="3t", callback_data="3")
  backbutton = types.InlineKeyboardButton(text="back", callback_data="mainmenu")
  keyboard2.add(rele1, rele2, rele3, backbutton)
  bot.send_message(message.chat.id,"settings",reply_markup=keyboard2)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.from_user.id, "/recipes - показывает все рецепты\n"
                                           "/settings - открывает настройки\n"
                                           "/favorites - показывает избранные рецепты\n"
                                           "/help - показывает весь функционал бота\n"
                                           "/start - начинает работу с ботом")


@bot.message_handler(func=lambda message:True)
def echo_all(message):
    if message.text == "Категории":
      keyboard = types.InlineKeyboardMarkup()
      key_sweets = types.InlineKeyboardButton(text='Выпечка', callback_data='categorysweets')
      keyboard.add(key_sweets)
      key_categories1 = types.InlineKeyboardButton(text='Первые блюда', callback_data='categorysoup')
      keyboard.add(key_categories1)
      key_2nddishes = types.InlineKeyboardButton(text='Основное блюдо', callback_data='category2nfood')
      keyboard.add(key_2nddishes)
      key_meiramfood = types.InlineKeyboardButton(text='Праздничные блюда', callback_data='categorymeiram')
      keyboard.add(key_meiramfood)
      key_kz = types.InlineKeyboardButton(text='Национальная кухня', callback_data='nathionalfood')
      keyboard.add(key_kz)
      key_gruzinf = types.InlineKeyboardButton(text='Грузинская кухня', callback_data='Gruzinfood')
      keyboard.add(key_gruzinf)
      key_koreanf = types.InlineKeyboardButton(text='Корейская кухня', callback_data='KoreanFood')
      keyboard.add(key_koreanf)
      key_salats = types.InlineKeyboardButton(text='Салаты', callback_data='Salats')
      keyboard.add(key_salats)
      key_desert = types.InlineKeyboardButton(text='Напитки', callback_data='drinks')
      keyboard.add(key_desert)
      bot.send_message(message.from_user.id, "Здесь ты можешь найти рецепты разделенные по категориям:" , reply_markup = keyboard)
    if message.text =="Поиск":
      keyboard = types.InlineKeyboardMarkup()
      url_button = types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
      url_button1 = types.InlineKeyboardButton(text="Поиск по ингридиентам", url="https://1000.menu/cooking/search")
      keyboard.add(url_button, url_button1)
      bot.send_message(message.chat.id, "Спасибо, что ты с нами! Нажми на кнопку и перейди в любой поисковик по твоему желанию.", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data =="categories":
      keyboard = types.InlineKeyboardMarkup()
      key_sweets = types.InlineKeyboardButton(text='Выпечка', callback_data='categorysweets')
      keyboard.add(key_sweets)
      key_categories1 = types.InlineKeyboardButton(text='Первые блюда', callback_data='categorysoup')
      keyboard.add(key_categories1)
      key_2nddishes = types.InlineKeyboardButton(text='Основное блюдо', callback_data='category2nfood')
      keyboard.add(key_2nddishes)
      key_meiramfood = types.InlineKeyboardButton(text='Праздничные блюда', callback_data='categorymeiram')
      keyboard.add(key_meiramfood)
      key_kz = types.InlineKeyboardButton(text='Национальная кухня', callback_data='nathionalfood')
      keyboard.add(key_kz)
      key_gruzinf = types.InlineKeyboardButton(text='Грузинская кухня', callback_data='Gruzinfood')
      keyboard.add(key_gruzinf)
      key_koreanf = types.InlineKeyboardButton(text='Корейская кухня', callback_data='KoreanFood')
      keyboard.add(key_koreanf)
      key_salats = types.InlineKeyboardButton(text='Салаты', callback_data='Salats')
      keyboard.add(key_salats)
      key_desert = types.InlineKeyboardButton(text='Напитки', callback_data='drinks')
      keyboard.add(key_desert)
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Здесь ты можешь найти рецепты разделенные по категориям:",
                            reply_markup=keyboard)
      # bot.send_message(chat_id=call.message.from_user.id, text = "Здесь ты можешь найти рецепты разделенные по категориям:",
      #                  reply_markup=keyboard)
    if call.data == "categorysweets":
        keyboardmain = types.InlineKeyboardMarkup(row_width=1)
        first_button = types.InlineKeyboardButton(text="Французские круассаны с шоколадом", callback_data="first")
        second_button = types.InlineKeyboardButton(text="Шоколадный бархатный бисквит", callback_data="second")
        third_button = types.InlineKeyboardButton(text="Американский чизкейк", callback_data="third")
        fourth_button = types.InlineKeyboardButton(text="Торт 'Молочная девочка'", callback_data="fourth")
        backbutton = types.InlineKeyboardButton(text="back", callback_data="categorymenu")
        keyboardmain.add(first_button, second_button, third_button,fourth_button,backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выпечка",reply_markup=keyboardmain)
    if call.data == "first":
        text =  "Количество продуктов на 18 круассанов:\n"+"500 гр муки высшего сорта\n"+"60 гр сахарного песка\n"+"10 гр соли\n"+"200 гр чуть теплого молока\n"+"1 яйцо\n"+"60 гр сливочного масла"
        img = "https://www.eat-me.ru/wp-content/uploads/2019/10/kruassan-shokolad.jpg"
        chat_id = call.message.chat.id
        keyboard = types.InlineKeyboardMarkup()
        url_b = types.InlineKeyboardButton(text="Перейте к готовке", url="https://www.eat-me.ru/20191013/kruassan-shokolad.htm")
        share = types.InlineKeyboardButton(text = "Поделиться",switch_inline_query="Telegram")
        keyboard.add(url_b,share)
        bot.send_message(chat_id, f'{text}\n{img}',reply_markup=keyboard)
    if call.data == "second":
        text =  "Продукты:\nЯйца - 4 шт\nМолоко - 150 мл\nМука - 220 г\nСахар - 160 г\nМасло сливочное - 150 г\nКакао-порошок - 100 г"
        img = "https://avatars.mds.yandex.net/get-zen_doc/1581245/pub_5e4916be67bb927569fb000f_5e493bee92b8200f2f56c375/scale_1200"
        chat_id = call.message.chat.id
        keyboard = types.InlineKeyboardMarkup()
        url_b = types.InlineKeyboardButton(text="Перейте к готовке", url="https://www.russianfood.com/recipes/recipe.php?rid=142989")
        share = types.InlineKeyboardButton(text = "Поделиться",switch_inline_query="Telegram")
        keyboard.add(url_b,share)
        bot.send_message(chat_id, f'{text}\n{img}',reply_markup=keyboard)
    if call.data == "third":
        text =  "Американский классический чизкейк\n" +  "Ингредиенты:\n"+ "Печенье песочное - 300 гр\n"+ "Сливочное масло - 100 гр\n"+ "Мускатный орех - 0.25 чайн.л.\n"+ "Сливочный сыр - 600 гр\n"+ "Сахар - 150 гр"
        img = "https://static.1000.menu/img/content/26665/chizkeik-nu-iork-s-kremette_1523900039_13_max.jpg"
        chat_id = call.message.chat.id
        keyboard = types.InlineKeyboardMarkup()
        url_b = types.InlineKeyboardButton(text="Перейте к готовке", url="https://1000.menu/cooking/26665-chizkeik-nu-iork-klassicheskii")
        share = types.InlineKeyboardButton(text = "Поделиться",switch_inline_query="Telegram")
        keyboard.add(url_b,share)
        bot.send_message(chat_id, f'{text}\n{img}',reply_markup=keyboard)
    if call.data == "fourth":
        text =  "Ингредиенты:\nЯйцо куриное 2 Шт\nМолоко сгущенное 380 Г\nМука пшеничная 160 Г\nРазрыхлитель 1 Ст. л\nВанилин 1 Ч. л.о"
        img = "https://dom-desertov.ru/wp-content/uploads/2018/02/molochnaya-devochka-retsept-torta-1125x1500.jpeg"
        chat_id = call.message.chat.id
        keyboard = types.InlineKeyboardMarkup()
        url_b = types.InlineKeyboardButton(text="Перейте к готовке", url="https://www.russianfood.com/recipes/recipe.php?rid=152315")
        share = types.InlineKeyboardButton(text = "Поделиться",switch_inline_query="Telegram")
        keyboard.add(url_b,share)
        bot.send_message(chat_id, f'{text}\n{img}',reply_markup=keyboard)
    if call.data == "categorysoup":
      keyboardmain = types.InlineKeyboardMarkup(row_width=1)
      first_button1 = types.InlineKeyboardButton(text="Гаспачо", callback_data="first1")
      second_button2 = types.InlineKeyboardButton(text="Грибной крем-суп ", callback_data="second1")
      third_button3 = types.InlineKeyboardButton(text="Суп лапша с цыпленком", callback_data="third1")
      fourth_button4 = types.InlineKeyboardButton(text="Чечевичный суп", callback_data="fourth1")
      backbutton = types.InlineKeyboardButton(text="back", callback_data="categorymenu")
      keyboardmain.add(first_button1, second_button2, third_button3, fourth_button4,backbutton)
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Первые блюда",
                            reply_markup=keyboardmain)
    if call.data == "first1":
        text =  "Ингредиенты:\nПомидоры\nЛук репчатый\nКонсервированный перец\nОгурцы\nТоматный сок"
        img = "https://img09.rl0.ru/eda/1200x-i/s2.eda.ru/StaticContent/Photos/110816122021/120213184954/p_O.jpg"
        chat_id = call.message.chat.id
        keyboard = types.InlineKeyboardMarkup()
        url_b = types.InlineKeyboardButton(text="Перейте к готовке", url="https://eda.ru/recepty/supy/klassicheskij-gaspacho-21178")
        share = types.InlineKeyboardButton(text = "Поделиться",switch_inline_query="Telegram")
        keyboard.add(url_b,share)
        bot.send_message(chat_id, f'{text}\n{img}',reply_markup=keyboard)
    if call.data == "category2nfood":
      keyboardmain = types.InlineKeyboardMarkup(row_width=1)
      first_button = types.InlineKeyboardButton(text="Кесадилья с курицей и овощной начинкой", callback_data="first2")
      second_button = types.InlineKeyboardButton(text="Паста Фетуччини", callback_data="second2")
      third_button = types.InlineKeyboardButton(text="Стейк по-американски", callback_data="third2")
      fourth_button = types.InlineKeyboardButton(text="Мясо по-тайски", callback_data="fourth2")
      backbutton = types.InlineKeyboardButton(text="back", callback_data="categorymenu")
      keyboardmain.add(first_button, second_button, third_button, fourth_button,backbutton)
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вторые блюда:",
                            reply_markup=keyboardmain)
    if call.data == "first2":
        text =  "Ингредиенты:\nПомидоры\nЛук репчатый\nКонсервированный перец\nОгурцы\nКесадилья\nТворожный сыр"
        img = "https://gribnichki.ru/wp-content/uploads/2017/04/1452077491_kesadilya-s-kuricey-i-gribami.jpg"
        chat_id = call.message.chat.id
        keyboard = types.InlineKeyboardMarkup()
        url_b = types.InlineKeyboardButton(text="Перейте к готовке", url="https://gribnichki.ru/recepty-s-gribami/zakuski/meksikanskaya-kesadilya-s-kuricej-i-gribami.html")
        share = types.InlineKeyboardButton(text = "Поделиться",switch_inline_query="Telegram")
        keyboard.add(url_b,share)
        bot.send_message(chat_id, f'{text}\n{img}',reply_markup=keyboard)
    if call.data == "categorymeiram":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Тарталетки с красной икрой", callback_data="1")
        rele2 = types.InlineKeyboardButton(text="Канапе с лососем", callback_data="2")
        rele3 = types.InlineKeyboardButton(text="Куриный рулет со сливочным сыром", callback_data="3")
        rele4 = types.InlineKeyboardButton(text="Сочный цыпленок в духовке", callback_data="4")
        backbutton = types.InlineKeyboardButton(text="back", callback_data="categorymenu")
        keyboard.add(rele1, rele2, rele3,rele4,backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Праздничное меню:",reply_markup=keyboard)

    if call.data == "nathionalfood":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        ret1 = types.InlineKeyboardButton(text="Бешбармак", callback_data="1nat")
        ret2 = types.InlineKeyboardButton(text="Сырне", callback_data="2nat")
        ret3 = types.InlineKeyboardButton(text="Бульон по-казахски", callback_data="3nat")
        ret4 = types.InlineKeyboardButton(text="Манты", callback_data="4nat")
        backbutton = types.InlineKeyboardButton(text="back", callback_data="categorymenu")
        keyboard.add(ret1, ret2, ret3 ,ret4,backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Национальные блюда:",reply_markup=keyboard)
    if call.data == "drinks":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        d1 = types.InlineKeyboardButton(text="Классический Мохито", callback_data="1drink")
        d2 = types.InlineKeyboardButton(text="Лимонад имбирь-цитрус", callback_data="2drink")
        d3 = types.InlineKeyboardButton(text="Молочный коктейль", callback_data="3drink")
        d4 = types.InlineKeyboardButton(text="Фирменный коктейль с шоколадом", callback_data="4drink")
        backbutton = types.InlineKeyboardButton(text="назад", callback_data="categorymenu")
        keyboard.add(d1, d2, d3,d4,backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Холодные напитки:",reply_markup=keyboard)
    if call.data == "KoreanFood":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        k1 = types.InlineKeyboardButton(text="Кукси", callback_data="1k")
        k2 = types.InlineKeyboardButton(text="Рамён", callback_data="2k")
        k3 = types.InlineKeyboardButton(text="Токпокки", callback_data="3k")
        k4 = types.InlineKeyboardButton(text="Пиггоди", callback_data="4k")
        backbutton = types.InlineKeyboardButton(text="назад", callback_data="categorymenu")
        keyboard.add(k1, k2, k3,k4,backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Корейские блюда:",reply_markup=keyboard)
    if call.data == "Salats":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="Цезарь", callback_data="1drink")
        rele2 = types.InlineKeyboardButton(text="Малибу", callback_data="2drink")
        rele3 = types.InlineKeyboardButton(text="Королевский салат с сухариками", callback_data="3drink")
        rele4 = types.InlineKeyboardButton(text="Дамский каприз", callback_data="4drink")
        backbutton = types.InlineKeyboardButton(text="назад", callback_data="categorymenu")
        keyboard.add(rele1, rele2, rele3,rele4,backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Салаты:",reply_markup=keyboard)
    if call.data == "categorymenu":
      keyboard = types.InlineKeyboardMarkup(row_width=2)
      cd = types.InlineKeyboardButton(text="Категории", callback_data="categories")
      fav = types.InlineKeyboardButton(text="Избранные", callback_data="ff2")
      search = types.InlineKeyboardButton(text="Поиск",callback_data="ff3")
      recipes = types.InlineKeyboardButton(text="Рецепты",callback_data="ff4")
      keyboard.add(fav,cd,search,recipes)
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Back:",
                            reply_markup=keyboard)

    elif call.data == "Gruzinfood":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        r1 = types.InlineKeyboardButton(text="Чахохбили", callback_data="gg1")
        r2 = types.InlineKeyboardButton(text="Хачапури по-аджарски", callback_data="gg2")
        r3 = types.InlineKeyboardButton(text="Хинкали", callback_data="gg3")
        r4 = types.InlineKeyboardButton(text="Хычины", callback_data="gg4")
        backbutton = types.InlineKeyboardButton(text="back", callback_data="categorymenu")
        keyboard.add(r1,r2,r3,r4,backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Грузинская кухня:",reply_markup=keyboard)



if __name__ == "__main__":
    bot.polling(none_stop=True, timeout=123)


# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#   if message.text == "Привет":
#     bot.send_message(message.from_user.id, "Привет,друг) Я Бот-Кухонная книга! Найди интересующий тебя рецепт через - Поиск, также со мной ты научишься готовить самые изысканные блюда начиная с простых до самых сложнейших!")
#     keyboard = types.InlineKeyboardMarkup()
#     key_search = types.InlineKeyboardButton(text='Поиск', callback_data='menu')
#     keyboard.add(key_search)
#     key_categories = types.InlineKeyboardButton(text='Категории', callback_data='menu')
#     keyboard.add(key_categories)
#     key_saves = types.InlineKeyboardButton(text='Избранные', callback_data='menu')
#     keyboard.add(key_saves)
#     key_random = types.InlineKeyboardButton(text='Рецепты', callback_data='menu')
#     keyboard.add(key_random)
#     key_support = types.InlineKeyboardButton(text='Настройка и помощь', callback_data='menu')
#     keyboard.add(key_support)
#     bot.send_message(message.from_user.id, text='Выбери то, что тебе нужно:', reply_markup=keyboard)
#   elif message.text == "/help":
#     bot.send_message(message.from_user.id, "Напиши Привет")
#   else:
#     bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")









