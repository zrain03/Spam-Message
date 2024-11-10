from telethon import TelegramClient, errors
import asyncio
import os

# Dapatkan API_ID, API_HASH dan nama fail sesi dari environment variables
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_name = os.getenv("SESSION_NAME", "my_session")  # Nama fail sesi yang digunakan

# ID kumpulan dan mesej yang ingin dihantar
group_id = -1002200241778  # ID kumpulan "Testing for MP CHAT"
message = "maaf"

# Buat klien Telegram
client = TelegramClient(session_name, api_id, api_hash)

# Fungsi untuk menghantar mesej 100 kali
async def send_message_repeatedly():
    await client.start()  # Log masuk jika belum log masuk
    try:
        # Cuba untuk mengakses kumpulan
        await client.get_entity(group_id)
    except errors.ChatAdminRequiredError:
        print("Akses ke kumpulan ini tidak dibenarkan.")
        return
    except ValueError:
        print("ID kumpulan tidak sah atau anda tidak mempunyai akses.")
        return

    # Hantar mesej 100 kali
    for i in range(25):
        await client.send_message(group_id, message)
        print(f"Mesej ke-{i+1} telah dihantar!")
        await asyncio.sleep(3)  # Tunggu 1 saat antara mesej

# Jalankan fungsi untuk menghantar mesej
with client:
    client.loop.run_until_complete(send_message_repeatedly())
