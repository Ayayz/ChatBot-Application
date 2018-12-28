from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os


while True:
	message=input('You:')
	if message.strip()!= 'Bye':
		reply=bot.get_respose(message)
		print('ChatBot:', reply)

	if message.strip() ==  'Bye':
		print('ChatBot: Bye')
		break