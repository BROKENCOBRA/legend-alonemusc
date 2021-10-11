from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAADBQADRQIAAhHHQFSfHJ-IR0eN6gI")
    await message.reply_text(
        f"""**𝐇𝐞𝐲, 𝐀𝐦 {bn} 💛🐬,
𝐈 𝐂𝐚𝐧 𝐏𝐥𝐚𝐲 𝐌𝐮𝐬𝐢𝐜 𝐈𝐧 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐕𝐨𝐢𝐜𝐞 𝐂𝐚𝐥𝐥. 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 [𝐌𝐚𝐡𝐢](https://t.me/ALONE_BOY_XD_01)❣️🤞.
𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝 𝐏𝐥𝐚𝐲 𝐌𝐮𝐬𝐢𝐜 𝐅𝐫𝐞𝐞𝐥𝐲💕😘**

        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐎𝐰𝐧𝐞𝐫", url="https://t.me/ALONE_BOY_XD_01")
                  ],[
                    InlineKeyboardButton(
                        "👿 𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url="https://t.me/shivamdemon"
                    ),
                    InlineKeyboardButton(
                        "🔊 𝐌𝐨𝐫𝐞 𝐈𝐧𝐟𝐨", url="https://t.me/ALONE_BOY_XD_01"
                    )    
                ],[ 
                    InlineKeyboardButton(
                        "➕ 𝐀𝐝𝐝 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ➕", url="https://t.me/legend_Alone_music_bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**𝐀𝐋𝐎𝐍𝐄 𝐌𝐔𝐒𝐈𝐂 𝐏𝐋𝐀𝐘𝐄𝐑 𝐈𝐒 𝐎𝐍𝐋𝐈𝐍𝐄 💕✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 𝐌𝐚𝐧𝐚𝐠𝐞𝐫", url="https://t.me/legend_boy_xd_01")
                ]
            ]
        )
   )
