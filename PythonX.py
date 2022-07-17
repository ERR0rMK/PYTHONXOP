import asyncio
import sys
import os
import random
from DataX import OneWord
from SessionX import hack, MK_USERS, Python
from telethon.tl.functions.channels import JoinChannelRequest


async def StartMK():
    try:
        await Python.start()
        await Python(JoinChannelRequest(channel="@MKxHACKER"))
        await Python(JoinChannelRequest(channel="@TheAltron"))
        await Python(JoinChannelRequest(channel="@Altron_X"))
    except Exception as e:
        print(e)

loop = asyncio.get_event_loop()
loop.run_until_complete(StartMK())



@hack(outgoing=True, pattern=".python")
async def spam(e):
    if e.sender_id in MK_USERS:
        pyspam = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        RMsg = await e.get_reply_message()
        if len(pyspam) == 2:
            message = str(pyspam[1])
            counter = int(pyspam[0])
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and RMsg.text:
            message = RMsg.text
            counter = int(pyspam[0])
            await asyncio.wait([e.respond(message) for i in range(counter)])


@hack(outgoing=True, pattern="pythonx")
async def oneword(e):
    if e.sender_id in MK_USERS:
        pyraid = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(pyraid) == 2:
            message = str(pyraid[1])
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(pyraid[0])
            for _ in range(counter):
                reply = random.choice(OneWord)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(pyraid[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(OneWord)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)


@hack(outgoing=True, pattern=".restart")
async def restart(e):
    if e.sender_id in MK_USERS:
        await e.reply("𝐄𝐑𝐑𝟎𝐑 𝟏𝟑𝟏: 𝐒𝐄𝐑𝐕𝐄𝐑 𝐈𝐒 𝐑𝐄𝐒𝐓𝐀𝐑𝐓𝐈𝐍𝐆 🥵", parse_mode=None, link_preview=None)
        try:
            await Python.disconnect()
        except Exception as e:
            pass
        
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


@hack(outgoing=True, pattern=".hack")
async def ping(e):
    if e.sender_id in MK_USERS:
        text = f"🤬 HACKER ✘SPAM 🤖!\n✘ #MK 131\n 😈𝙍𝙀𝘼𝘿𝙔 𝙏𝙊 𝙃𝘼𝘾𝙆😎"
        await e.reply(text, parse_mode=None, link_preview=None )


print("\n𝐌𝐊𝐱𝐒𝐏𝐀𝐌 𝐃𝐄𝐏𝐋𝐎𝐘𝐄𝐃 𝐒𝐔𝐂𝐂𝐄𝐒𝐒𝐅𝐔𝐋𝐋𝐘 😎🤘🏻\nMy Master ---> @𝐇𝐀𝐂𝐊𝟑𝐑_𝐗𝐃")

if len(sys.argv) not in (1, 3, 4):
    try:
        Python.disconnect()
    except Exception as e:
        pass

else:
    try:
        Python.run_until_disconnected()
    except Exception as e:
        pass
