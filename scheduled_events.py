import json

from pyrogram.enums import ChatMembersFilter


async def scheduled_fwd(userbot):
    with open("config.json", "r") as f:
        data = json.load(f)

    main_chat_id = data[0]["MAIN_CHAT_ID"]

    for entry in data[1:]:
        chat_id = int(entry["CHAT_ID"])
        last_time = entry.get("LAST_POST_TIME", 0)
        new_last_time = last_time

        post_list = [post async for post in userbot.get_chat_history(chat_id=chat_id, limit=10)]

        for post in reversed(post_list):
            post_time = post.date.timestamp()
            if post_time > last_time:
                try:
                    await userbot.forward_messages(
                    chat_id=main_chat_id,
                    from_chat_id=chat_id,
                    message_ids=post.id
                    )
                    new_last_time = max(new_last_time, post_time)

                except:
                    print(f"There are troubles with forwarding from {userbot.get_chat(chat_id).title}{chat_id}")

        entry["LAST_POST_TIME"] = new_last_time

    with open("config.json", "w") as f:
        json.dump(data, f, indent=4)

async def admin_list_update(userbot):
    with open('config.json', 'r') as f:
        admin_list = []
        data = json.load(f)
        async for member in userbot.get_chat_members(
                chat_id=data[0]['MAIN_CHAT_ID'],
                filter=ChatMembersFilter.ADMINISTRATORS
        ):
            admin_list.append({
                "id": member.user.id,
                "username": member.user.username
            })

        with open("admin_list.json", "r") as af:
            admin_data = json.load(af)
            if admin_data == admin_list:
                return

        with open("admin_list.json", "w") as af:
            json.dump(admin_list, af, indent=4)

