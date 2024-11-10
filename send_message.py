from telethon import TelegramClient, errors
import asyncio
import os

# Dapatkan API_ID, API_HASH dan nama fail sesi dari environment variables
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_name = os.getenv("SESSION_NAME", "my_session")  # Nama fail sesi yang digunakan

# ID kumpulan dan mesej yang ingin dihantar
group_ids = [-1002200241778, -1002288720559, -1001161916810, -1001897381179, -1002056756757, 
             -1001656152814, -1001641889050, -1002032128619, -1001513360832, -1002083219543, 
             -1001338686972, -1002080497857, -1001194015232, -1002080593272, -1001473865431, 
             -1001778610644, -1002065798504, -1002329458039, -1002379900836, -1001192339217, 
             -1001875616025, -1001938068566, -1001626914578, -1002174886965, -1001965994500]  # ID kumpulan "Testing for MP CHAT" dan satu lagi kumpulan
message = "https://t.me/mpgoviralgrowthtools (admin share 3 kali MP goviral setiap hari)"

# Buat klien Telegram
client = TelegramClient(session_name, api_id, api_hash)

# Fungsi untuk menghantar mesej 100 kali
async def send_message_repeatedly():
    await client.start()  # Log masuk jika belum log masuk
    try:
        # Cuba untuk mengakses kumpulan
        for group_id in group_ids:
            await client.get_entity(group_id)
    except errors.ChatAdminRequiredError:
        print("Akses ke kumpulan ini tidak dibenarkan.")
        return
    except ValueError:
        print("ID kumpulan tidak sah atau anda tidak mempunyai akses.")
        return

    # Hantar mesej kepada setiap kumpulan
    for i in range(2):
        for group_id in group_ids:
            await client.send_message(group_id, message)
            print(f"Mesej ke-{i+1} telah dihantar ke kumpulan {group_id}!")
        await asyncio.sleep(30)  # Tunggu 3600 saat / 1 jam antara mesej

# Jalankan fungsi untuk menghantar mesej
with client:
    client.loop.run_until_complete(send_message_repeatedly())
