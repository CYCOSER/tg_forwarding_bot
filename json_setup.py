import json

def confirm_input(prompt_name):
    while True:
        value = input(f"Please enter {prompt_name}: ")
        confirm = input(f"Is \"{value}\" correct? (y/n): ").strip().lower()

        while confirm not in ["y", "n", "yes", "no"]:
            confirm = input(f"Incorrect answer, is \"{value}\" correct? (y/n): ").strip().lower()

        if confirm in ["y", "yes"]:
            return value

def json_setup():
    print("Welcome! Let's get started!")

    config_keys = ["API_ID", "API_HASH", "BOT_TOKEN", "MAIN_CHAT_ID"]
    config = {key: confirm_input(key) for key in config_keys}

    with open("config.json", "w", encoding="utf-8") as f:
        json.dump([config], f, ensure_ascii=False, indent=4)

    with open("admin_list.json", "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=4)

    print("Setup complete! Please restart the app.")
    input("Press Enter to exit...")
