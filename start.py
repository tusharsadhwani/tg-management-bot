import os.path

def start(bot, update):
    chat_id = update.message.chat_id
    if chat_id == update.message.from_user.id:
        text = update.message.text.split(" ",1)
        if len(text) > 1:
            trigger = text[1]
            if trigger == "rules":
                if os.path.exists('rules.txt'):
                    try:
                        with open('rules.txt') as f:
                            rules = f.read().strip()
                    except:
                        rules = None
                else:
                    rules = None

                if rules:
                    bot.send_message(chat_id = update.message.chat_id, text = f"Rules:\n{rules}")
                else:
                    bot.send_message(chat_id = update.message.chat_id, text = "This group doesnt have rules set.")
                return

    bot.send_message(chat_id = update.message.chat_id, text = "H*ck you.")


