
    
import asyncio
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from logobot import logobot

CHANNEL_ID = -1001531907575


async def ForceSub(bot: Client, event: Message):
    try:
        await bot.get_chat_member(chat_id=(int(CHANNEL_ID) if CHANNEL_ID.startswith("-100") else CHANNEL_ID), user_id=event.from_user.id)
    except UserNotParticipant:
        try:
           gh = await bot.send_message(chat_id=event.chat.id,text=f"""
**Hey** {event.from_user.mention} !,
**You are not subscribed my channel... So subscribe my channel for use me 🍃
Click join now button and join [➷ʟҡ #ɴᴏᴏʙ](https://t.me/ItsMeLasith) channel.**
||When you subscribed my channel, This message not display again 🕊||
""",
reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("↗️ Join Now ↗️", url="https://t.me/ItsMeLasith")]]),disable_web_page_preview=True)
           await gh.delete()
           return 400
        except FloodWait as e:
           await asyncio.sleep(e.x)
           fix_ = await ForceSub(bot, event)
           return fix_
    except Exception as err:
        print(f"Something Went Wrong! Unable to do Force Subscribe.\nError: {err}\n\nContact Developer: https://t.me/ImLasith")
        return 200  
