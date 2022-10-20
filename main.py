import telebot
import translate

# создаём экземпляр бота
bot = telebot.TeleBot('5406951943:AAFON_RFI_f9X5FduRGpxcFF0miDTj6YZKQ')

# создаём экземпляр переводчика
translator = translate.Translator(from_lang="english", to_lang="russian")


# обработка команды /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет! Я переведу любое известное современным переводчикам слово'
                                'с английского на русский, просто напиши его ;)')


# обработка сообщений в чат
@bot.message_handler(content_types=["text"])
def handle_text(message):
    try:
        if len(message.text.split()) > 1:
            bot.send_message(message.chat.id, 'Вы написали больше одного слова! Пожалуйста, пишите по одному,'
                                              ' я ещё не так крут :(')
            return 1
        else:
            bot.send_message(message.chat.id, translator.translate(message.text))
            return 0
    except:
        bot.send_message(message.chat.id, 'Что-то пошло не так, давайте попробуем ещё раз!')
        return -1


bot.polling(none_stop=True, interval=0)
