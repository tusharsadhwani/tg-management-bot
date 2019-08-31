import os.path

import defaults

def clearwarns(bot, update):
    msg = update.message
    chat_id = msg.chat_id

    if chat_id != defaults.chat_id: return

    user_id = msg.from_user.id
    clearer = bot.get_chat_member(chat_id, user_id)['status']

    if clearer in ['creator', 'administrator']:
        if update.message.reply_to_message:
            warned_user = msg.reply_to_message.from_user
            
            newlines = []
            if os.path.exists('warns.txt'):
                with open('warns.txt') as f:
                    lines = f.readlines()
                    for line in lines:
                        if not line:
                            continue
                        
                        userid, _ = line.split()
                        if int(userid) != warned_user.id:
                            newlines.append(line)

            with open('warns.txt', 'w') as f:
                f.writelines(newlines)
    
            msg.reply_text(f"Warns cleared for {msg.reply_to_message.from_user.first_name}")
            
def warn_count(bot, update):
    msg = update.message
    chat_id = msg.chat_id

    if chat_id != defaults.chat_id: return

    if update.message.reply_to_message:
        checked_user = msg.reply_to_message.from_user
        if os.path.exists('warns.txt'):
            with open('warns.txt') as f:
                lines = f.readlines()
                for line in lines:
                    if not line.strip():
                        continue
                    
                    userid, warns = line.split()
                    if int(userid) == checked_user.id:
                        msg.reply_text(f"Warns : {warns}/3.")
                        return
        
        msg.reply_text(f"Warns : 0/3.")


def warn(bot, update):
    msg = update.message
    chat_id = msg.chat_id

    if chat_id != defaults.chat_id: return

    user_id = msg.from_user.id
    clearer = bot.get_chat_member(chat_id, user_id)['status']

    if clearer in ['creator', 'administrator']:
        if update.message.reply_to_message:
            warned_user = msg.reply_to_message.from_user
            
            if os.path.exists('warns.txt'):
                with open('warns.txt') as f:
                    newlines = []
                    lines = f.readlines()
                    warned_user_warns = None
                    for line in lines:
                        if not line:
                            continue
                        
                        userid, warns = line.split()
                        if int(userid) == warned_user.id:
                            warned_user_warns = int(warns) + 1

                            if warned_user_warns == 3:
                                try:
                                    bot.kick_chat_member(chat_id, warned_user.id)
                                    msg.reply_text(f"Warns: 3/3 reached. Banned {warned_user.first_name}.")
                                except:
                                    msg.reply_text("Warns: 3/3 reached. Couldn't ban tho.")
                                
                                warned_user_warns = 0
                            else:
                                msg.reply_text(f"Warns: {warned_user_warns}/3 reached.")
                            newlines.append(f"{userid} {warned_user_warns}")
                        else:
                            newlines.append(line)

                    if warned_user_warns is None:
                        newlines.append(f"{warned_user.id} 1")
                        msg.reply_text("Warns: 1/3 reached")

                with open('warns.txt', 'w') as f:
                    f.writelines(newlines)
            else:
                with open('warns.txt', 'w') as f:
                    f.write(f"{warned_user.id} 1\n")
                    msg.reply_text("Warns: 1/3 reached")
