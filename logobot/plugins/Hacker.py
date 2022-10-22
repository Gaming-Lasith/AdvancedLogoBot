import re
from logobot import logobot
from io import BytesIO
from requests import get
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os 
from os import getenv
from PIL import Image, ImageDraw, ImageFont
import random
import requests
import shutil
from logobot.utils import LOGOCREATE, LOGOCREATEBTNS

@logobot.on_message(filters.command("slmask"))
async def logomake(_, message: Message):
    if len(message.command) != 2:
        return await message.reply_text("Please give a text.\nEx:`/slmask Name` ")
    else:
        pass
    m = await message.reply('Designing your logo...wait!')
    await m.edit("Logo in processing...\n░░░░░░░░░░ 0%")
    await m.edit("Logo in processing...\n▇▇░░░░░░░░ 20%")
    await m.edit("Logo in processing...\n▇▇▇▇░░░░░░ 40%")
    await m.edit("Logo in processing...\n▇▇▇▇▇▇░░░░ 60%")
    await m.edit("Logo in processing...\n▇▇▇▇▇▇▇▇░░ 80%")
    await m.edit("Logo in processing...\n▇▇▇▇▇▇▇▇▇▇ 100%")
    text = message.text.split(None, 1)[1]
    img = Image.open("./logobot/resources/Hacker Bike.jpg")
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./logobot/resources/SpacePatrol.ttf", 400)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 255), stroke_width=8, stoke_fill='#FFFFFF')
    img.save("hackerbike.jpg")
    await m.edit("📤Uploading...")
    await message.reply_photo(
                photo=f"hackerbike.jpg",
                caption= f"""
✅ Logo Created Successfully ✅
◇───────────────◇
✨ **Requester** :
{message.from_user.mention}
🔥 **Created by** :
[Amazing Logos](http://t.me/AmazingLogosBot)
⚡️ **Powered by** :
[➷ʟҡ #ɴᴏᴏʙ](http://t.me/ImLasith)
◇───────────────◇
""",
                reply_markup=LOGOCREATEBTNS
            )
    await m.delete()
