import telethon


API_ID = config["API_ID"]
API_HASH = config["API_HASH"]


client = TelegramClient('anon', API_ID, API_HASH)

async def send_message(message_text, group_id):
    await client.send_message(group_id, message_text)
    print(f"message to {group_id} was successfully sent")

def get_numbers():
    result = []
    with open("numbers.txt", "r", encoding="utf8") as file:
        f = file.readlines()
    for i in f:
        if i.strip():
            result.append(i.strip())
    return result
print(get_numbers())
