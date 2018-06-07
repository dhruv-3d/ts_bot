import webbrowser as wb
import urllib3
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot(
        "TeaTea",
        storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
        input_adapter = 'chatterbot.input.TerminalAdapter',
        output_adapter = 'chatterbot.output.TerminalAdapter',
        database = './database.sqlite3'
)

conversation = [
    "Hello",
    "Hello, How can I help you?",
    "Open my timesheet.",
    "Ok, Here's your timesheet."
]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)

print("Say hello to " +chatbot.name+ "...\n")

while True:
    try:
        chatbot_input = chatbot.get_response(None)

        ip = []
        ip = chatbot_input.split()

        if 'timesheet.' in ip:
            url = "http://192.168.1.201:81/EasyCollab/time_sheets"
            wb.get("chrome").open(url)
    except(KeyboardInterrupt, SystemExit):
        break
