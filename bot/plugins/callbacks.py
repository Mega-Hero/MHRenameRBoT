# (c) @AbirHasan2005

from pyrogram import types
from bot.client import Client
from bot.core.db.database import db
from bot.core.file_info import (
    get_media_file_name,
    get_media_file_size,
    get_file_type,
    get_file_attr
)
from bot.core.display import humanbytes
from bot.core.handlers.settings import show_settings


@Client.on_callback_query()
async def cb_handlers(c: Client, cb: "types.CallbackQuery"):
    if cb.data == "showSettings":
        await cb.answer()
        await show_settings(cb.message)
    elif cb.data == "showThumbnail":
        thumbnail = await db.get_thumbnail(cb.from_user.id)
        if not thumbnail:
            await cb.answer("𝑌𝑜𝑢 𝑑𝑖𝑑𝑛'𝑡 𝑠𝑒𝑡 𝑎𝑛𝑦 𝑐𝑢𝑠𝑡𝑜𝑚 𝑡ℎ𝑢𝑚𝑏𝑛𝑎𝑖𝑙!", show_alert=True)
        else:
            await cb.answer()
            await c.send_photo(cb.message.chat.id, thumbnail, "𝑪𝒖𝒔𝒕𝒐𝒎 𝑻𝒉𝒖𝒎𝒃𝒏𝒂𝒊𝒍",
                               reply_markup=types.InlineKeyboardMarkup([[
                                   types.InlineKeyboardButton("Delete Thumbnail",
                                                              callback_data="deleteThumbnail")
                               ]]))
    elif cb.data == "deleteThumbnail":
        await db.set_thumbnail(cb.from_user.id, None)
        await cb.answer("Oᴋᴀʏ, I ᴅᴇʟᴇᴛᴇᴅ ʏᴏᴜʀ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ. Nᴏᴡ I ᴡɪʟʟ ᴀᴘᴘʟʏ ᴅᴇғᴀᴜʟᴛ ᴛʜᴜᴍʙɴᴀɪʟ.", show_alert=True)
        await cb.message.delete(True)
    elif cb.data == "setThumbnail":
        await cb.answer()
        await cb.message.edit("𝑆𝑒𝑛𝑑 𝑚𝑒 𝑎𝑛𝑦 𝑝ℎ𝑜𝑡𝑜 𝑡𝑜 𝑠𝑒𝑡 𝑡ℎ𝑎𝑡 𝑎𝑠 𝑐𝑢𝑠𝑡𝑜𝑚 𝑡ℎ𝑢𝑚𝑏𝑛𝑎𝑖𝑙.\n\n"
                              "𝙿𝚛𝚎𝚜𝚜 /cancel 𝚝𝚘 𝚌𝚊𝚗𝚌𝚎𝚕 𝚙𝚛𝚘𝚌𝚎𝚜𝚜.")
        from_user_thumb: "types.Message" = await c.listen(cb.message.chat.id)
        if not from_user_thumb.photo:
            await cb.message.edit("ℙ𝕣𝕠𝕔𝕖𝕤𝕤 ℂ𝕒𝕟𝕔𝕖𝕝𝕝𝕖𝕕!")
            return await from_user_thumb.continue_propagation()
        else:
            await db.set_thumbnail(cb.from_user.id, from_user_thumb.photo.file_id)
            await cb.message.edit("OKᗩY!\n"
                                  "𝐍𝐨𝐰 𝐈 𝐰𝐢𝐥𝐥 𝐚𝐩𝐩𝐥𝐲 𝐭𝐡𝐢𝐬 𝐭𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐭𝐨 𝐧𝐞𝐱𝐭 𝐮𝐩𝐥𝐨𝐚𝐝𝐬.",
                                  reply_markup=types.InlineKeyboardMarkup(
                                      [[types.InlineKeyboardButton("Show Settings",
                                                                   callback_data="showSettings")]]
                                  ))
    elif cb.data == "setCustomCaption":
        await cb.answer()
        await cb.message.edit("OKᗩY,\n"
                              "Send me your custom caption.\n\n"
                              "Press /cancel to cancel process.")
        user_input_msg: "types.Message" = await c.listen(cb.message.chat.id)
        if not user_input_msg.text:
            await cb.message.edit("Process Cancelled!")
            return await user_input_msg.continue_propagation()
        if user_input_msg.text and user_input_msg.text.startswith("/"):
            await cb.message.edit("Process Cancelled!")
            return await user_input_msg.continue_propagation()
        await db.set_caption(cb.from_user.id, user_input_msg.text.markdown)
        await cb.message.edit("Custom Caption Added Successfully!",
                              reply_markup=types.InlineKeyboardMarkup(
                                  [[types.InlineKeyboardButton("Show Settings",
                                                               callback_data="showSettings")]]
                              ))
    elif cb.data == "triggerApplyCaption":
        await cb.answer()
        apply_caption = await db.get_apply_caption(cb.from_user.id)
        if not apply_caption:
            await db.set_apply_caption(cb.from_user.id, True)
        else:
            await db.set_apply_caption(cb.from_user.id, False)
        await show_settings(cb.message)
    elif cb.data == "triggerApplyDefaultCaption":
        await db.set_caption(cb.from_user.id, None)
        await cb.answer("Okay, now I will keep default caption.", show_alert=True)
        await show_settings(cb.message)
    elif cb.data == "showCaption":
        caption = await db.get_caption(cb.from_user.id)
        if not caption:
            await cb.answer("You didn't set any custom caption!", show_alert=True)
        else:
            await cb.answer()
            await cb.message.edit(
                text=caption,
                parse_mode="Markdown",
                reply_markup=types.InlineKeyboardMarkup([[
                    types.InlineKeyboardButton("Go Back", callback_data="showSettings")
                ]])
            )
    elif cb.data == "triggerUploadMode":
        await cb.answer()
        upload_as_doc = await db.get_upload_as_doc(cb.from_user.id)
        if upload_as_doc:
            await db.set_upload_as_doc(cb.from_user.id, False)
        else:
            await db.set_upload_as_doc(cb.from_user.id, True)
        await show_settings(cb.message)
    elif cb.data == "showFileInfo":
        replied_m = cb.message.reply_to_message
        _file_name = get_media_file_name(replied_m)
        text = f"**File Name:** `{_file_name}`\n\n" \
               f"**File Extension:** `{_file_name.rsplit('.', 1)[-1].upper()}`\n\n" \
               f"**File Type:** `{get_file_type(replied_m).upper()}`\n\n" \
               f"**File Size:** `{humanbytes(get_media_file_size(replied_m))}`\n\n" \
               f"**File MimeType:** `{get_file_attr(replied_m).mime_type}`"
        await cb.message.edit(
            text=text,
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=types.InlineKeyboardMarkup(
                [[types.InlineKeyboardButton("Close Message", callback_data="closeMessage")]]
            )
        )
    elif cb.data == "closeMessage":
        await cb.message.delete(True)
