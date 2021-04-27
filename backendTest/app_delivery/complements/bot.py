import slack

from celery import shared_task

# class Bot_Slack:
   
#     def __init__(self, text):
#         self.client = slack.WebClient(token="xoxb-974816393074-1989003701255-FuPS0TNCcmyA84or8NMkgMWV")
#         # self.CHANNEL = "#backen-test-cornershop"
#         self.channel = "#test"
#         self.text=text
    
#     @shared_task(self)
#     def send_message(self):
#         try:
#             self.client.chat_postMessage(channel=self.channel, text=self.text)
#         except:
#             print("Message can't be send it")

CLIENT = slack.WebClient(token="")
#CHANNEL = "#backen-test-cornershop"
CHANNEL = "#test"

@shared_task
def send_message(text):
    try:
        CLIENT.chat_postMessage(channel=CHANNEL, text=text)
    except:
        print("Message can't be send it")