import json

from telethon import TelegramClient


async def send_message(message_text, group_id):
    await client.send_message(group_id, message_text)
    print(f"message to {group_id} was successfully sent")


def get_config():
    try:
        with open('config.json') as config_json:
            config = json.load(config_json)
    except json.decoder.JSONDecodeError:
        print("something with Json config")


def get_numbers():
    result = []
    with open("numbers.txt", "r", encoding="utf8") as file:
        f = file.readlines()
    for i in f:
        if i.strip():
            result.append(i.strip())
    return result


if __name__ == "__main__":
    client = TelegramClient('anon', API_ID, API_HASH)
    print(get_numbers())
