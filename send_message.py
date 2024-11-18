from telethon import TelegramClient, errors
import os

# Get API_ID, API_HASH, and session name from environment variables
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_name = os.getenv("SESSION_NAME", "my_session")

# Group IDs and the message to be sent
group_ids = [
    -1002200241778, -1002288720559, -1001161916810, -1001897381179, -1002056756757,
    -1001656152814, -1001641889050, -1002032128619, -1001513360832, -1002083219543,
    -1001338686972, -1002080497857, -1001194015232, -1002080593272, -1001473865431,
    -1001778610644, -1002065798504, -1002329458039, -1002379900836, -1001192339217,
    -1001875616025, -1001938068566, -1001626914578, -1002174886965, -1001965994500
]
message = """New Task Tele By @nurazylahh
Link Group: https://t.me/+tjqzu74AnN4yMTA9

📌 0.02 sen/Acc
📌 Join & Send SS
📌 Claim To Pm @nurazylahh
❌ Tolong Jangan Left Bila Dah Join Group"""

# Initialize Telegram client
client = TelegramClient(session_name, api_id, api_hash)


async def send_messages():
    await client.start()  # Log in if not already logged in
    for group_id in group_ids:
        try:
            await client.send_message(group_id, message)
            print(f"Message sent to group {group_id}")
        except errors.ChatAdminRequiredError:
            print(f"Access to group {group_id} is restricted.")
        except errors.FloodWaitError as e:
            print(f"Rate limit reached. Sleeping for {e.seconds} seconds.")
            await asyncio.sleep(e.seconds)
        except ValueError:
            print(f"Invalid group ID {group_id} or access denied.")
        except Exception as e:
            print(f"Unexpected error for group {group_id}: {e}")


# Run the function to send messages
with client:
    client.loop.run_until_complete(send_messages())
