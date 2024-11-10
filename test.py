from telethon import TelegramClient
import asyncio

# API ID dan API Hash
api_id = 20240995
api_hash = "a6cb8eb76c7e91215e483416a29dc0e0"

# Nama sesi sederhana
session_name = 'my_session'

# ID grup
group_id = -10022200241778

# Mesej yang ingin dihantar
message = "Maaf"

# Membuat klien Telegram
client = TelegramClient(session_name, api_id, api_hash)

# Fungsi untuk mengirim pesan beberapa kali dengan jeda
async def send_message_repeatedly():
    await client.start()
    for i in range(10000):  # Contoh mengirim 10000 kali untuk keamanan
        await client.send_message(group_id, message)
        print(f"Mesej ke-{i+1} telah dihantar!")
        await asyncio.sleep(1)  # Jeda 1 detik antara setiap pesan

# Jalankan fungsi
with client:
    client.loop.run_until_complete(send_message_repeatedly())
