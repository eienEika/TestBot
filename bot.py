import config
import telebot

bot = telebot.Telebot(config.token)

@bot.message_handler(content_types=["text"])
def repeat(message):
	bot.send_message(message.chat.id, message.text)

