""" 
MIT License

Copyright (c) 2022 Gaming Lasith

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

    
import asyncio
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from config import Config

CHANNEL_ID = config.F_SUB_CHANNEL


async def ForceSub(bot: Client, event: Message):
    try:
        await bot.get_chat_member(chat_id=(int(CHANNEL_ID) if CHANNEL_ID.startswith("-100") else CHANNEL_ID), user_id=event.from_user.id)
    except UserNotParticipant:
        try:
           gh = await bot.send_message(chat_id=event.chat.id,text=f"""
**Hey** {event.from_user.mention} !,
**You are not subscribed my channel... So subscribe my channel for use me 🍃
Click join now button and join [➷ʟҡ </ɴᴏᴏʙ>](https://t.me/ItsMeLasith) channel.**
||When you subscribed my channel, This message not display again 🕊||
""",
reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("↗️ Join Now ↗️", url="https://t.me/ItsMeLasith")]]),disable_web_page_preview=True)
           await asyncio.sleep(10)
           await gh.delete()
           return 400
        except FloodWait as e:
           await asyncio.sleep(e.x)
           fix_ = await ForceSub(bot, event)
           return fix_
    except Exception as err:
        print(f"""Something Went Wrong! Unable to do Force Subscribe.
        Error: {err}
        
        Contact ԌΛϺェƝԌ ㄥΛکェтℋ: https://t.me/ImLasith""")
        return 200  
