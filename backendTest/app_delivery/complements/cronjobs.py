from bot import Bot_Slack

def hi():
    text="Send a message from another function"
    Bot_Slack(text).send_message()
    print("taskComplete")  