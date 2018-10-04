import config
import telebot
import os
import solve
import time

bot = telebot.TeleBot(config.token)

# path to downloaded files
if os.name is 'nt':  # if windows
	path = os.environ['HOMEPATH']
else:
	path = os.environ['HOME']
if not os.path.exists(path + os.sep + '.tmpBOT'):
	os.mkdir(path + os.sep + '.tmpBOT')
path += os.sep + '.tmpBOT' + os.sep


# @bot.message_handler(content_types=["text"])
# def repeat(message):
#	bot.send_message(message.chat.id, message.text)


@bot.message_handler(content_types=['document'])
def get_file(message):
	file_info = bot.get_file(message.document.file_id)
	downloaded_file = bot.download_file(file_info.file_path)

	file_name = str(time.time())    # creating unique dir and file names
	file_dir = path + file_name
	os.mkdir(file_dir)
	src = file_dir + os.sep + file_name
	with open(src, 'wb') as file:
		file.write(downloaded_file)
	file.close()
	bot.reply_to(message, "Файл добавлено")

	out = solve.solve(src)
	os.remove(src)

	if out is None:
		bot.send_message(message.chat.id, "No solution")
	elif len(out) > 10:   # if system is big then bot will send you answer in out file
		out_file = open(file_dir + os.sep + 'out.txt', 'w+')
		for i in out:
			out_file.write(str(i) + '=' + str(out[i]) + '\n')
		out_file = open(file_dir + os.sep + 'out.txt', 'r')
		bot.send_document(message.chat.id, out_file)
		out_file.close()
		os.remove(file_dir + os.sep + 'out.txt')
		os.rmdir(file_dir)
	else:
		out_message = ''
		for i in out:
			out_message += str(i) + '=' + str(out[i]) + '\n'
		bot.send_message(message.chat.id, out_message)


if __name__ == '__main__':
	bot.polling(none_stop=True)


