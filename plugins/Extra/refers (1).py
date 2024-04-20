import pytz
import datetime, time
from Script import script
from info import PICS
from pyrogram import Client, filters 
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.command("refer"))
async def refers(client, message):
    user_id = message.from_user.id 
    users = message.from_user.mention 
    btn = [[
	
        InlineKeyboardButton(' Invite link ', url=f"https://telegram.me/share/url?url=https://telegram.me/Testing_00100_bot?start=AV-{message.from_user.id}&text=Hᴇʟʟᴏ%21%20ᴇxᴘᴇʀɪᴇɴᴄᴇ%20ᴀ%20ʙᴏᴛ%20ᴛʜᴀᴛ%20ᴏғғᴇʀs%20ᴀ%20ᴠᴀsᴛ%20ʟɪʙʀᴀʀʏ%20ᴏғ%20ᴜɴʟɪᴍɪᴛᴇᴅ%20ᴍᴏᴠɪᴇs%20ᴀɴᴅ%20sᴇʀɪᴇs.%20%F0%9F%98%83"),InlineKeyboardButton('⇋ ʙᴀᴄᴋ ⇋', callback_data='close_data')
    ]]
    await message.reply_photo(photo="https://telegra.ph/file/b2ab60c80ff67f6af0f6e.jpg", caption=script.AKA_TEXT.format(message.from_user.mention, message.from_user.id), reply_markup=InlineKeyboardMarkup(btn))
 
