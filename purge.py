import defaults

def purge(bot, update):
    msg = update.message
    chat_id = msg.chat_id
    user_id = msg.from_user.id
    msg_id = msg.message_id

    if chat_id != defaults.chat_id: return


    user = bot.get_chat_member(chat_id, user_id)

    if user['status'] in ["creator", "administrator"]:
        msg_list = msg.text.split(' ', 1)
        if len(msg_list) > 1:
            try:
                purge_limit = int(msg_list[1])
            except:
                bot.send_message(chat_id = chat_id, 
                                text = "Format:\n/purge <number>",
                                reply_to_message_id = msg_id)
        elif msg.reply_to_message:
            purge_limit = msg_id - msg.reply_to_message.message_id
        else:
            bot.send_message(chat_id = chat_id, 
                                text = "Format:\n/purge <number>",
                                reply_to_message_id = msg_id)
            return
        
        for lim in range(1, purge_limit + 1):
            msg_to_delete = msg_id - lim

            try:
                bot.delete_message(chat_id, msg_to_delete)
            except:
                pass

        bot.send_message(chat_id = chat_id, 
                        text = "Purge complete.",
                        reply_to_message_id = msg_id)
