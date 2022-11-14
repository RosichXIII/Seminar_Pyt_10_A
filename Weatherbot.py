import telebot
import requests

bot = telebot.TeleBot('5711638068:AAFergmX5gtya3X4L0o9DtGQbF-mK__M-l8')

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, 'Выберите город:')
        bot.register_next_step_handler(message, weather)
    else:
        bot.send_message(message.from_user.id, 'Введите команду */start*')

def weather(message):
    name = message.text
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={name}&appid=4321a3d417b53045aa1b6617c529c910&units=metric&lang=ru")
    weather = response.json()['weather'][0]['description']
    temp = response.json()['main']['temp']
    temp_feeling = response.json()['main']['feels_like']
    bot.send_message (message.from_user.id, f'Погода в городе{name}:\n{weather}\nтемпература воздуха: {temp}\nощущается как: {temp_feeling}')

bot.polling(none_stop=True, interval=0)
