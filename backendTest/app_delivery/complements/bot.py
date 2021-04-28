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

#se genera el canal con el cliente de slack aqui va el token
CLIENT = slack.WebClient(token="token goes here")
# canal en el cual va a ser deplegado el mensaje
CHANNEL = "#backend_test"


#con celery se crea esta tarea compartida para enviarlo de manera asincrona
@shared_task
def send_message(text):
    try:
        #envia el mensaje al canal asignado previamente
        CLIENT.chat_postMessage(channel=CHANNEL, text=text)
    except:
        print("Message can't be send it")