import config
import telebot
import numpy
import os

bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=["text"])
def repeat(message):
	bot.send_message(message.chat.id, message.text)


@bot.message_handler(content_types=['document'])
def files(message):
	file_info = bot.get_file(message.document.file_id)
	downloaded_file = bot.download_file(file_info.file_path)

	src = 'D:\\qot\\' + message.document.file_name
	with open(src, 'w') as file:
		file.write(downloaded_file)

	bot.reply_to(message, "Файл добавлено")


if __name__ == '__main__':
	bot.polling(none_stop=True)

