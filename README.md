# 📬 Telegram Forwarding Bot

A Telegram bot built with **Pyrogram** that automatically forwards messages from multiple channels or chats into a single one.

## 🚀 Features

- ➕ **Add/remove** source channels **dynamically**
- 🔁 **Automatically** forwards new messages
- 🛡 **Admin-only access** to bot controls
- 🐍 Built with **Python 3.11** and **Pyrogram**

## 🛠 Requirements

- Python 3.11 or newer
- Telegram API credentials: `API_ID`, `API_HASH`, `BOT_TOKEN`
- Dependencies listed in `requirements.txt`

## 📦 Installation

### 1. Install Python  
Download and install Python 3.11+ from:  
👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)

### 2. Clone the repository

```bash
git clone https://github.com/CYCOSER/tg_forwarding_bot
```
```bash
cd tg_forwarding_bot
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run main.py

Run program for the first time:

```bash
python3 main.py
```

You'll be prompted to enter:
- `API_ID`
- `API_HASH`
- `BOT_TOKEN`
- `MAIN_CHAT_ID` (the destination where messages will be forwarded)


### 5. Restart main.py 

Restart main.py

```bash
python main.py
```

You will be prompted to log into Telegram accout that will forward the posts


## ▶️ Usage

Start the bot:

```bash
python main.py
```

To add a channel to the forwarding list, simply forward any message from that channel to the bot.
