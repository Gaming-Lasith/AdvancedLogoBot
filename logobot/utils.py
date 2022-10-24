
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
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
import config

BOTNAME=config.BOT_NAME
BOTUNAME=config.BOT_USERNAME

STARTTEXT = f"""
**✨Hello 🙋
💫I am {BOTNAME}**

😈I can create simple logos for you.            
ℹ️Click "About" and "Help And Commands" to know more.
✌️__[➷ʟҡ #ɴᴏᴏʙ](https://t.me/ImLasith) All Right Received©__
"""

STARTBTNS = InlineKeyboardMarkup(
            [       
                [
                    InlineKeyboardButton("UPDATES", url="https://t.me/ImLasith"),
                    InlineKeyboardButton("SUPPORT", callback_data="contact"),
                ],
                [
                    InlineKeyboardButton("About bot", callback_data="aboutmenu")
                ], 
                [
                    InlineKeyboardButton("☘️Help And Commands☘️", callback_data="helpmenu")
                ],
                [ 
                    InlineKeyboardButton("Developer", url="https://t.me/Lasith4")           
                ]
            ]
        )

HELPTEXT = f"""
**✨Hello 🙋**
I have some commands.
Try bellow buttons to 
👇__know about them__👇
"""

HELPBTNS = InlineKeyboardMarkup(
           [
             [
               InlineKeyboardButton("Logo Commands", callback_data="logomenu")
             ],
             [
               InlineKeyboardButton("Bot Commands", callback_data="botmenu")
             ],
             [
               InlineKeyboardButton("🔙Back", callback_data="startmenu")
             ],
           ]
       ) 

CONTACTTEXT = f"""
😓Sorry,
⚠️No Support Chat for this bot,
🤗But You can contact [Developer](https://t.me/Lasith4)...
✌️__[➷ʟҡ #ɴᴏᴏʙ](https://t.me/ImLasith) All Right Received©__
"""

CONTACTBTNS = InlineKeyboardMarkup(
           [
             [
               InlineKeyboardButton("Developer", url="https://t.me/Lasith4"),
             ],
             [
               InlineKeyboardButton("🔙Back", callback_data="helpmenu")
             ],
           ]
       )

REPOPRIVATETEXT = f"""
😓Sorry,
⚠️The Source code of this bot is private,
🤗But I will publish a simple repo of this bot soon...
✌️__[➷ʟҡ #ɴᴏᴏʙ](https://t.me/ImLasith) All Right Received©__
"""

REPOPRIVATEBTNS = InlineKeyboardMarkup(
           [
             [
               InlineKeyboardButton("Developer", url="https://t.me/Lasith4"),
             ],
             [
               InlineKeyboardButton("🔙Back", callback_data="helpmenu")
             ],
           ]
       )

ABOUTTEXT = f"""
***෴ABOUT BOT෴**

Bot Name is **{BOTNAME}** &
Bot UserName is @{BOTUNAME}


||Bot ID - 5409032614
Bot Created Date - 2022.07.08
Bot Version - v1.0||


Credits 💳
•[Sเƚԋเʝα▁ƚԃ](https://t.me/sithijatd) ( [for the repo](https://github.com/Sithijadewmina/simple-logo-bot/) )


✍️ Written with pyrogram & pillow
✌️__[➷ʟҡ #ɴᴏᴏʙ](https://t.me/ImLasith) All Right Received©__
"""

ABOUTBTNS = InlineKeyboardMarkup(
           [
             [
               InlineKeyboardButton("Source Code📦", callback_data="itsprivate"),
             ],
             [
               InlineKeyboardButton("🔙Back", callback_data="startmenu")
             ],
           ]
       )


LOGOTEXT = """
**෴Logo Commands෴**

__Here Logo making cmds 🔥__
__Try them and Get a fun.__

•/slmask {text} - Mask Logo.
•/anime {text} - Alone Anime Boy.
•/hacker {text} - Hacker Bike Logo

```More logos update in soon.``` """

LOGOBTNS = InlineKeyboardMarkup(
           [[
               InlineKeyboardButton("🔙Back", callback_data="helpmenu")
           ]]
         )

BOTTEXT = """
**෴Bot commands෴**

•/start - Start bot.
•/help - Get Help.
•/about - About bot.
 """

BOTBTNS = InlineKeyboardMarkup(
           [[
               InlineKeyboardButton("🔙Back", callback_data="helpmenu")
           ]]
         )

LOGOCREATE = f"""
☘️ Logo Created Successfully✅
◇───────────────◇
🔥 **Created by** :
[Amazing Logos](http://t.me/AmazingLogosBot)
⚡️ **Powered by**   :
[➷ʟҡ #ɴᴏᴏʙ](http://t.me/ImLasith)
◇───────────────◇
"""

LOGOCREATEBTNS = InlineKeyboardMarkup(
      [
        [
        InlineKeyboardButton(text="Developer", url=f"http://t.me/Lasith4") 
        ],
        [
         InlineKeyboardButton(text="🌚 Share Our Bot 🌝", url=f"tg://msg_url?url=I%20found%20a%20super%20logo%20bot%20use%20now%20@AmazingLogosBot%20%F0%9F%A4%A9") 
        ]
      ]      
  )
