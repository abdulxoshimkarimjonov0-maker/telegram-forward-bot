import os, asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.errors import FloodWaitError

def env(name: str) -> str:
    v = os.getenv(name)
    if not v or not str(v).strip():
        raise RuntimeError(f"Environment variable '{name}' kiritilmagan. Replit → Secrets bo'limida qo'shing.")
    return v.strip()

API_ID = int(env("25160319"))
API_HASH = env("91cb0805c2623fda9b91ab922d5bb3f9")
SESSION_STRING = env("1ApWapzMBu4w958H9PEN1q2nlrmxNRLICvyvUoXnp6FfUlBmwkSqMoe4mbQUBiS-hPtZqnz3GY5eGw0t-3QoVSsyR1ub9CkQ_NGEcAU1Iqx6ZIiSAWAYQCo0GnylYb6dq9psdV7RdpjayJJgdjqv3GIMpkETfI9wroPMXvSK9Es99mySOiYsE6aigmDPIueeTp02h4U6S_zDLM7h-az6cid_DA7uzOsApp2mJb1yWTG4IAK0Xu0qw_fKX10t8kGgZqxx20AkEcjyudBFdO8Oqq3vkX5FztPcFVCrI6zbOeWygG09-vtoPdokEPDBXnug11TbtczSmKQXZN_TCJr3iDXbBJpvhdeE=")

SOURCE_CHAT = int(env("-1002772634438"))      # masalan: -1001234567890
MESSAGE_ID  = int(env("MESSAGE_ID"))       # masalan: 55
TARGET_CHATS = [int(x) for x in env("TARGET_CHATS").split("-1002305699151,-1001919071943,-1002437075012,-1002311823407,-1002377383060,-1002016923230,-1002849134056,-1002741551279,-1002526964072,-1002222348198,-1002778498963,-1002500832549")]

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

async def main():
    await client.start()
    print("✅ Ishga tushdi. Targetlar:", TARGET_CHATS)

    while True:
        for chat in TARGET_CHATS:
            try:
                await client.forward_messages(chat, MESSAGE_ID, SOURCE_CHAT)
                print(f"➡️ Forward OK: {chat}")
            except FloodWaitError as e:
                print(f"⏳ FloodWait {e.seconds}s (chat {chat})")
                await asyncio.sleep(e.seconds)
            except Exception as e:
                print(f"⚠️ Xato ({chat}): {e}")
        await asyncio.sleep(300)  # 5 minut

asyncio.run(main())
