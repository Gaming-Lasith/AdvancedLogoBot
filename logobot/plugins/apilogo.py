import re
from logobot import logobot
from io import BytesIO
import requests
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os 
from PIL import Image, ImageDraw, ImageFont
import random
import requests
import shutil
import config 
from logobot.utils import LOGOCREATE, LOGOCREATEBTNS

repmark = LOGOCREATEBTNS

def nospace(s):

    s = re.sub(r"\s+", '%20', s)

    return s
@logobot.on_message(filters.command("logo"))
async def make_logo(_, message):
    imgcaption = f"""
✅ Logo Created Successfully ✅
◇───────────────◇
✨ **Requester** :
{message.from_user.mention}
🔥 **Created by** :
[Amazing Logos](http://t.me/AmazingLogosBot)
⚡️ **Powered by** :
[➷ʟҡ #ɴᴏᴏʙ](http://t.me/ImLasith)
◇───────────────◇
"""
    if len(message.command) < 2:
            return await message.reply_text("Please give a text")
    m = await message.reply_text("📸 Creating..")
    name = message.text.split(None, 1)[1] if len(message.command) < 3 else message.text.split(None, 1)[1].replace(" ", "%20")
    api = requests.get(f"https://single-developers.up.railway.app/logo?name={name}")
    await m.edit("📤 Uploading ...")
    await stdlogo.send_chat_action(message.chat.id, "upload_photo")
    img = Image.open(BytesIO(api.content))
    logoname = "stdlogo.png"
    img.save(logoname, "png")
    await message.reply_photo(photo = logoname,
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
                              reply_markup=LOGOCREATEBTNS)
    await m.delete()
    if os.path.exists(logoname):
            os.remove(logoname)
                       
fonts = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
# Colour Selection
colour = ["yellow",
          "red",
          "blue"]

logomake = ["https://telegra.ph/file/7cd465d6609ea17141747.jpg", 
            "https://telegra.ph/file/9cafdfbcdc5212b3138a9.jpg", 
            "https://telegra.ph/file/4e56b39faa4c03ca4079c.jpg",]

@logobot.on_message(filters.command("write"))
async def write_logo(_, message):
    imgcaption = f"""
✅ Logo Created Successfully ✅
◇───────────────◇
✨ **Requester** :
{message.from_user.mention}
🔥 **Created by** :
[Amazing Logos](http://t.me/AmazingLogosBot)
⚡️ **Powered by** :
[➷ʟҡ #ɴᴏᴏʙ](http://t.me/ImLasith)
◇───────────────◇
"""
    if len(message.command) < 2:
            return await message.reply_text("Please give a text")
    m = await message.reply_text("✍️ writing..")
    name = message.text.split(None, 1)[1] if len(message.command) < 3 else message.text.split(None, 1)[1].replace(" ", "%20")
    api = requests.get(f"https://single-developers.up.railway.app/write={name}")
    await m.edit("📤 Uploading ...")
    await stdlogo.send_chat_action(message.chat.id, "upload_photo")
    img = Image.open(BytesIO(api.content))
    logoname = "stdwrite.png"
    img.save(logoname, "png")
    await message.reply_photo(photo = logoname,
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
                              reply_markup=LOGOCREATEBTNS)
    await m.delete()
    if os.path.exists(logoname):
            os.remove(logoname)
  
