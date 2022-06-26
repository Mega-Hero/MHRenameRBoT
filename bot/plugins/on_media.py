# (c) @AbirHasan2005

import asyncio
from bot.client import Client
from bot.core.db.add import (
    add_user_to_database
)
from pyrogram import (
    filters,
    types
)


@Client.on_message((filters.video | filters.audio | filters.document) & ~filters.channel & ~filters.edited)
async def on_media_handler(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("𝙸 𝚍𝚘𝚗'𝚝 𝚔𝚗𝚘𝚠 𝚊𝚋𝚘𝚞𝚝 𝚢𝚘𝚞 𝚍𝚞𝚍𝚎 :(")
    await add_user_to_database(c, m)
    await asyncio.sleep(3)
    await c.send_flooded_message(
        chat_id=m.chat.id,
        text="**𝑆ℎ𝑜𝑢𝑙𝑑 𝐼 𝑠ℎ𝑜𝑤 𝐹𝑖𝑙𝑒 𝐼𝑛𝑓𝑜𝑟𝑚𝑎𝑡𝑖𝑜𝑛?**",
        reply_markup=types.InlineKeyboardMarkup(
            [[types.InlineKeyboardButton("Yes", callback_data="showFileInfo"),
              types.InlineKeyboardButton("No", callback_data="closeMessage")]]
        ),
        disable_web_page_preview=True,
        reply_to_message_id=m.message_id
    )
