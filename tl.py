import requests
import defaults

def tl(bot, update):
    msg = update.message
    chat_id = msg.chat_id

    if chat_id != defaults.chat_id: return	
    
    text = ''
    if msg.reply_to_message:
        text += msg.reply_to_message.text
    else:
        msg_list = msg.text.strip().split(' ', 1)
        if len(msg_list) > 1:
            text += msg_list[1].strip().replace('&', '').replace('_', r'\_').replace('*', r'\*').replace('`', r'\`')

    key = defaults.tl_api_key
    url = f'https://translate.yandex.net/api/v1.5/tr.json/translate?key={key}&text={text}&lang=en'

    response = requests.get(url)
    data = response.json()

    reply = ''
    
    if data['code'] == 502:
        reply += "H*ck off."
    elif data['code'] != 200:
        reply += f"Something went wrong, Error {data['code']}"
    else:
        reply_text = '\n'.join(data['text'])
        reply += f"*{data['lang']}:*\n{reply_text}"

    bot.send_message(chat_id = msg.chat_id, 
                     text = reply, 
                     reply_to_message_id = msg.message_id,
                     parse_mode = 'Markdown')