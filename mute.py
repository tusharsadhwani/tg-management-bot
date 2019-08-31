import time
import defaults

def mute(bot, update):
    msg = update.message
    chat_id = msg.chat_id
    
    if chat_id != defaults.chat_id: return


    user = bot.get_chat_member(chat_id=chat_id, user_id=msg.from_user.id)['status']
    try:
        muted = bot.get_chat_member(chat_id=chat_id, user_id=msg.reply_to_message.from_user.id)['status']
    except:
        bot.send_message(chat_id = msg.chat_id, 
                             text = "Reply to the person you want to mute.", 
                             reply_to_message_id = msg.message_id,
                             parse_mode = 'Markdown')
        return

    if user in ["administrator", "creator"]:
        user_name = msg.reply_to_message.from_user.username or msg.reply_to_message.from_user.first_name
        
        if muted == 'member':
            text = msg.text.split()
            if len(text)>1:
                times = text[1]
                print(times)
                try:
                    times = int(times)
                except:
                    bot.send_message(chat_id = msg.chat_id, 
                             text = "*Format:*\n_/mute time (in seconds)_", 
                             reply_to_message_id = msg.message_id,
                             parse_mode = 'Markdown')
                    return
                occurance = bot.restrict_chat_member(chat_id = chat_id, user_id = msg.reply_to_message.from_user.id, until_date = int(time.time())+(times), can_send_messages = False)
                if occurance:
                    bot.send_message(chat_id = msg.chat_id, 
                             text = f"Restricted @{user_name} for {times} seconds.", 
                             reply_to_message_id = msg.message_id)
                else:
                    bot.send_message(chat_id = msg.chat_id, 
                             text = "Couldn't restrict. Maybe I'm not admin...", 
                             reply_to_message_id = msg.message_id,
                             parse_mode = 'Markdown')
            else:
                occurance = bot.restrict_chat_member(chat_id = chat_id, user_id = msg.reply_to_message.from_user.id, can_send_messages = False)
                if occurance:
                    bot.send_message(chat_id = msg.chat_id, 
                         text = f"Restricted @{user_name}", 
                         reply_to_message_id = msg.message_id)
                else:
                    bot.send_message(chat_id = msg.chat_id, 
                         text = "Couldn't restrict. Maybe I'm not admin...", 
                         reply_to_message_id = msg.message_id,
                         parse_mode = 'Markdown')
        elif muted in ['left', 'kicked']:
                bot.send_message(chat_id = msg.chat_id, 
                             text = "The person is not in the chat anymore.", 
                             reply_to_message_id = msg.message_id,
                             parse_mode = 'Markdown')
        elif muted in ['administrator', 'creator']:
                bot.send_message(chat_id = msg.chat_id, 
                             text = "I wish I could restrict admins.", 
                             reply_to_message_id = msg.message_id,
                             parse_mode = 'Markdown')
        elif muted == 'restricted':
            bot.send_message(chat_id = msg.chat_id, 
                             text = "User is already restricted.", 
                             reply_to_message_id = msg.message_id,
                             parse_mode = 'Markdown')
    else:
        bot.send_message(chat_id = msg.chat_id, 
                             text = "H*ck off.", 
                             reply_to_message_id = msg.message_id,
                             parse_mode = 'Markdown')

def unmute(bot, update):
    msg = update.message
    chat_id = msg.chat_id

    if chat_id != defaults.chat_id: return

    user = bot.get_chat_member(chat_id = chat_id, user_id = msg.from_user.id)['status']
    try:
        muted = bot.get_chat_member(chat_id = chat_id, user_id = msg.reply_to_message.from_user.id)['status']
    except:
        bot.send_message(chat_id = msg.chat_id, 
                             text = "Please reply to the person you want to mute.", 
                             reply_to_message_id = msg.message_id,
                             parse_mode = 'Markdown')
        return

    if user in ["administrator", "creator"]:
        if muted == 'restricted':
            occurance = bot.restrict_chat_member(chat_id = chat_id, user_id = msg.reply_to_message.from_user.id, can_send_messages = True, can_send_media_messages = True, can_send_other_messages = True, can_add_web_page_previews = True)
            if occurance:
                bot.send_message(chat_id = msg.chat_id, 
                             text = f"Unrestricted @{msg.reply_to_message.from_user.username}", 
                             reply_to_message_id = msg.message_id)
            else:
                bot.send_message(chat_id = msg.chat_id, 
                             text = "Couldn't unrestrict. Maybe I'm not admin...", 
                             reply_to_message_id = msg.message_id,
                             parse_mode = 'Markdown')
        else:
            bot.send_message(chat_id = msg.chat_id, 
                             text = "The user isn't restricted.", 
                             reply_to_message_id = msg.message_id,
                             parse_mode = 'Markdown')
    else:
        bot.send_message(chat_id = msg.chat_id, 
                             text = "H*ck off.", 
                             reply_to_message_id = msg.message_id,
                             parse_mode = 'Markdown')
