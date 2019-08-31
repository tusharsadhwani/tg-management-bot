_error = """
Enter your Bot Token and Chat ID in defaults.py, eg.
token = "123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZ-12345678"
chat_id = -10012340000001
"""

try:
    token = TOKEN_HERE
    chat_id = CHAT_ID_HERE
    tl_api_key = ''
except NameError:
    raise ValueError(_error)