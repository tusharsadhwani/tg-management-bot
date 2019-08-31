from welcome import welcome
import defaults

def msg_all(bot, update):
    if update.message.chat_id != defaults.chat_id: return

    welcome(bot, update)