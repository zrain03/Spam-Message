from telethon import TelegramClient
import asyncio
import os

# Dapatkan API ID dan API Hash daripada GitHub Secrets
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_name = os.getenv("SESSION_NAME")  # Nama fail sesi yang digunakan

# ID grup dan mesej yang ingin dihantar
group_id = -10022200241778
message = "Maaf"

# Buat klien Telegram
client = TelegramClient(session_name, api_id, api_hash)

# Fungsi untuk menghantar mesej beberapa kali
async def send_message_repeatedly():
    await client.start()
    for i in range(10000):
        await client.send_message(group_id, message)
        print(f"Mesej ke-{i+1} telah dihantar!")
        await asyncio.sleep(1)

# Jalankan fungsi utama
with client:
    client.loop.run_until_complete(send_message_repeatedly())
