# (c) @AbirHasan2005

import shutil
import psutil
from pyrogram import filters
from pyrogram.types import (
    Message
)
from configs import Config
from bot.client import Client
from bot.core.db.database import db
from bot.core.display import humanbytes
from bot.core.handlers.broadcast import broadcast_handler


@Client.on_message(filters.command("status") & filters.user(Config.OWNER_ID) & ~filters.edited)
async def status_handler(_, m: Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    await m.reply_text(
        text=f"**𝚃𝚘𝚝𝚊𝚕 𝙳𝚒𝚜𝚔 𝚂𝚙𝚊𝚌𝚎:** {total} \n"
             f"**𝑈𝑠𝑒𝑑 𝑆𝑝𝑎𝑐𝑒:** {used}({disk_usage}%) \n"
             f"**Fʀᴇᴇ Sᴘᴀᴄᴇ:** {free} \n"
             f"**ᑕᑭᑌ ᑌՏᗩᘜᗴ:** {cpu_usage}% \n"
             f"**ᖇᗩᗰ ᑌՏᗩᘜᗴ:** {ram_usage}%\n\n"
             f"**𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫𝐬 𝐢𝐧 𝐃𝐁:** `{total_users}`",
        parse_mode="Markdown",
        quote=True
    )


@Client.on_message(filters.command("broadcast") & filters.user(Config.OWNER_ID) & filters.reply & ~filters.edited)
async def broadcast_in(_, m: Message):
    await broadcast_handler(m)
