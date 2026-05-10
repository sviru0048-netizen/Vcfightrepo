# =========================================
# KRISH X STAR LIVE VC COMMANDS
# =========================================

from pyrogram import Client, filters

from core.vcplayer.live import LiveVC

live_clients = {}


@Client.on_message(filters.command("live"))
async def start_live(client, message):

    chat_id = message.chat.id

    try:

        live = LiveVC(client, chat_id)

        live_clients[chat_id] = live

        await message.reply_text(
            "🎙️ LIVE VC STARTED"
        )

        await live.start_live()

    except Exception as e:

        await message.reply_text(
            f"❌ ERROR:\n{e}"
        )
