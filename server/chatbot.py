from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

la_params = [{'import_path': 'chatterbot.logic.BestMatch'},{'import_path': 'chatterbot.logic.LowConfidenceAdapter','threshold': 0.70,'default_response': "I am sorry, I didn't understand."}]

def generate_response(message):
    bot = ChatBot('Bot', storage_adapter='chatterbot.storage.SQLStorageAdapter', logic_adapters=la_params, trainer='chatterbot.trainers.ListTrainer')
    bot.set_trainer(ListTrainer)
    while True:
        if message.strip()!= 'Bye':
            reply = bot.get_response(message)                        
            reply = str(reply)
            return {"chatbot_message" : reply}
        if message.strip() == 'Bye':
            return {"chatbot_message" : "Bye"}
        