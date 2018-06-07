# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import webbrowser as wb
import tkinter as tk
try:
    import ttk as ttk
    import ScrolledText
except ImportError:
    import tkinter.ttk as ttk
    import tkinter.scrolledtext as ScrolledText
import time
from parse_webpage import TimeSheetInfo

class BotGUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        """
        Create & set window and bot variables.
        """
        tk.Tk.__init__(self, *args, **kwargs)

        self.chatbot = ChatBot(
            "Sbot",
            storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
            logic_adapters=[
                "chatterbot.logic.BestMatch"
            ],
            filters=[
                'chatterbot.filters.RepetitiveResponseFilter'
            ],
            input_adapter="chatterbot.input.VariableInputTypeAdapter",
            output_adapter="chatterbot.output.OutputAdapter",
            database='chatterbot-database'
        )

        self.title("Chatterbot")

        self.initialize()
        self.train_bot()


    def initialize(self):
        """
        Setup bot UI.
        """
        self.grid()

        self.respond = ttk.Button(self, text='Get Response', command=self.get_response)
        self.respond.grid(column=1, row=0, sticky='nesw', padx=3, pady=3)
        
        self.usr_input = ttk.Entry(self, state='normal')
        self.usr_input.grid(column=0, row=0, sticky='nesw', padx=3, pady=3)
        self.usr_input.bind('<Return>', self.get_response)

        self.conversation_lbl = ttk.Label(self, anchor=tk.W, text='Conversation:')
        self.conversation_lbl.grid(column=0, columnspan=2, row=1, sticky='nesw', padx=3, pady=3)

        self.conversation = ScrolledText.ScrolledText(self, state='disabled')
        self.conversation.grid(column=0, row=2, columnspan=2, sticky='nesw', padx=3, pady=3)

    def train_bot(self):
        """
        You can set content for ListTrainers here to train your chatbot.
        """
        self.td = [
            "Hello",
            "Hello, How can I help you?",
            "Open my timesheet.",
            "Ok, Here's your timesheet."
        ]

        self.chatbot.set_trainer(ListTrainer)
        self.chatbot.train(self.td)

    def get_response(self, event=None):
        """
        Get a response from the chatbot and display it.
        """
        user_input = self.usr_input.get()
        self.usr_input.delete(0, tk.END)

        # response = self.gen_resp(user_input)
        response = self.chatbot.get_response(user_input)

        self.conversation['state'] = 'normal'
        self.conversation.insert(
            tk.END, "Human: " + user_input + "\n" + "ChatBot: " + str(response.text) + "\n"
        )
        self.conversation['state'] = 'disabled'
        
        time.sleep(0.5)
        self.do_stuff(response)

    def gen_resp(user_input):
        ip = []
        ip = user_input.split()
        if('timesheet' in ip):
            response = self.do_stuff()
        else:
            response = self.chatbot.get_response(user_input)
            return response

    def do_stuff(self, response):
        """
        You can call the fucntions here for the stuff to be done by the bot on particular resp.
        """
        
        # pr_list = TimeSheetInfo.fetch_project_info()
        #aa bhangar che.. dynamic banavanu che
        # resp = 'Please select your project: \n' + pr_list[0] + '\n' + pr_list[1] + '\n'

        return response
        # open timesheet in browser
        # url = "http://192.168.1.201:81/EasyCollab/time_sheets"
        # wb.get("chrome").open(url)

bot_gui = BotGUI()
bot_gui.mainloop()