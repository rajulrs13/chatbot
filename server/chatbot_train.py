from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

def chat_bot_train():
    chatbot = ChatBot('Bot', storage_adapter='chatterbot.storage.SQLStorageAdapter', trainer='chatterbot.trainers.ListTrainer')
    chatbot.set_trainer(ListTrainer)
    for file in os.listdir('training_data/'):
        file_data = open('training_data/' + file, 'r').readlines()
        chatbot.train(file_data)
    return {"code":"success"}