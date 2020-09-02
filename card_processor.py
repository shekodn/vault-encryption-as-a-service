import requests
import base64
import json

VAULT_TOKEN = "the-token"
API_ADDR = "http://127.0.0.1:8000"
CARD_PATH = "/credit-cards/"
VAULT_URI = "http://127.0.0.1:8200/v1/transit/decrypt/api"

_headers = {
    "X-Vault-Token": VAULT_TOKEN,
    "Content-Type": "application/json",
}

def get_plaintext(message):

    data = {"ciphertext": message}    
    json_object = json.dumps(data, indent=4)

    response = requests.post(
        VAULT_URI,
        headers=_headers,
        data=json_object,
    )

    res = response.json()
    plaintext = res['data']['plaintext']
    plaintext_bytes = base64.b64decode(plaintext)
    return plaintext_bytes.decode("ascii")


if __name__ == "__main__":
    response = requests.get(
        API_ADDR + CARD_PATH,
    )

    cards = response.json()
    for card in cards:
        card_holder = card['name']
        encrypted_pan = card['pan']
        pan = get_plaintext(encrypted_pan)
        print(f"Processing {card_holder.upper()} card with number {pan}")
