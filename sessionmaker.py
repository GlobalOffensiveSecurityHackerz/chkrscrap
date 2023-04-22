from telethon import TelegramClient
from telethon.sessions import StringSession


API_KEY = int(input("5956785974:AAEO2S09X5fKPkXmyPU4vu9QUu5o6EzAxc0"))
API_HASH = input("21f1e74c0b644d21ea1afabfda42459e") 


bot = TelegramClient(StringSession(), API_KEY, API_HASH)
bot.start()
string_session = bot.session.save()
print(string_session)
