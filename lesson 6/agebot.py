import telebot

token = '5370805992:AAFOxuyiDj55Xc77BsAfbCJdTCNoGUIkxfU'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def greetings(message):
    bot.send_message(message.chat.id, 'How old are you?',)
    print(message.chat.id)

@bot.message_handler(content_types=['text'])
def old_check(message):
    try:
        age = int(message.text)
        if age >= 18:
            bot.send_message(message.chat.id, 'You are adult')
        elif age >= 1:
            bot.send_message(message.chat.id, 'You are child')
        else:
            bot.send_message(message.chat.id, 'Error!!!')

    except:
        bot.send_message(message.chat.id, 'Error!!! Try again')


bot.polling(non_stop=True)
