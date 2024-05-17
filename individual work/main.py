import telebot
from currency_converter import CurrencyConverter
from telebot import types

bot = telebot.TeleBot('7169851532:AAFJy2K2dWmrXtKOgyF18JtlcFgx8EPHJgc')
currency = CurrencyConverter()
amount = 0
income = 0
expenses = []

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton('Конвертация валют💰', callback_data='convert_currency')
    btn2 = types.InlineKeyboardButton('Планировщик бюджета📝', callback_data='budget_planner')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Привет, я biz ваш личный помощник. Я умею конвертировать валюты и планировать ваш бюджет исходя из ваших доходов и расходов! Чем я могу вам помочь? Выберите действие:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ['convert_currency', 'budget_planner', 'continue'])
def handle_choice(call):
    if call.data == 'convert_currency':
        start_currency_converter(call.message)
    elif call.data == 'budget_planner':
        start_budget_planner(call.message)
    elif call.data == 'continue':
        continue_currency_converter(call.message)

def start_currency_converter(message):
    bot.send_message(message.chat.id, 'Введите сумму для конвертации:')
    bot.register_next_step_handler(message, summa)

def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат, введите сумму.')
        bot.register_next_step_handler(message, summa)
        return

    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
        btn2 = types.InlineKeyboardButton('EUR/BGN', callback_data='eur/bgn')
        btn3 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        btn4 = types.InlineKeyboardButton('другое значение', callback_data='else')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Выберите пару валют.', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Число должно быть больше 0.')
        bot.register_next_step_handler(message, summa)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data in ['usd/gbp', 'eur/bgn', 'eur/usd']:
        values = call.data.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f'Получается: {round(res, 2)}. Можете заново вписать сумму.')

        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('Продолжить💰', callback_data='continue')
        btn2 = types.InlineKeyboardButton('Планировщик бюджета📝', callback_data='budget_planner')
        markup.add(btn1, btn2)

        bot.send_message(call.message.chat.id, 'Что вы хотите сделать дальше?', reply_markup=markup)
    elif call.data == 'else':
        bot.send_message(call.message.chat.id, 'Введите пару значений через слэш.')
        bot.register_next_step_handler(call.message, my_currency)
    elif call.data == 'budget_planner':
        start_budget_planner(call.message)
    elif call.data == 'convert_currency':
        start_currency_converter(call.message)
    elif call.data in ['yes', 'no']:
        expense_choice(call)

def my_currency(message):
    try:
        values = message.text.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f'Получается: {round(res, 2)}. Можете заново вписать сумму.')

        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('Продолжить💰', callback_data='continue')
        btn2 = types.InlineKeyboardButton('Планировщик бюджета📝', callback_data='budget_planner')
        markup.add(btn1, btn2)

        bot.send_message(message.chat.id, 'Что вы хотите сделать дальше?', reply_markup=markup)
    except Exception:
        bot.send_message(message.chat.id,
                         'Возникла ошибка. Возможно, введенная валюта не поддерживается. Пожалуйста, введите пару заново.')
        bot.register_next_step_handler(message, my_currency)

def continue_currency_converter(message):
    bot.send_message(message.chat.id, 'Введите сумму для конвертации:')
    bot.register_next_step_handler(message, summa)

def start_budget_planner(message):
    bot.send_message(message.chat.id, 'Введите ваш доход в EUR:')
    bot.register_next_step_handler(message, set_income)

def set_income(message):
    global income
    try:
        income = float(message.text.strip())
        bot.send_message(message.chat.id,
                         'Ваш доход успешно установлен. Теперь введите ваш первый расход в формате "Описание: сумма" (например, "Еда: 50"):')
        bot.register_next_step_handler(message, add_expense)
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат, введите доход в числовом формате.')
        bot.register_next_step_handler(message, set_income)

def add_expense(message):
    global expenses
    try:
        description, amount = message.text.split(':')
        amount = float(amount.strip())
        expenses.append((description.strip(), amount))
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('Да', callback_data='yes')
        btn2 = types.InlineKeyboardButton('Нет', callback_data='no')
        btn3 = types.InlineKeyboardButton('Перейти к конвертации валют💰', callback_data='convert_currency')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, 'Расход добавлен. Хотите добавить еще один расход?', reply_markup=markup)
    except ValueError:
        bot.send_message(message.chat.id,
                         'Неверный формат, введите расход в формате "Описание: сумма" (например, "Еда: 50").')
        bot.register_next_step_handler(message, add_expense)

def expense_choice(call):
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, 'Введите следующий расход в таком же формате.')
        bot.register_next_step_handler(call.message, add_expense)
    elif call.data == 'no':
        calculate_balance(call.message)

def calculate_balance(message):
    total_expenses = sum(amount for description, amount in expenses)
    balance = income - total_expenses
    advice = 'Все в порядке с вашим бюджетом👍.' if balance >= 0 else 'Ваши расходы превышают доходы, попробуйте сократить расходы📉.'

    expense_details = '\n'.join([f'{description}: {amount}' for description, amount in expenses])
    response = (
        f'Ваш бюджет:\nДоход: {income} EUR\n\nРасходы:\n{expense_details}\n\nИтого расходов: {total_expenses} EUR\n'
        f'Оставшийся баланс: {balance} EUR\n\nСовет: {advice}')

    bot.send_message(message.chat.id, response)

    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton('Продолжить📝', callback_data='budget_planner')
    btn2 = types.InlineKeyboardButton('Конвертировать валюты💰', callback_data='convert_currency')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Что вы хотите сделать дальше?', reply_markup=markup)

bot.polling(none_stop=True)
