from pyrogram import Client
from config import CONFIG

Client.UPDATES_WORKERS = CONFIG.pyrogram.updates_workers


def main():
    app = Client(
        "Firewatch",
        api_id=CONFIG.pyrogram.api_id,
        api_hash=CONFIG.pyrogram.api_hash,
        app_version="Firewatch",
        lang_code=CONFIG.pyrogram.lang_code,
        bot_token=CONFIG.pyrogram.bot_token,
        workers=CONFIG.pyrogram.workers,
        plugins=dict(root="firewatch"),
        proxy=CONFIG.proxy
    )
    app.run()


if __name__ == "__main__":
    main()
