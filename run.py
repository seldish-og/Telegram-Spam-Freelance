import json
from os import times
import random
from telethon.sync import TelegramClient
from telethon import functions, types
import time

from telethon import TelegramClient

try:
    with open("config.json") as config_json:
        config = json.load(config_json)

except json.decoder.JSONDecodeError:
        print("something wrong with Json config")


ID = config["API_ID"]
HASH = config["API_HASH"]
QUEUE_NUMBER = int(config["QUEUE_NUMBER"])


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

    for i in numbers[QUEUE_NUMBER:]:
        with TelegramClient("anon", ID, HASH) as client:

            client_id_numb = random.randrange(-2**63, 2**63)

            '''Add new contact'''
            try:
                result = client(functions.contacts.ImportContactsRequest(
                    contacts=[types.InputPhoneContact(
                        client_id=client_id_numb,
                        phone='some string here',
                        first_name=f'{client_id_numb + "user"}',
                        last_name=f'{client_id_numb + "user"}')]))
            except Exception as e:
                print(f"smth wrong with adding new contact {i}")
                print(e)
            '''Add new contact'''

            time.sleep(10)

            '''Send message'''
            try:
                client.loop.run_until_complete(send_message(i, "hi"))
            except Exception as ex:
                print(f"smth wrong with sending message to {i}")
                print(ex)
            '''Send message'''
