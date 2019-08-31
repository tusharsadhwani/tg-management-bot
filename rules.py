import os.path

import defaults

def rules(bot, update):
    msg = update.message
    chat_id = update.message.chat_id

    if chat_id != defaults.chat_id: return	
    
    if os.path.exists('rules.txt'):
        try:
            with open('rules.txt') as f:
                rules = f.read().strip()
        except:
            rules = None
    else:
        rules = None
    
    if rules:
        rules = rules.replace('_', r'\_')
        bot.send_message(chat_id = msg.chat_id, 
                         text = f"*Rules:*\n{rules}",
                         reply_to_message_id = msg.message_id,
                         parse_mode = 'Markdown')
    else:
        bot.send_message(chat_id = msg.chat_id, 
                         text = "_There are no rules set for this chat._",
                         reply_to_message_id = msg.message_id,
                         parse_mode = 'Markdown')

def setrules(bot, update):
    msg = update.message
    chat_id = msg.chat_id
    
    if chat_id != defaults.chat_id: return

    setter = bot.get_chat_member(chat_id, msg.from_user.id)['status']

    if setter in ["administrator", "creator"]:
        msg_list = msg.text.split("\n", 1)
        if len(msg_list) > 1:
            rules = msg_list[1].strip()

            if rules:
                with open('rules.txt', 'w') as f:
                    f.write(rules)

                bot.send_message(chat_id = msg.chat_id, 
                            text = "Rules added!", 
                            reply_to_message_id = msg.message_id,
                            parse_mode = 'Markdown')
                return
            
        bot.send_message(chat_id = msg.chat_id, 
                         text = "*Format:*\n/setrules\n_rule 1\nrule 2_", 
                         reply_to_message_id = msg.message_id,
                         parse_mode = 'Markdown')
    else:
        bot.send_message(chat_id = msg.chat_id, 
                         text = "Fuck off.", 
                         reply_to_message_id = msg.message_id,
                         parse_mode = 'Markdown')