from telegram.ext import (Updater, MessageHandler, Filters, CommandHandler,
                          ConversationHandler, CallbackQueryHandler, RegexHandler)
import logging

import defaults
from start import start

from msg_text import msg_text
from msg_all import msg_all

from admins import admins
from pin import pin
from ban import ban, unban
from kick import kick
from warn import warn, warn_count, clearwarns
from mute import mute, unmute
from purge import purge
from delete import delete

from welcome import setwelcome
from rules import rules, setrules

from save import add_save, save_list, remove_save
from ud import ud
from tl import tl


def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    updater = Updater(token="698907268:AAGNhlX1Nkquxij-5QcBJ6R-R3t7l4M8q-0")
 
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)

    msg_text_handler = MessageHandler(Filters.text, msg_text)

    msg_all_handler = MessageHandler(Filters.all, msg_all)

    setwelcome_handler = CommandHandler('setwelcome', setwelcome)
    rules_handler = CommandHandler('rules', rules)
    setrules_handler = CommandHandler('setrules', setrules)
    
    warn_handler = CommandHandler('warn', warn)
    warns_handler = CommandHandler('warns', warn_count)
    clearwarn_handler = CommandHandler('clearwarns', clearwarns)

    kick_handler = CommandHandler('kick', kick)
    ban_handler = CommandHandler('ban', ban)
    unban_handler = CommandHandler('unban', unban)
    pin_handler = CommandHandler('pin', pin)
    mute_handler = CommandHandler('mute', mute)
    unmute_handler = CommandHandler('unmute', unmute)
    delete_handler = CommandHandler(['del', 'delet', 'delete'], delete)
    purge_handler = CommandHandler('purge', purge)
    
    add_save_handler = CommandHandler('save', add_save)
    save_list_handler = CommandHandler('saves', save_list)
    remove_save_handler = CommandHandler('clear', remove_save)

    admins_handler = CommandHandler('admins', admins)

    ud_handler = CommandHandler('ud', ud)
    tl_handler = CommandHandler('tl', tl)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(setwelcome_handler)
    dispatcher.add_handler(rules_handler)
    dispatcher.add_handler(setrules_handler)
    dispatcher.add_handler(warn_handler)
    dispatcher.add_handler(warns_handler)
    dispatcher.add_handler(clearwarn_handler)
    dispatcher.add_handler(kick_handler)
    dispatcher.add_handler(ban_handler)
    dispatcher.add_handler(unban_handler)
    dispatcher.add_handler(mute_handler)
    dispatcher.add_handler(unmute_handler)
    dispatcher.add_handler(delete_handler)
    dispatcher.add_handler(purge_handler)
    dispatcher.add_handler(add_save_handler)
    dispatcher.add_handler(save_list_handler)
    dispatcher.add_handler(remove_save_handler)
    dispatcher.add_handler(admins_handler)
    dispatcher.add_handler(ud_handler)
    dispatcher.add_handler(tl_handler)
    dispatcher.add_handler(pin_handler)

    dispatcher.add_handler(msg_text_handler)
    dispatcher.add_handler(msg_all_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
