import defaults

def delete(bot, update):
    msg = update.message
    chat_id = msg.chat_id

    if chat_id != defaults.chat_id: return

    deleter = bot.get_chat_member(chat_id=chat_id, user_id=msg.from_user.id)['status']

    if deleter in ['administrator','creator']:
        if msg.reply_to_message:
            try:
                bot.delete_message(chat_id=chat_id, message_id=msg.reply_to_message.message_id)
            except:
                bot.send_message(chat_id=chat_id, text=f"Couldn't delete message. Maybe I'm not admin...", reply_to_message_id=msg.message_id)
                return

            reason = msg.text.split(' ',1)
            if len(reason)>1:
                reason = reason[1]
                user_name = msg.reply_to_message.from_user.username
                if user_name:
                    user_name =user_name.replace("_", r"\_")
                    bot.send_message(chat_id=chat_id, text=f"@{user_name}'s *Message deleted.\nReason:* _{reason}_", parse_mode="Markdown", reply_to_message_id=msg.message_id)
                else:
                    first_name = msg.reply_to_message.from_user.first_name
                    bot.send_message(chat_id=chat_id, text=f"{first_name}'s *Message deleted.\nReason:* _{reason}_", parse_mode="Markdown", reply_to_message_id=msg.message_id)
        else:
            bot.send_message(chat_id=chat_id, text=f"Reply to the message you want to delete.", reply_to_message_id=msg.message_id)
        
        try:
            bot.delete_message(chat_id=chat_id, message_id=msg.message_id)        
        except:
            pass
    else:
        bot.send_message(chat_id=chat_id, text="H*ck off, you're not admin.", reply_to_message_id=msg.message_id)

