# (c) @AbirHasan2005 & @MutyalaHarshith

from bot.client import Client
from pyrogram import filters
from pyrogram import types
from bot.core.db.add import add_user_to_database


@Client.on_message(filters.command(["start", "ping"]) & filters.private & ~filters.edited)
async def ping_handler(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("𝙸 𝚍𝚘𝚗'𝚝 𝚔𝚗𝚘𝚠 𝚊𝚋𝚘𝚞𝚝 𝚢𝚘𝚞 𝚍𝚞𝚍𝚎 :(")
    await add_user_to_database(c, m)
    await c.send_flooded_message(
        chat_id=m.chat.id,
        text="𝙷𝚒, 𝙸 𝚊𝚖 𝙵𝚊𝚜𝚝 𝙵𝚒𝚕𝚎 𝚁𝚎𝚗𝚊𝚖𝚎𝚛 𝙱𝚘𝚝!\n\n"
             "I ᴄᴀɴ ʀᴇɴᴀᴍᴇ ᴍᴇᴅɪᴀ & ᴅᴏᴄᴜᴍᴇɴᴛs!\n"
             "𝐹𝑜𝑟 𝑀𝑜𝑟𝑒 𝑖𝑛𝑓𝑜𝑟𝑚𝑎𝑡𝑖𝑜𝑛 𝐶𝑙𝑖𝑐𝑘 /help.\n\n"
             "ᑕᖇᗴᗩTᗴᗪ ᗷY : @MutyalaHarshith",
        reply_markup=types.InlineKeyboardMarkup([[
           types.InlineKeyboardButton("𝚂𝚑𝚘𝚠 𝚂𝚎𝚝𝚝𝚒𝚗𝚐𝚜",
                                      callback_data="showSettings")
        ]])
    )


@Client.on_message(filters.command("help") & filters.private & ~filters.edited)
async def help_handler(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("𝙸 𝚍𝚘𝚗'𝚝 𝚔𝚗𝚘𝚠 𝚊𝚋𝚘𝚞𝚝 𝚢𝚘𝚞 𝚍𝚞𝚍𝚎 :(")
    await add_user_to_database(c, m)
    await c.send_flooded_message(
        chat_id=m.chat.id,
        text="𝙸 𝚌𝚊𝚗 𝚛𝚎𝚗𝚊𝚖𝚎 𝚖𝚎𝚍𝚒𝚊 𝚠𝚒𝚝𝚑𝚘𝚞𝚝 𝚍𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐 𝚒𝚝!\n"
             "𝚂𝚙𝚎𝚎𝚍 𝚍𝚎𝚙𝚎𝚗𝚍𝚜 𝚘𝚗 𝚢𝚘𝚞𝚛 𝚖𝚎𝚍𝚒𝚊 𝙳𝚊𝚝𝚊 𝙲𝚎𝚗𝚝𝚎𝚛.\n\n"
             "𝙹𝚞𝚜𝚝 𝚜𝚎𝚗𝚍 𝚖𝚎 𝚖𝚎𝚍𝚒𝚊 𝚘𝚛 𝚍𝚘𝚌𝚞𝚖𝚎𝚗𝚝 𝚏𝚒𝚕𝚎 𝚊𝚗𝚍 𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚒𝚝 𝚠𝚒𝚝𝚑 /rename 𝚌𝚘𝚖𝚖𝚊𝚗𝚍.\n\n"
             "𝑇𝑜 𝑠𝑒𝑡 𝑐𝑢𝑠𝑡𝑜𝑚 𝑡ℎ𝑢𝑚𝑏𝑛𝑎𝑖𝑙 𝑟𝑒𝑝𝑙𝑦 𝑡𝑜 𝑎𝑛𝑦 𝑖𝑚𝑎𝑔𝑒 𝑤𝑖𝑡ℎ /set_thumbnail\n\n"
             "𝑇𝑜 𝑠𝑒𝑒 𝑐𝑢𝑠𝑡𝑜𝑚 𝑡ℎ𝑢𝑚𝑏𝑛𝑎𝑖𝑙 𝑝𝑟𝑒𝑠𝑠 /show_thumbnail",
        reply_markup=types.InlineKeyboardMarkup([[
           types.InlineKeyboardButton("𝚂𝚑𝚘𝚠 𝚂𝚎𝚝𝚝𝚒𝚗𝚐𝚜",
                                      callback_data="showSettings")]])
    )
