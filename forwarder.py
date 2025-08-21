import asyncio
from telethon import TelegramClient

api_id = 25160319
api_hash = "91cb0805c2623fda9b91ab922d5bb3f9"
session_name = "my_account"

SOURCE_CHAT = -1002772634438   # Manba guruh
MESSAGE_ID = 3                # Forward qilinadigan xabar
TARGET_CHAT = -1002500832549   # Qabul qiluvchi guruh

async def main():
    client = TelegramClient(session_name, api_id, api_hash)
    await client.start()

    msg = await client.get_messages(SOURCE_CHAT, ids=MESSAGE_ID)

    while True:
        try:
            await client.forward_messages(TARGET_CHAT, msg)  # faqat bitta guruh!
            print("➡️ Xabar forward qilindi!")
        except Exception as e:
            print(f"⚠️ Xatolik: {e}")

        await asyncio.sleep(15)

asyncio.run(main())
