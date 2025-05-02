import asyncio
import json
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from scheduled_events import scheduled_fwd, admin_list_update

from json_setup import json_setup
from pyrogram import Client, idle

async def main():
    try:
        with open('config.json', 'r') as f:
            data = json.load(f)
            userbot = Client(
                name="userbot",
                api_id=data[0]["API_ID"],
                api_hash=data[0]["API_HASH"],
                plugins=dict(root="userbot_plugins")
            )

            bot = Client(
                name="bot",
                bot_token=data[0]["BOT_TOKEN"],
                api_id=data[0]["API_ID"],
                api_hash=data[0]["API_HASH"],
                plugins=dict(root="bot_plugins")
            )

            await userbot.start()
            await bot.start()

            scheduler = AsyncIOScheduler()
            scheduler.add_job(scheduled_fwd, trigger="interval", seconds=10, args=[userbot])
            scheduler.add_job(admin_list_update, trigger="interval", seconds=30, args=[userbot])
            scheduler.start()

            await idle()
            await userbot.stop()
            await bot.stop()

    except FileNotFoundError:
        json_setup()

asyncio.run(main())