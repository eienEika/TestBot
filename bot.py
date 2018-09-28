import config
import telebot
import numpy
import os

bot = telebot.TeleBot(config.token)


def solve(file):
	handle = open(file, 'r')
	row = int(handle.readline())
	col = int(handle.readline())
	b = [float(x) for x in handle.readline().split()]

	A = []
	for i in range(0, row):
		A.append([float(x) for x in handle.readline().split()])
	handle.close()
	print(A)
	print(b)
	x = numpy.linalg.lstsq(A, b, rcond=None)
	print(x)
	return x


@bot.message_handler(content_types=["text"])
def repeat(message):
	bot.send_message(message.chat.id, message.text)


@bot.message_handler(content_types=['document'])
def get_file(message):
	file_info = bot.get_file(message.document.file_id)
	downloaded_file = bot.download_file(file_info.file_path)

	src = 'D:\\qot\\' + message.document.file_name
	with open(src, 'wb') as file:
		file.write(downloaded_file)
	file.close()
	bot.reply_to(message, "Файл добавлено")

	out = solve(src)[0]
	if len(out) > 10:
		out_file = open('D:\\qot\\out.txt', 'w+')
		for i in out:
			out_file.write(str(i) + '\n')
		out_file = open('D:\\qot\\out.txt', 'r')
		bot.send_document(message.chat.id, out_file)
		out_file.close()
		os.remove('D:\\qot\\out.txt')
	else:
		out_message = ''
		for i in out:
			out_message += str(i) + '\n'
		bot.send_message(message.chat.id, out_message)


if __name__ == '__main__':
	bot.polling(none_stop=True)

