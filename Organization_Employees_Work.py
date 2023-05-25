
# импортируем файл с токеном телеграм бота, которого хотим использовать
# в файле пишем token=' сюда вставляем токен, присвоенный @BotFather '
import bot_token
# импортируем библиотеку для разработки телеграм бота
import telebot
# импортируем библиотеку с типами, для возможности создания кнопок
from telebot import types
# импортируем файл с функцией для сопоставления текущего времени с временем работы предприятия
import stt

# из файла bot_token вызываем переменную token, где хранится токен
bot = telebot.TeleBot(bot_token.token)

# вызываем декоратор функции обработки входного сообщения от пользователя
# и настраиваем его на работы с типом сообщений "команда от пользователя" с названием "/start"
# кнопка появится при первом входе в личный чат с ботом
@bot.message_handler(commands=['start'])
# бот должен обрабатывать текстовые сообщения как команды
# для этого во всех фукциях аргументом выступает " message "
def start_phrase(message):
    # если у предприятия есть логотип, то необходимо создать файл типа .png с параметрами 200*200 пикселей и 100ppi
    # при сохранении использовать минимальный размер. После конвертировать файл в .webp
    # для отображения логотипа в приветствии, необходимо
    # инициировать переменную как =open(путь к файлу внутри папки проекта, указать тип для использование 'rb')
    ico = open('ico/ico_IS_SUAI.webp', 'rb')

    # теперь логотип предриятия превратился в стикер, который вызывается следующей командой
    bot.send_sticker(message.chat.id, ico)

    # markup служит для идентификации различный типов объектов, используемых для взаимодейсвия ботом
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    # инициируем виртульные кнопки, в скобочках в виде аргумента выступает надпись на кнопке
    bt1 = types.KeyboardButton("Расписание работы лаборатории")
    bt2 = types.KeyboardButton("Связь с заведующим")
    bt3 = types.KeyboardButton("Список мероприятий")

    # добавляем кнопки в чат с ботом
    markup.add(bt1, bt2, bt3)

    # настраиваем ответное сообщение от бота при использовании команды " /start "
    # команда " parse_mode='' " применяется, если необходимо использовать другой язык программирования
    # это применимо для видоизмененя ответного сообщения(например, как в MS Word можно сделать нужное слово полужирным)
    # в программе это реализовано через язык программирования html, нужные слова выделяются конструкцией " <b>...</b> "
    bot.send_message(message.chat.id, "Добро пожаловть, {0.first_name}.\n\t\t Меня зовут <b>{1.first_name}</b>! "
                                      "Я - ваш путеводитель по лаборатории робототехники ИШ ГУАП."
                                      " Чтобы узнать мои возможности, вы в любое время можете написать в чат:"
                                      " <b>/help</b> , эта команда покажет навигацию моих команд.\n\t\t "
                                      "Приятного времяприпровождения в стенках Инженерной "
                                      "Школы ГУАП.".format(message.from_user, bot.get_me()),
    parse_mode='html', reply_markup=markup)

# вызываем декоратор функции обработки входного сообщения от пользователя
# и настраиваем его на работы с типом сообщений "команда от пользователя" с названием "/help"
@bot.message_handler(commands=['help'])
# по аналогии с созданной функцией " start_phrase() " инициируем новую функцию
# для ответа на запросы для выше созданной команды
# в отличие от " start_phrase() ", не нужно снова задавать кнопки
def helper(message):
    bot.send_message(message.chat.id, "Вы можете выбрать несколько копанд:\n\t\t <b>Расписание работы лаборатории</b>"
                                      " - могу показать ежедневное расписание лаборатории, либо узнаю - работает ли она"
                                      " в тот момент, когда вы захотите это узнать;\n\t\t <b>Связь с заведующим</b>"
                                      " - можно узнать контактные данные, либо написать заведующему;\n\t\t"
                                      " <b>Список мероприятий</b> - вам отобразятся все необходимые ссылки, где вы "
                                      "подробнее ознакомитесь с прошедшими и грядущими мероприятиями, "
                                      "проводимые в ИШ ГУАП.".format(message.from_user, bot.get_me()),
    parse_mode='html')

