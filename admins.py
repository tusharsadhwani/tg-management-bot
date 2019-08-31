import defaults

def admins(bot, update):
    msg = update.message
    chat_id = msg.chat_id
    chat_title = msg.chat.title

    if chat_id != defaults.chat_id: return

    text = f"*Admins for {chat_title}:*\n"
    for admin in bot.getChatAdministrators(chat_id = chat_id):
        if not admin.user.is_bot:
            username = admin.user.username.replace("_","\_")
            text += f"@{username}\n"
    bot.send_message(chat_id=chat_id, text=text, parse_mode="markdown")