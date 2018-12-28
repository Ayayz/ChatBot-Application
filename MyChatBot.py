from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot= ChatBot('Bot')
bot.set_trainer(ListTrainer)

for files in os.listdir('/path of ChatterBot Corpus/')
	data=open('/path of corpus')
	bot.train(data)
	
while True:
	message=input('You:')
	if message.strip()!= 'Bye':
		reply=bot.get_respose(message)
		print('ChatBot:', reply)

	if message.strip() ==  'Bye':
		print('ChatBot: Bye')
		break