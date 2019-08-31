import os.path
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

import defaults

def welcome(bot, update):
    msg = update.message
    chat_id = update.message.chat_id

    if chat_id != defaults.chat_id: return

    if msg.new_chat_members:
        if os.path.exists('welcome.txt'):
            try:
                with open('welcome.txt') as f:
                    welcome_msg = f.read().strip()
            except:
                return
        else:
            return
        
        if not welcome_msg: return

        user_name = msg.new_chat_members[0]['username']
        botusername = bot.get_me().username
        reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Rules", url = f't.me/{botusername}?start=rules')]])
        
        if user_name: 
            user_name = user_name.replace("_", r"\_")

        bot.send_message(chat_id=msg.chat_id, 
                         text=welcome_msg, 
                         reply_to_message_id=msg.message_id,
                         reply_markup=reply_markup)

def setwelcome(bot, update):
    msg = update.message
    chat_id = update.message.chat_id

    if chat_id != defaults.chat_id: return
    
    setter = bot.get_chat_member(chat_id, msg.from_user.id)['status']

    if setter in ["administrator", "creator"]:
        msg_list = msg.text.split(" ", 1)
        if len(msg_list) > 1:
            welcome_text = msg_list[1]
            
            with open('welcome.txt', 'w') as f:
                f.write(welcome_text)
            
            bot.send_message(chat_id = msg.chat_id, 
                         text = "Welcome message set!", 
                         reply_to_message_id = msg.message_id,
                         parse_mode = 'Markdown')
        else:
            bot.send_message(chat_id = msg.chat_id, 
                         text = "*Format:*\n/setwelcome _welcome message_", 
                         reply_to_message_id = msg.message_id,
                         parse_mode = 'Markdown')
    else:
        bot.send_message(chat_id = msg.chat_id, 
                         text = "Fuck off.", 
                         reply_to_message_id = msg.message_id,
                         parse_mode = 'Markdown')