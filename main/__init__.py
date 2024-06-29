#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "27803618" #config("API_ID", default=None, cast=int)
API_HASH = "2cdaef9643189f6bd9c7b31a70257356" #config("API_HASH", default=None)
BOT_TOKEN = "7048821409:AAF4foRNkVcRuKD5oXA8e2M2rQ_LIBjsiTg" #config("BOT_TOKEN", default=None)
SESSION = "BQGoP-IAroAVGkkn2qUiMGxnsGBierCQIyLfahhUA9ci4b9vxFvSOCyQycQenEWzHWG0gbSpDaGfvHBs26fodHIjawuaGdOtAuE-yfHg-Qs6pOQyXNq7XfIBa0R2zC7YjDznodzSJ32_6Pw2uzf56p3OhLTKwifl6YsFvMh0F6oHKd--0vDRouy3Cg4kAEfu6Vd6uUFpJVY-JM0uufSj1MhHY6ULud5oekg8Sj8nopw99uD7mBFe28Rm-TiFt13MFRV6raxitbAyT-gGOMoiaBjgcwrfXhXTcbl8RfRbttd6edn8mZ768T0oTab-28lSu4SEMswfARuR9sNCHOSZvKATU84T1QAAAAAsaRVjAA" #config("SESSION", default=None)
FORCESUB = "bot_user12838" #config("FORCESUB", default=None)
AUTH = "745084259" #config("AUTH", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