# вызываем декоратор функции обработки входного обычного текстового сообщения от пользователя
# и настраиваем его на работу с текстовыми сообщениями
@bot.message_handler(content_types=['text'])
def bot_message(message):
    # органиуем переписку в личном чате с ботом через " message.chat.type == 'private' "
    if message.chat.type == 'private':
        # Организовываем работу кнопки "Расписание работы лаборатории"
        if message.text == "Расписание работы лаборатории":
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            bt1 = types.KeyboardButton("Полное расписание")
            bt2 = types.KeyboardButton("Открыта сейчас?")
            back = types.KeyboardButton("назад")
            markup.add(bt1, bt2, back)
            bot.send_message(message.chat.id, "Выберите один из следующий вариантов:\n\t\t <b>Полное расписание</b> "
                                              "- Я покажу вам ежедневное расписание работы лаборатории;\n\t\t"
                                              " <b>Открыта сейчас?</b> - Проверю, работает ли сейчас"
                                              " лаборатория и отвечу вам.",
            parse_mode='html', reply_markup=markup)

            if message.text == "назад":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                bt5 = types.KeyboardButton("Расписание работы лаборатории")
                bt6 = types.KeyboardButton("Связь с заведующим")
                bt7 = types.KeyboardButton("Список мероприятий")
                markup.add(bt5, bt6, bt7)
                bot.send_message(message.chat.id, "Вы вернулись в главное меню, "
                                                  "чтобы узнать доступные команды введит <b>/help</b>, либо"
                                                  " выберите необходимое действие:",
                parse_mode='html', reply_markup=markup)

        if message.text == "Связь с заведующим":
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            bt3 = types.KeyboardButton("Контактные данные")
            bt4 = types.KeyboardButton("Открыть чат")
            back = types.KeyboardButton("назад")
            markup.add(bt3, bt4, back)
            bot.send_message(message.chat.id, "Выберите следующее действие:", reply_markup = markup)

        if message.text == "Список мероприятий":
            bot.send_message(message.chat.id, "Группа в ВК:\n\t "
                                              "https://vk.com/public207559107\n Список мероприятиятий по ссылке:\n\t"
                                              " https://docs.google.com/spreadsheets/"
                                              "d/1Xu10e2dpv_-s4e413pvWUcHys3VUGh7XYt337Exfi1g/edit#gid=0")

        if message.text == "назад":
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            bt5 = types.KeyboardButton("Расписание работы лаборатории")
            bt6 = types.KeyboardButton("Связь с заведующим")
            bt7 = types.KeyboardButton("Список мероприятий")
            markup.add(bt5, bt6, bt7)
            bot.send_message(message.chat.id, "Вы вернулись в главное меню, выберите необходимое действие:",
            reply_markup = markup)

        if message.text == "Контактные данные":
            bot.send_message(message.chat.id,
            """
            Заведующий лаборатории: Василий Евгеньевич Белай \n
            
            """)

        if message.text == "Открыть чат":
            bot.send_message(message.chat.id, "https://t.me/bvecool")
            
        elif message.text == "Полное расписание":
            bot.send_message(message.chat.id, "Расписание работы лаборатории робототехники:\n\t\t"
                                              " <b>Пн-Пт: 11:00-20:00</b>\n\t\t"
                                              " <b>Сб: 12:00-19.00</b>",
            parse_mode='html')
            
        elif message.text == "Открыта сейчас?":
            #
            bot.send_message(message.chat.id, stt.lab_status())

# организация точки входа кода
if __name__ == '__main__':
    # инициализируем бесконечный цикл получения новых записей со стороны Telegram
    bot.polling(none_stop = True)