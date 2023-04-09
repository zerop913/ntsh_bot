import telebot

bot = telebot.TeleBot("5839862571:AAE40nopFEQWOARgzEjvR-SvbbMlzZ8K3qk")

# Создаем inline клавиатуру для выбора языка
language_keyboard = telebot.types.InlineKeyboardMarkup()
language_keyboard.add(
    telebot.types.InlineKeyboardButton(text="🇷🇺 Русский", callback_data="russian"),
    telebot.types.InlineKeyboardButton(text="🇬🇧 English", callback_data="english"),
)

# Создаем inline клавиатуру для выбора раздела
menu_keyboard = telebot.types.InlineKeyboardMarkup()
menu_keyboard.add(
    telebot.types.InlineKeyboardButton(text="О компании", callback_data="about"),
    telebot.types.InlineKeyboardButton(text="Планировка здания", callback_data="plan"),
    telebot.types.InlineKeyboardButton(text="Выбор языка", callback_data="message"),
)
menu_keyboard_back = telebot.types.InlineKeyboardMarkup()
menu_keyboard_back.add(
    telebot.types.InlineKeyboardButton(text="Назад", callback_data="back")
)
menu_keyboard1 = telebot.types.InlineKeyboardMarkup()
menu_keyboard1.add(
    telebot.types.InlineKeyboardButton(text='About the company', callback_data='about'),
    telebot.types.InlineKeyboardButton(text='Building layout', callback_data='plan'),
    telebot.types.InlineKeyboardButton(text='Choose language', callback_data='message')
)
# Создаем inline клавиатуру для раздела "Направления"
directions_keyboard = telebot.types.InlineKeyboardMarkup()
directions_keyboard.add(
    telebot.types.InlineKeyboardButton(text="НТШ", url='https://novtechschool.ru/'),
    telebot.types.InlineKeyboardButton(text="Образовательные программы", url='https://novtechschool.ru/edu_prog/'),
    telebot.types.InlineKeyboardButton(text="Назад", callback_data="back")
)
become_member_keyboard = telebot.types.InlineKeyboardMarkup()
become_member_keyboard.add(
    telebot.types.InlineKeyboardButton(text="Форма", url='https://istc-valday.ru/uchastnikam/'),
    telebot.types.InlineKeyboardButton(text="Назад", callback_data="back")
)
contacts_keyboard = telebot.types.InlineKeyboardMarkup()
contacts_keyboard.add(
    telebot.types.InlineKeyboardButton(text="VK", url='https://vk.com/novtechscool'),
    telebot.types.InlineKeyboardButton(text="Сайт", url='https://novtechschool.ru/'),
    telebot.types.InlineKeyboardButton(text="Назад", callback_data="back")
)
floor_keyboard = telebot.types.InlineKeyboardMarkup()
floor_keyboard.add(
    telebot.types.InlineKeyboardButton(text="1 этаж", callback_data="floor1"),
    telebot.types.InlineKeyboardButton(text="2 этаж", callback_data="floor2"),
    telebot.types.InlineKeyboardButton(text="Назад", callback_data="back")
)
floor1_keyboard = telebot.types.InlineKeyboardMarkup()
floor1_keyboard.add(
    telebot.types.InlineKeyboardButton(text="Выбрать этаж", callback_data="choose_floor"),
    telebot.types.InlineKeyboardButton(text="Назад", callback_data="back"),
)
floor2_keyboard = telebot.types.InlineKeyboardMarkup()
floor2_keyboard.add(
    telebot.types.InlineKeyboardButton(text="1 корпус", callback_data="building1"),
    telebot.types.InlineKeyboardButton(text="2 корпус", callback_data="building2"),
    telebot.types.InlineKeyboardButton(text="Выбрать этаж", callback_data="choose_floor"),
    telebot.types.InlineKeyboardButton(text="Назад", callback_data="back"),
)
floor1_body1_keyboard = telebot.types.InlineKeyboardMarkup()
floor1_body1_keyboard.add(
    telebot.types.InlineKeyboardButton(text="2 корпус", callback_data="body1_2"),
    telebot.types.InlineKeyboardButton(text="Выбрать этаж", callback_data="choose_floor"),
    telebot.types.InlineKeyboardButton(text="Назад", callback_data="back")
)

# Обработчик команды /start
@bot.message_handler(commands=["start"])
def start(message):
    # Отправляем сообщение с выбором языка
    bot.send_message(
        message.chat.id,
        "Выберите язык | Choose language",
        reply_markup=language_keyboard,
    )

