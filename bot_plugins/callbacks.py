import time

from pyrogram import Client
from bot_contents.texts import start_text, already_in_queue, not_in_queue
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import json


@Client.on_callback_query()
async def callback_handler(client, callback_query):
    data=callback_query.data

    if data == "back":
        await callback_query.message.edit_text(start_text)

    if data.startswith("add_channel_fwd"):
        channel_id = data[16:]

        with open("config.json", "r") as f:
            jdata = json.load(f)

        already_exists = any(item.get("CHAT_ID") == channel_id for item in jdata)

        if already_exists:
            await callback_query.message.edit_text(
                text=already_in_queue,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="Удалить канал",
                                callback_data=f"delete_channel_fwd {channel_id}"
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                text="Отмена",
                                callback_data="back"
                            )
                        ]
                    ]
                )
            )
        else:
            jdata.append({
                "CHAT_ID": channel_id,
                "LAST_POST_TIME": time.time()
            })
            with open("config.json", "w") as f:
                json.dump(jdata, f, indent=4)
            await callback_query.answer("✔️ Канал был успешно добавлен в очередь!")
            await callback_query.message.edit_text(start_text)

    if data.startswith("delete_channel_fwd"):
        channel_id = data[19:]

        with open("config.json", "r") as f:
            jdata = json.load(f)

        index_to_remove = next(
            (i for i, item in enumerate(jdata) if item.get("CHAT_ID") == channel_id),
            None
        )

        if index_to_remove is not None:
            jdata.pop(index_to_remove)
            with open("config.json", "w") as f:
                json.dump(jdata, f, indent=4)
            await callback_query.answer("✔️ Канал был успешно удален из очереди!")
            await callback_query.message.edit_text(start_text)

        else:
            await callback_query.message.edit_text(
                text=not_in_queue,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="Добавить канал",
                                callback_data=f"add_channel_fwd {channel_id}"
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                text="Отмена",
                                callback_data="back"
                            )
                        ]
                    ]
                )
            )
