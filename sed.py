import re
import defaults

def sed(bot, update):
    msg = update.message
    chat_id = msg.chat_id
    
    if chat_id != defaults.chat_id: return

    if msg.text.startswith('s/'):
        if msg.reply_to_message:
            string = msg.reply_to_message.text or msg.reply_to_message.caption

            msg_list = msg.text.split('/')

            pattern = msg_list[1]
            repl = msg_list[2]

            result = re.sub(pattern, repl, string)

            reply = f"{result}" if result else "*empty message*"

            bot.send_message(chat_id = chat_id,
                             text = reply,
                             reply_to_message_id = msg.reply_to_message.message_id)

