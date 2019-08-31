import defaults

def ban(bot, update):
    msg = update.message
    chat_id = msg.chat_id
    msg_id = msg.message_id
    
    if chat_id != defaults.chat_id: return

    banner = bot.get_chat_member(chat_id, msg.from_user.id)

    if banner.user.id == 170256543 or banner['status'] in ['creator', 'administrator']:
        if update.message.reply_to_message:
            user_to_ban = update.message.reply_to_message.from_user
            try:
                bot.kick_chat_member(chat_id, user_to_ban.id)
                bot.send_message(chat_id=chat_id,
                                 text=f"Banned {user_to_ban.first_name}.",
                                 reply_to_message_id=msg_id)
            except:
                bot.send_message(chat_id=chat_id,
                                 text="Couldn't ban, either I'm not an admin or the other user is.",
                                 reply_to_message_id=msg_id)
        else:
            bot.send_message(chat_id=chat_id,
                             text="Reply to the person who you want to ban.",
                             reply_to_message_id=msg_id)
    else:
        bot.send_message(chat_id=chat_id,
                         text=f"H*ck off.",
                         reply_to_message_id=msg_id)

def unban(bot, update):
    msg = update.message
    chat_id = msg.chat_id
    msg_id = msg.message_id
    
    if chat_id != defaults.chat_id: return

    banner = bot.get_chat_member(chat_id, msg.from_user.id)

    if banner.user.id == 170256543 or banner['status'] in ['creator', 'administrator']:
        if update.message.reply_to_message:
            user_to_unban = update.message.reply_to_message.from_user
            try:
                bot.unban_chat_member(chat_id, user_to_unban.id)
                bot.send_message(chat_id=chat_id,
                                 text=f"Unbanned {user_to_unban.first_name}.",
                                 reply_to_message_id=msg_id)
            except:
                bot.send_message(chat_id=chat_id,
                                 text="Couldn't unban.",
                                 reply_to_message_id=msg_id)