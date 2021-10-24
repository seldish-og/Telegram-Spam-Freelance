import json

from telethon import TelegramClient

try:
    with open("config.json") as config_json:
        config = json.load(config_json)

except json.decoder.JSONDecodeError:
        print("something wrong with Json config")

# client = TelegramClient('anon', config["API_ID"], config["API_HASH"])


async def send_message(group_id, message_text):
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


if __name__ == "__main__":
    numbers = get_numbers()
    queue_number = int(config["queue_number"])
    for i in numbers[queue_number:]:
        print(i)
