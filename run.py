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
    time.sleep(100000)

ID = config["API_ID"]
HASH = config["API_HASH"]
QUEUE_NUMBER = int(config["QUEUE_NUMBER"])
FILE_NAME = config["FILE_NAME"]
MESSAGE = config["MESSAGE"]

async def send_message(group_id, message_text):
    await client.send_message(group_id, message_text)
    print(f"message to {group_id} was successfully sent")


def get_numbers():
    try:
        result = []
        with open(FILE_NAME, "r", encoding="utf8") as file:
            f = file.readlines()
        for i in f:
            if i.strip():
                result.append(i.strip())
        return result
    except Exception as ee:
        print("Smth wrong with number's file")
        print(ee)
        time.sleep(100000)


if __name__ == "__main__":
    numbers = get_numbers()

    for i in numbers[QUEUE_NUMBER:]:
        
        with TelegramClient("anon", ID, HASH) as client:
            time.sleep(random.randrange(500, 600))

            client_id_numb = random.randrange(-2**63, 2**63)

            '''Add new contact'''
            try:
                result = client(functions.contacts.ImportContactsRequest(
                    contacts=[types.InputPhoneContact(
                        client_id=client_id_numb,
                        phone=i,
                        first_name=f'user',
                        last_name=f'{numbers.index(i)}')]))
            except Exception as e:
                print(f"smth wrong with adding new contact {i}")
                print(e)
                time.sleep(100000)
            '''Add new contact'''

            time.sleep(random.randrange(10, 15))

            '''Send message'''
            try:
                client.loop.run_until_complete(send_message(i, MESSAGE))
                print(f"number index is {numbers.index(i)}")
            except Exception as ex:
                print(f"smth wrong with sending message to {i}")
                print(ex)
                time.sleep(100000)
            '''Send message'''

            time.sleep(random.randrange(10, 15))
