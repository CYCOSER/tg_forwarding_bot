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

    if data.startswith("acf"):
        channel_id = data[3:17]
        channel_name = data[17:]

        with open("config.json", "r", encoding="utf-8") as f:
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
                                callback_data=f"dcf{channel_id}{channel_name}",
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
                "CHAT_NAME": channel_name,
                "LAST_POST_TIME": time.time()
            })
            with open("config.json", "w") as f:
                json.dump(jdata, f, ensure_ascii=False, indent=4)
            await callback_query.answer("✔️ Канал был успешно добавлен в очередь!")
            await callback_query.message.edit_text(start_text)

    if data.startswith("dcf"):
        channel_id = data[4:17]
        channel_name = data[17:]

        with open("config.json", "r", encoding="utf-8") as f:
            jdata = json.load(f)

        index_to_remove = next(
            (i for i, item in enumerate(jdata) if item.get("CHAT_ID") == channel_id),
            None
        )

        if index_to_remove is not None:
            jdata.pop(index_to_remove)
            with open("config.json", "w") as f:
                json.dump(jdata, f, ensure_ascii=False, indent=4)
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
                                callback_data=f"acf{channel_id}{channel_name}"
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
