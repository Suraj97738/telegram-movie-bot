import os
from pyrogram import Client, filters
from motor.motor_asyncio import AsyncIOMotorClient

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
MONGO_URI = os.environ.get("MONGO_URI")

mongo = AsyncIOMotorClient(MONGO_URI)
db = mongo.moviebot.files

app = Client(
    "moviebot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(_, msg):
    await msg.reply_text(
        "🎬 Movie Bot Online!\n\nSend movie name to search."
    )

app.run()
