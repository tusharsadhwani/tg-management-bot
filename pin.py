import defaults

def pin(bot, update):
    msg = update.message
    chat_id = msg.chat_id

    if chat_id != defaults.chat_id: return


    user = bot.get_chat_member(chat_id = chat_id, user_id = msg.from_user.id)['status']

    if user in ["administrator", "creator"]:
        try:
            bot.pin_chat_message(chat_id = chat_id, message_id = msg.reply_to_message.message_id, disable_notification = True)
        except:
            bot.send_message(chat_id = chat_id, text = "Couldn't pin message. Maybe I am not admin..", reply_to_message_id = msg.message_id)
    else:
        bot.send_message(chat_id = chat_id, text = "H*ck off.", reply_to_message_id = msg.message_id)
