import random
import string
import time
import requests

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

var = "https://discord.com/billing/promotions/"
webhook_url = "webhook_url_here" # Type your webhook url here

while True:
    random_string = generate_random_string(22)
    output = var + random_string + var + random_string
    payload = {"content": output}
    requests.post(webhook_url, json=payload)
    time.sleep(0.2)  # Sleep for 0.2 seconds (1/5 of a second) to achieve 5Hz frequency

