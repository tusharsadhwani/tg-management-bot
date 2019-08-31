from save import check_saves
from sed import sed
import defaults

def msg_text(bot, update):
    if update.message.chat_id != defaults.chat_id: return

    check_saves(bot, update)
    sed(bot, update)