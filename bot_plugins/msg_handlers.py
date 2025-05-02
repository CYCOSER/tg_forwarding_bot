import asyncio

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from bot_contents.texts import start_text, no_permission_text
import json

handled_groups = set()

@Client.on_message(filters.command("start") & filters.private)
async def start(client, cmd):
    with open("admin_list.json", "r") as f:
        admin_data = json.load(f)
        if cmd.from_user.id in [i["id"] for i in admin_data]:
            await cmd.reply_text(text=start_text)

        else:
            await cmd.reply_text(text=no_permission_text)


@Client.on_message(filters.forwarded)
async def forwarded_handler(client, message):
    with open("admin_list.json", "r") as f:
        admin_data = json.load(f)
        if message.from_user.id in [i["id"] for i in admin_data]:
            group_id = message.media_group_id

            if group_id:
                if group_id in handled_groups:
                    return

                handled_groups.add(group_id)
                asyncio.create_task(remove_from_cache(group_id))

            if message.forward_from_chat:
                channel_id = message.forward_from_chat.id
                await message.reply_text(
                    text="📑 Вы хотели бы добавить этот канал в список, или удалить?",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="➕ Добавить канал",
                                    callback_data=f"add_channel_fwd {channel_id}",
                                ),
                                InlineKeyboardButton(
                                    text="➖ Удалить канал",
                                    callback_data=f"delete_channel_fwd {channel_id}",
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    text="❌ Отмена",
                                    callback_data="back"
                                )
                            ]
                        ]
                    )
                )
            else:
                await message.reply_text("⚠️ Похоже, что этот канал закрыт для ботов ⚠️")

        else:
            await message.reply_text(text=no_permission_text)

async def remove_from_cache(group_id):
    await asyncio.sleep(30)
    handled_groups.discard(group_id)