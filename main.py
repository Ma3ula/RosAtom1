import telebot
from telebot import types

TOKEN = '7948332571:AAEHSn0qqw6a8_77gCXob90fscUPx-KK20I'
bot = telebot.TeleBot(TOKEN)

# Словарь с данными о предметах и их фото
data = {
    "Нимбы": "https://otvet.imgsmail.ru/download/b6bec61ad659382cd909c7fcf1921a1f_i-302.jpg",
    "Наушники": "https://cdn1.ozone.ru/s3/multimedia-7/6424067911.jpg",
    "Нейтроны": "https://avatars.mds.yandex.net/i?id=5d3c97aefe0960ca281feceea768d7ff_l-4310964-images-thumbs&n=13",
    "Наст": "https://avatars.mds.yandex.net/i?id=3d5b7f7a92db676dfdb0f6065e459df7_l-4767749-images-thumbs&n=13",
    "Носы": "https://www.meme-arsenal.com/memes/6d6374a0c5862438a8f156db3ca19117.jpg",
    "Нимф": "https://avatars.mds.yandex.net/i?id=bfb2d8c523742ef8126f457a7ca5381acd79457c-10637828-images-thumbs&n=13",
    "Нитрогениум": "https://reword.su/online/api/image/?wordId=855&file=b1_0019b.jpg&dict=bd"
}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Как в книге Лема, я выдам  информацию с фотографиями следующих слов: Нимбы, Наушники, Нейтроны, Наст, Носы, Нимф и Нитрогениум. Напиши «информация», чтобы получить информацию о предметах.")

@bot.message_handler(func=lambda message: message.text.lower() == 'информация')
def send_info(message):
    for item in data:
        bot.send_message(message.chat.id, f"Информация о {item}:")
        bot.send_photo(message.chat.id, data[item])

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Я не понимаю. Напиши 'информация' для получения данных.")

if __name__ == "__main__":
    bot.polling(none_stop=True)