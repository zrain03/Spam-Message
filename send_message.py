from telethon import TelegramClient, errors
import asyncio
import os

# Dapatkan API ID dan API Hash daripada GitHub Secrets
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_name = os.getenv("SESSION_NAME", "my_session")  # Nama fail sesi yang digunakan, default ke 'my_session'

# ID grup dan mesej yang ingin dihantar
group_id = -10022200241778  # Pastikan ini adalah ID kumpulan yang betul
message = "Maaf"

# Buat klien Telegram
client = TelegramClient(session_name, api_id, api_hash)

# Fungsi untuk menghantar mesej beberapa kali
async def send_message_repeatedly():
    await client.start()
    print("Memulakan sesi...")
    try:
        # Cuba untuk mengakses kumpulan terlebih dahulu
        entity = await client.get_input_entity(group_id)
        print(f"Berjaya mengakses kumpulan: {entity}")
    except errors.ChatAdminRequiredError:
        print("Akses ke kumpulan ini tidak dibenarkan.")
        return
    except ValueError:
        print("ID kumpulan tidak sah atau anda tidak mempunyai akses.")
        return
    except IndexError:
        print("Tidak dapat mencari entiti untuk ID kumpulan yang diberikan.")
        return

    # Menghantar mesej jika berjaya mendapat akses ke kumpulan
    for i in range(10000):
        await client.send_message(group_id, message)
        print(f"Mesej ke-{i+1} telah dihantar!")
        await asyncio.sleep(1)

# Jalankan fungsi utama
with client:
    client.loop.run_until_complete(send_message_repeatedly())
