import requests

url = "https://api.telegram.org/bot1405208821:AAEU7UalGaxxqUZcdXAHLOaZUMHOx_hJtpk/"


#? returns the chat id
def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id


#? returns the text of the message
def get_message_text(update):
    message_text = update['message']['text']
    return message_text

#? returns the last update
def last_update(req):
    response = requests.get(req + "getUpdates")
    response = response.json()
    result = response['result']
    total_updates = len(result) -1 
    return result[total_updates]
    
#? returns the response due to the sended message
def send_message(chat_id, message_text):
    params = {"chat_id": chat_id, "text":message_text}
    response = requests.post(url+'sendMessage', data=params)
    return response



def main():
    update_id = last_update(url)['update_id']
    while True:
        update = last_update(url)
        if update_id == update['update_id']:
            if get_message_text(update).lower() == "hi":
                send_message(get_chat_id(update), "Hey Welcome to our bot")
            elif get_message_text(update).lower() == "how are you":
                send_message(get_chat_id(update), "i am great") 
            elif get_message_text(update).lower() == "what's your name":
                send_message(get_chat_id(update), "my name is python")
            else:
                send_message(get_chat_id(update), "I didn't understand what you just said!")
            update_id+=1
        
main()