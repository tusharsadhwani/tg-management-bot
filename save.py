import pickle
import os.path

import defaults

def add_save(bot, update):
    chat_id = update.message.chat_id
    msg = update.message.text

    if chat_id != defaults.chat_id: return

    user = bot.get_chat_member(chat_id, update.message.from_user.id)['status']

    if os.path.exists('saves.db'):
        with open('saves.db', 'rb') as f:
            try:
                save_dict = pickle.load(f)
            except:
                save_dict = {}
    else:
        save_dict = {}
    
    if user in ["administrator", "creator"]:
        if '-' in msg:
            msg_list = msg.split(' ', 1)[1].split('-', 1)
            save_name = msg_list[0].strip().lower()

            if msg_list[1]:
                response = msg_list[1].strip()

                if save_name not in save_dict.keys():
                    save_dict[save_name] = response

                    with open('saves.db', 'wb') as f:
                        pickle.dump(save_dict, f)

                    text = f'`!{save_name}` succesfully added'
                    bot.send_message(chat_id = update.message.chat_id, text = text, parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
                    return
                else:
                    text = f'A note already exists by the name `{save_name}`'
                    bot.send_message(chat_id = update.message.chat_id, text = text, parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
                    return

            bot.send_message(chat_id = update.message.chat_id, text = r'*Format:*\n/save _note_\__name_ - _response_', parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
    else:
        bot.send_message(chat_id = update.message.chat_id, text = 'Fuck off.', parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
        
def check_saves(bot, update):
    msg = update.message
    chat_id = msg.chat_id

    if chat_id != defaults.chat_id: return

    reply_id = msg.reply_to_message.message_id if msg.reply_to_message else msg.message_id

    if os.path.exists('saves.db'):
        with open('saves.db', 'rb') as f:
            try:
                save_dict = pickle.load(f)
            except:
                save_dict = {}
    else:
        save_dict = {}

    txt = msg.text.lower()
    for trigger in save_dict.keys():
        if txt.startswith(f'!{trigger}'):
            bot.send_message(chat_id = chat_id, text = save_dict[trigger], reply_to_message_id = reply_id)

def save_list(bot, update):
    chat_id = update.message.chat_id
    chat_title = update.message.chat.title

    if chat_id != defaults.chat_id: return

    if os.path.exists('saves.db'):
        with open('saves.db', 'rb') as f:
            try:
                save_dict = pickle.load(f)
            except:
                save_dict = {}
    else:
        save_dict = {}
    
    if save_dict:
            msg = f'Saves for {chat_title}:\n'
            save_list = save_dict.keys()
            for save_name in save_list:
                msg += f'`!{save_name}`\n'
            bot.send_message(chat_id = update.message.chat_id, text = msg, parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
    else:
        bot.send_message(chat_id = update.message.chat_id, text = 'Notes have not been added yet. Use /save to add', parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
    
def remove_save(bot, update):
    chat_id = update.message.chat_id
    msg = update.message.text
    
    user = bot.get_chat_member(chat_id, update.message.from_user.id)['status']
    if user in ["administrator", "creator"]:
        msg_list = msg.strip().split(' ', 1)

        if len(msg_list) == 2:

            if os.path.exists('saves.db'):
                with open('saves.db', 'rb') as f:
                    try:
                        save_dict = pickle.load(f)
                    except:
                        save_dict = {}
            else:
                save_dict = {}

            trigger = msg_list[1].lower().strip()
            if trigger in save_dict.keys():
                del save_dict[trigger]

                with open('saves.db', 'wb') as f:
                    pickle.dump(save_dict, f)

                bot.send_message(chat_id = update.message.chat_id, text = f'Successfully deleted `!{trigger}`', parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
            else:
                bot.send_message(chat_id = update.message.chat_id, text = "That note doesn't exist.", parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
        else:
            bot.send_message(chat_id = update.message.chat_id, text = r"*Format:*\n/stop _save_\__name_", parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
    else:
        bot.send_message(chat_id = update.message.chat_id, text = "H*ck off.", parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)