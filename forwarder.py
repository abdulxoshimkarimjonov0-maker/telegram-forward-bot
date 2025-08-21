from telethon import TelegramClient
from telethon.sessions import StringSession
import asyncio

api_id = 25160319   # o'z API_ID
api_hash = "91cb0805c2623fda9b91ab922d5bb3f9"  # o'z API_HASH
string = "1ApWapzMBu4w958H9PEN1q2nlrmxNRLICvyvUoXnp6FfUlBmwkSqMoe4mbQUBiS-hPtZqnz3GY5eGw0t-3QoVSsyR1ub9CkQ_NGEcAU1Iqx6ZIiSAWAYQCo0GnylYb6dq9psdV7RdpjayJJgdjqv3GIMpkETfI9wroPMXvSK9Es99mySOiYsE6aigmDPIueeTp02h4U6S_zDLM7h-az6cid_DA7uzOsApp2mJb1yWTG4IAK0Xu0qw_fKX10t8kGgZqxx20AkEcjyudBFdO8Oqq3vkX5FztPcFVCrI6zbOeWygG09-vtoPdokEPDBXnug11TbtczSmKQXZN_TCJr3iDXbBJpvhdeE="  # oldindan olingan String Session

# Forward qilinadigan sozlamalar
SOURCE_CHAT = -1002772634438   # manba guruh
SOURCE_MSG_ID = 3            # qaysi xabarni forward qilish kerak
TARGET_CHAT = -1002500832549   # bitta maqsad guruh

async def main():
    client = TelegramClient(StringSession(string), api_id, api_hash)
    await client.start()

    while True:
        try:
            await client.forward_messages(TARGET_CHAT, SOURCE_MSG_ID, SOURCE_CHAT)
            print("✅ Xabar forward qilindi")
        except Exception as e:
            print("⚠️ Xatolik:", e)
        await asyncio.sleep(300)  # har 5 minutda
        

if __name__ == "__main__":
    asyncio.run(main())
