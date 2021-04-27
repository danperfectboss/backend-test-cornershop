import slack
import os
from pathlib import Path
from dotenv import load_dotenv

class Bot_Slack:
    
    def __init__(self, text):
        self.client = slack.WebClient(token="xoxb-974816393074-1989003701255-azhrmau374nDvHaZ3lkeZzOj")
        # self.channel = "#backen-test-cornershop"
        self.channel = "#test"
        self.text=text

    def send_message(self):
        try:
            self.client.chat_postMessage(channel=self.channel, text=self.text)
        except:
            print("Message can't be send it")