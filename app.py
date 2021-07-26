#Python libraries that we need to import for our bot
import random
import os
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
bot = Bot(ACCESS_TOKEN)

#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                if message['message'].get('text'):
                    response_sent_text = get_message(message['message'].get('text'))
                    send_message(recipient_id, response_sent_text)
    return "Message Processed"


def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


#chooses a random message to send to the user
def get_message(message):
    if "!hatch" in message:
        maxLevel = [int(i) for i in message.split() if i.isdigit()]
        if len(maxLevel) > 0:
            dinoLevel = random.randrange(5, maxLevel[0])
            spawnLevel = dinoLevel / 1.5
            dinoCount = get_dino_count()
            response = "You had " + str(dinoCount) + " babies, level " + str(dinoLevel) + ", spawn level " + str(int(spawnLevel))
            return response
        else:
            return "Unable to process your request, try again in format '!hatch <maxLevel>"

def get_dino_count():
    roll = random.randrange(1, 100)
    if roll in range(1,2):
        return 3
    elif roll in range(3,12):
        return 2
    else:
        return 1

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
    app.run()