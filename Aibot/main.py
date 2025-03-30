
import telebot
import requests
from model import get_class

# Замени 'YOUR_TELEGRAM_BOT_TOKEN' на токен своего бота
bot = telebot.TeleBot('7846154698:AAHjHHkNXJ_WdTFE7OqmXWeDpiRtoBHN1Bk')

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Привет! Я бот для получения изображений уток и анализа изображений. Используй команду /duck для получения изображения утки. Отправь фото для анализа изображения")

@bot.message_handler(commands=['duck'])
def duck(message):
    '''По команде /duck возвращает фото утки'''
    image_url = get_duck_image_url()
    bot.send_message(message.chat.id, image_url)

@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    '''При отправке изображения, проводит его анализ'''
    # Проверяем, есть ли фотографии
    if not message.photo:
        return bot.send_message(message.chat.id, "Вы забыли загрузить картинку :(")

    # Получаем файл и сохраняем его
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]

    # Загружаем файл и сохраняем
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    # Анализируем изображение
    result = get_class(model_path="keras_model.h5", labels_path="labels.txt", image_path=file_name)
    bot.send_message(message.chat.id, result)

# Запускаем бота
bot.polling()