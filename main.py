# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import pyrogram, os, asyncio

app_id = int(os.environ.get("app_id", ""))
api_hash = os.environ.get("api_hash", "")
bot_token = os.environ.get("bot_token", "")
custom_caption = os.environ.get("custom_caption", "`{file_name}`")

AutoCaptionBotV1 = pyrogram.Client(name="AutoCaptionBotV1", api_id=app_id, api_hash=api_hash, bot_token=bot_token)

start_message = """
<b>👋Hello {}</b>
<b>I am an AutoCaption bot</b>
<b>All you have to do is to add me to your channel as admin and I will show you my power</b>
<b>@VJ_Botz</b>"""

about_message = """
<b>• Name : <a href=https://t.me/VJ_Botz>VJ AutoCaption</a></b>
<b>• Developer : <a href=https://t.me/VJ_Botz>[VJ UPDATES]</a></b>
<b>• Language : Python3</b>
<b>• Library : Pyrogram v{version}</b>
<b>• Updates : <a href=https://t.me/VJ_Botz>Click Here</a></b>
<b>• Source Code : <a href=https://github.com/VJBots/VJ-AutoCaption-Bot>Click Here</a></b>"""

@AutoCaptionBotV1.on_message(pyrogram.filters.private & pyrogram.filters.command(["start"]))
def start_command(bot, update):
    update.reply(start_message.format(update.from_user.mention), reply_markup=start_buttons(bot, update), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@AutoCaptionBotV1.on_callback_query(pyrogram.filters.regex("start"))
def strat_callback(bot, update):
    update.message.edit(start_message.format(update.from_user.mention), reply_markup=start_buttons(bot, update.message), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@AutoCaptionBotV1.on_callback_query(pyrogram.filters.regex("about"))
def about_callback(bot, update): 
    bot = bot.get_me()
    update.message.edit(about_message.format(version=pyrogram.__version__, username=bot.mention), reply_markup=about_buttons(bot, update.message), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@AutoCaptionBotV1.on_message(pyrogram.filters.channel)
def edit_caption(bot, update: pyrogram.types.Message):
    techvj, _ = get_file_details(update)
    try:
       try:
           update.edit(custom_caption.format(file_name=techvj.file_name))
       except pyrogram.errors.FloodWait as FloodWait:
           asyncio.sleep(FloodWait.value)
           update.edit(custom_caption.format(file_name=techvj.file_name))
       except:
          pass
    except pyrogram.errors.MessageNotModified:
        pass 
    
def get_file_details(update: pyrogram.types.Message):
    if update.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            "sticker"
        ):
            obj = getattr(update, message_type)
            if obj:
                return obj, obj.file_id

def start_buttons(bot, update):
    bot = bot.get_me()
    buttons = [[
        pyrogram.types.InlineKeyboardButton("Updates", url="t.me/VJ_Botz"),
        pyrogram.types.InlineKeyboardButton("About 🤠", callback_data="about")
    ],[
        pyrogram.types.InlineKeyboardButton("➕️ Add To Your Channel ➕️", url=f"http://t.me/{bot.username}?startchannel=true")
    ]]
    return pyrogram.types.InlineKeyboardMarkup(buttons)

def about_buttons(bot, update):
    buttons = [[
        pyrogram.types.InlineKeyboardButton("🏠 Back To Home 🏠", callback_data="start")
    ]]
    return pyrogram.types.InlineKeyboardMarkup(buttons)

print("Telegram AutoCaption V1 Bot Start")
print("Bot Created By @VJ_Botz")

AutoCaptionBotV1.run()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
