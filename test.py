from telethon import TelegramClient
import asyncio
import os

# Mengambil API ID, API Hash, dan sesi dari environment variables
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_name = os.getenv("SESSION_NAME")

# ID grup
group_id = -10022200241778

# Mesej yang ingin dihantar
message = "Maaf"

# Membuat klien Telegram
client = TelegramClient(session_name, api_id, api_hash)

# Fungsi untuk mengirim pesan beberapa kali dengan jeda
async def send_message_repeatedly():
    await client.start()
    for i in range(10000):
        await client.send_message(group_id, message)
        print(f"Mesej ke-{i+1} telah dihantar!")
        await asyncio.sleep(1)  # Jeda 1 detik antara setiap pesan

# Jalankan fungsi
with client:
    client.loop.run_until_complete(send_message_repeatedly())
