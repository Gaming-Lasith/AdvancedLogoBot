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

import os
from pyrogram import filters, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from requests import get
import datetime
import pytz
from logobot import logobot
from logobot.plugins import *
from logobot import LOGGER
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
import random
import requests
import shutil
import config
from logobot.utils import HELPTEXT, HELPBTNS

BOTNAME = config.BOT_NAME
BOTUNAME = config.BOT_USERNAME
STICKID = config.STICKER_ID

STARTTEXT = f"""
**✨Hello 🙋
💫I am {BOTNAME}**

😈I can create simple logos for you.            
ℹ️Click "About" and "Help And Commands" to know more.
✌️__[➷ʟҡ </ɴᴏᴏʙ>](https://t.me/ItsMeLasith) All Right Received©__
"""

STARTBTNS = InlineKeyboardMarkup(
            [       
                [
                    InlineKeyboardButton("UPDATES", url="https://t.me/ItsMeLasith"),
                    InlineKeyboardButton("SUPPORT", callback_data="contact")
                ],
                [
                    InlineKeyboardButton("About bot", callback_data="aboutmenu")
                ], 
                [
                    InlineKeyboardButton("☘️Help And Commands☘️", callback_data="helpmenu")
                ],
                [ 
                    InlineKeyboardButton("Developer", url="https://t.me/ImLasith")           
                ]
            ]
        )

START_IMG = "https://telegra.ph/file/e0a135d44f34933616069.jpg"

@logobot.on_message(filters.private & filters.incoming & filters.command(["start"]))
async def startmsg(_, message):
    file_id = f"{STICKID}"
    await logobot.send_sticker(message.from_user.id, file_id)
    await message.reply_text(
    text=f"""
**✨Hello {message.from_user.mention} 🙋
💫I am {BOTNAME}**

😈I can create simple logos for you.            
ℹ️Click "About" and "Help And Commands" to know more.
✌️__[➷ʟҡ </ɴᴏᴏʙ>](https://t.me/ItsMeLasith) All Right Received©__
""", 
    reply_markup=STARTBTNS
  )

@logobot.on_message(filters.private & filters.incoming & filters.command(["help"]))
async def startmsg(_, message):
    file_id = f"{STICKID}"
    await logobot.send_sticker(message.from_user.id, file_id)
    await message.reply_text(
    text=f"""
**✨Hello {message.from_user.mention} 🙋**

I have some commands.
Try bellow buttons to 
👇__know about them__👇
""", 
    reply_markup=HELPBTNS
  )
    
@logobot.on_message(filters.private & filters.incoming & filters.command(["about"]))
async def startmsg(_, message):
    file_id = f"{STICKID}"
    await logobot.send_sticker(message.from_user.id, file_id)
    await message.reply_text(
    text=f"""
**෴ABOUT BOT෴**

Bot Name is **{BOTNAME}** &
Bot UserName is @{BOTUNAME}


||Bot ID - 5409032614
Bot Created Date - 2022.07.08
Bot Version - v1.0||


Credits 💳
•[Sเƚԋเʝα▁ƚԃ](https://t.me/sithijatd) ( [for the repo](https://github.com/Sithijadewmina/simple-logo-bot/) )
•[Single Developers </>](https://t.me/SingleDevelopers) ( [for the api](https://github.com/Single-Developers/API/) )
•[Rose bot ✨](https://t.me/szrosebot) ( [for the fusb.py](https://github.com/szsupunma/sz-rosebot/blob/master/Rose/plugins/fsub.py) )


✍️ Written with pyrogram & pillow
✌️__[ԌΛϺェƝԌ ㄥΛکェтℋ](https://t.me/ItsMeLasith) All Right Received©__
""", 
    reply_markup= InlineKeyboardMarkup(
           [
             [
               InlineKeyboardButton("Source Code📦", callback_data="itsprivate"),
             ],
             [
               InlineKeyboardButton("🔙Back", callback_data="startmenu")
             ],
           ]
       )
  )



logobot.start()
LOGGER.info("RLP Logo Bot is online!")
idle()
