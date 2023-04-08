import telebot

bot = telebot.TeleBot('5839862571:AAE40nopFEQWOARgzEjvR-SvbbMlzZ8K3qk')

# Создаем inline клавиатуру для выбора языка
language_keyboard = telebot.types.InlineKeyboardMarkup()
language_keyboard.add(
    telebot.types.InlineKeyboardButton(text='🇷🇺 Русский', callback_data='russian'),
    telebot.types.InlineKeyboardButton(text='🇬🇧 English', callback_data='english')
)

# Создаем inline клавиатуру для выбора раздела
menu_keyboard = telebot.types.InlineKeyboardMarkup()
menu_keyboard.add(
    telebot.types.InlineKeyboardButton(text='О компании', callback_data='about'),
    telebot.types.InlineKeyboardButton(text='Планировка здания', callback_data='plan'),
    telebot.types.InlineKeyboardButton(text='Выбор языка', callback_data='message')
)
menu_keyboard1 = telebot.types.InlineKeyboardMarkup()
menu_keyboard1.add(
    telebot.types.InlineKeyboardButton(text='About the company', callback_data='about'),
    telebot.types.InlineKeyboardButton(text='Building layout', callback_data='plan'),
    telebot.types.InlineKeyboardButton(text='Choose language', callback_data='message')
)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # Отправляем сообщение с выбором языка
    bot.send_message(message.chat.id, 'Выберите язык | Choose language', reply_markup=language_keyboard)

# Обработчик inline кнопок
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    # Если пользователь выбрал язык
    if call.data in ['russian']:
        # Отправляем сообщение с выбором раздела
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Привет! \n\n'
                                   'Я гид-бот по зданию НТШ (Новгородской Технической Школы имени Ярослава Мудрого).\n\n'
                                   'Если ты не нашел нужной информации, то можешь задать вопрос нам напрямую: \n\n'
                                   'Адрес: г. Великий Новгород, Большая Санкт-Петербургская улица, 46, кабинет 201 \n\n'
                                   'Телефон +7(8162)90-60-55 \n\n'
                                   'Email: fond-info@novtechschool.ru \n\n'
                                   'Время работы: 9:00 - 18:00 \n',
                              reply_markup=menu_keyboard)
    elif call.data in ['english']:
        # Отправляем сообщение с выбором раздела
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Hi! \n\n'
                                   'I am a bot guide to the building of the NTSH (Yaroslav the Wise Novgorod Technical School).\n\n'
                                   'If you havent found the information you need, you can ask us a question directly: \n\n'
                                   'Address: Veliky Novgorod, Bolshaya St. Petersburg street, 46, office 201 \n\n'
                                   'Phone +7(8162)90-60-55 \n\n'
                                   'Email: fond-info@novtechschool.ru \n\n'
                                   'Opening hours: 9:00 - 18:00 \n',
                              reply_markup=menu_keyboard1)
    elif call.data == 'about':
        # Создаем inline клавиатуру для раздела "О компании"
        menu_keyboard2 = telebot.types.InlineKeyboardMarkup()
        menu_keyboard2.add(
            telebot.types.InlineKeyboardButton(text='Направления', callback_data='directions'),
            telebot.types.InlineKeyboardButton(text='Как стать участником', callback_data='become_member'),
            telebot.types.InlineKeyboardButton(text='Контакты', callback_data='contacts')
        )
        # Отправляем сообщение с текстом "НТШ" и inline клавиатурой для раздела "О компании"
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Новгородская техническая школа (НТШ) – это инфраструктурный проект, '
                                   'связанный с развитием прорывных (сквозных) технологий, '
                                   'на базе которого будут проводиться профессиональная ориентация школьников, '
                                   'обучение студентов, реализовываться программы опережающей профессиональной '
                                   'подготовки по профессиям и навыкам будущего, переподготовка и повышение квалификации, '
                                   'научные разработки в интересах региона, промышленных партнеров и Российской Федерации '
                                   'в целом, а также в перспективе, использование в качестве регионального центра коллективного '
                                   'пользования, создания условий для развития высокотехнологичных импортозамещающих '
                                   'отраслей промышленности и областей бизнеса.',
                              reply_markup=menu_keyboard2)
    # Если пользователь выбрал раздел "Планировка здания"
    elif call.data == 'plan':
        # Отправляем сообщение с текстом "Планировка здания" и inline клавиатурой для раздела "Планировка здания"
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Планировка здания',
                              reply_markup=menu_keyboard3)
    elif call.data == 'message':
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text='Выберите язык | Choose language',
                              reply_markup=language_keyboard)

    # Создаем inline клавиатуру для раздела "О компании"
    menu_keyboard2 = telebot.types.InlineKeyboardMarkup()
    menu_keyboard2.add(
        telebot.types.InlineKeyboardButton(text='Направления', callback_data='directions'),
        telebot.types.InlineKeyboardButton(text='Как стать участником', callback_data='become_member'),
        telebot.types.InlineKeyboardButton(text='Контакты', callback_data='contacts')
    )


# Запускаем бота
bot.polling()