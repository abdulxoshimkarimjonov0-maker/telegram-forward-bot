import os, asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.errors import FloodWaitError

API_ID = int(os.getenv("25160319"))
API_HASH = os.getenv("91cb0805c2623fda9b91ab922d5bb3f9")
SESSION_STRING = os.getenv("1ApWapzMBu4w958H9PEN1q2nlrmxNRLICvyvUoXnp6FfUlBmwkSqMoe4mbQUBiS-hPtZqnz3GY5eGw0t-3QoVSsyR1ub9CkQ_NGEcAU1Iqx6ZIiSAWAYQCo0GnylYb6dq9psdV7RdpjayJJgdjqv3GIMpkETfI9wroPMXvSK9Es99mySOiYsE6aigmDPIueeTp02h4U6S_zDLM7h-az6cid_DA7uzOsApp2mJb1yWTG4IAK0Xu0qw_fKX10t8kGgZqxx20AkEcjyudBFdO8Oqq3vkX5FztPcFVCrI6zbOeWygG09-vtoPdokEPDBXnug11TbtczSmKQXZN_TCJr3iDXbBJpvhdeE=")

SOURCE_CHAT = int(os.getenv("-1002772634438"))     # masalan: -100123...
MESSAGE_ID   = int(os.getenv("3"))     # forward qilinadigan xabar ID

# TARGET_CHATS ni Secrets’da vergul bilan yozing:  -100111,-100222,-100333
def parse_targets(s: str):
    return [int(x.strip()) for x in s.split(",") if x.strip()]

TARGET_CHATS = parse_targets(os.getenv("TARGET_CHATS", "-1002500832549"))

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

async def main():
    await client.start()
    print("✅ Ishga tushdi. Targetlar:", TARGET_CHATS)

    while True:
        for chat in TARGET_CHATS:
            try:
                # 1-argument: bitta chat; 2-argument: xabar ID; 3-argument: manba chat
                await client.forward_messages(chat, MESSAGE_ID, SOURCE_CHAT)
                print(f"➡️ Forward OK: {chat}")
            except FloodWaitError as e:
                print(f"⏳ FloodWait {e.seconds}s (chat {chat})")
                await asyncio.sleep(e.seconds)
            except Exception as e:
                print(f"⚠️ Xato ({chat}): {e}")
        await asyncio.sleep(15)  # 5 minut

asyncio.run(main())