# Обработчик inline кнопок
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call, save_message_id=None):
    # Если пользователь выбрал язык
    if call.data in ["russian"]:
        # Получаем имя пользователя
        user_name = call.message.chat.first_name

        # Отправляем сообщение с выбором раздела
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f"<b>Привет, {user_name}!</b>\n\n"
            "Я гид-бот по зданию <b>НТШ (Новгородской Технической Школы имени Ярослава Мудрого)</b>.\n\n"
            "Если ты не нашел нужной информации, то можешь задать вопрос нам напрямую:\n\n"
            "<b>Адрес:</b> г. Великий Новгород, Большая Санкт-Петербургская улица, 46, кабинет 201\n\n"
            "<b>Телефон:</b> +7(8162)90-60-55\n\n"
            "<b>Email:</b> fond-info@novtechschool.ru\n\n"
            "<b>Время работы:</b> 9:00 - 18:00\n",
            parse_mode="HTML",
            reply_markup=menu_keyboard,
        )
    if call.data in ['english']:
        user_name = call.message.chat.first_name
        # Отправляем сообщение с выбором раздела
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=f"<b>Hi, {user_name}!</b>\n\n"
                                   "I am a bot guide to the building of the <b>NTSH (Yaroslav the Wise Novgorod Technical School)</b>.\n\n"
                                   "If you haven't found the information you need, you can ask us a question directly:\n\n"
                                   "<b>Address:</B> Veliky Novgorod, Bolshaya St. Petersburg street, 46, office 201\n\n"
                                   "<b>Telephone:</b> +7(8162)90-60-55\n\n"
                                   "<b>Email:</b> fond-info@novtechschool.ru\n\n "
                                   "<b>Working hours:</b> 9:00 - 18:00\n",
                              parse_mode="HTML",
                              reply_markup=menu_keyboard1)

    elif call.data == "about":
        # Создаем inline клавиатуру для раздела "О компании"
        menu_keyboard2 = telebot.types.InlineKeyboardMarkup()
        menu_keyboard2.add(
            telebot.types.InlineKeyboardButton(
                text="Направления", callback_data="directions"
            ),
            telebot.types.InlineKeyboardButton(
                text="Как стать участником", callback_data="become_member"
            ),
            telebot.types.InlineKeyboardButton(
                text="Контакты", callback_data="contacts"
            ),
            telebot.types.InlineKeyboardButton(text="Назад", callback_data="back"),
        )
        # Отправляем сообщение с текстом "НТШ" и inline клавиатурой для раздела "О компании"
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="<b>Новгородская техническая школа (НТШ)</b> – это инфраструктурный проект, "
            "связанный с развитием прорывных (сквозных) технологий, "
            "на базе которого будут проводиться профессиональная ориентация школьников, "
            "обучение студентов, реализовываться программы опережающей профессиональной "
            "подготовки по профессиям и навыкам будущего, переподготовка и повышение квалификации, "
            "научные разработки в интересах региона, промышленных партнеров и Российской Федерации "
            "в целом, а также в перспективе, использование в качестве регионального центра коллективного "
            "пользования, создания условий для развития высокотехнологичных импортозамещающих "
            "отраслей промышленности и областей бизнеса.\n\n"
            "<b>Novgorod Technical School (NTS)</b> is an infrastructure project, "
            "related to the development of breakthrough (end–to-end) technologies, "
            "on the basis of which professional orientation of schoolchildren will be conducted, "
            "training of students, advanced professional training programs will be implemented, "
            "training in professions and skills of the future, retraining and advanced training, "
            "scientific developments in the interests of region, industrial partners and the Russian Federation "
            "in general, as well as in the future, the use as a regional center of collective "
            "use, creating conditions for the development of high-tech import-substituting "
            "industries and business areas.",
            parse_mode="HTML",
            reply_markup=menu_keyboard2,
        )

    # Если пользователь выбрал раздел "Планировка здания"
    elif call.data == "plan":
        # Отправляем сообщение с текстом "Планировка здания" и inline клавиатурой для раздела "Планировка здания"
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Планировка здания",
            reply_markup=floor_keyboard,
        )
    elif call.data == "message":
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Выберите язык | Choose language",
            reply_markup=language_keyboard,
        )

    elif call.data == "back":
        user_name = call.message.chat.first_name
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f"<b>Привет, {user_name}!</b>\n\n"
            "Я гид-бот по зданию <b>НТШ (Новгородской Технической Школы имени Ярослава Мудрого)</b>.\n\n"
            "Если ты не нашел нужной информации, то можешь задать вопрос нам напрямую:\n\n"
            "<b>Адрес:</b> г. Великий Новгород, Большая Санкт-Петербургская улица, 46, кабинет 201\n\n"
            "<b>Телефон:</b> +7(8162)90-60-55\n\n"
            "<b>Email:</b> fond-info@novtechschool.ru\n\n"
            "<b>Время работы:</b> 9:00 - 18:00\n",
            parse_mode="HTML",
            reply_markup=menu_keyboard,
        )

    elif call.data == "directions":
        # Отправляем сообщение с inline клавиатурой для выбора направления
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Разработка и создание высокотехнологичной электронно-компонентной базы, профессиональной и потребительской электроники \n\n"
                 "Разработка и создание квантовых сенсоров, устройств с использованием квантовых технологий \n\n"
                 "Разработка и создание новых, в том числе портативных, источников энергии \n\n"
                 "Разработка биомедицинских клеточных технологий \n\n"
                 "Разработка и создание мобильной сети связи 5-го поколения \n\n"
                 "Разработка и создание интернета вещей (приборы, устройства, системы, программные платформы)",
            reply_markup=directions_keyboard,
        )

    elif call.data == "become_member":
        # Отправляем сообщение с inline клавиатурой для выбора направления
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Заполняйте форму на участие",
            reply_markup=become_member_keyboard,
        )

    elif call.data == "contacts":
        # Отправляем сообщение с inline клавиатурой для выбора направления
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Наши контакты \n\n"
                 "<b>Телефон:</b> +7(8162)90-60-55",
            parse_mode="HTML",
            reply_markup=contacts_keyboard
        )

    elif call.data == "floor1":
        file = open('1 этаж 1 корпус.jpg', 'rb')
        file1 = open('1 этаж 2 корпус.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, '1 корпус'),
        bot.send_photo(call.message.chat.id, file1, '2 корпус'),

    elif call.data == "floor2":
        file = open('2 этаж 1 корпус.jpg', 'rb')
        file1 = open('2 этаж 2 корпус.jpg', 'rb')
        bot.send_photo(call.message.chat.id, file, '1 корпус'),
        bot.send_photo(call.message.chat.id, file1, '2 корпус'),

# Запускаем бота
bot.polling()