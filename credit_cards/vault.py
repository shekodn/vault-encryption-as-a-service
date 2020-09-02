import requests
import base64

from django.conf import settings
import json

_headers = {
    "X-Vault-Token": settings.VAULT_TOKEN,
    "Content-Type": "application/json",
}


def get_ciphertext(message) -> str:

    message_bytes = message.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode("ascii")

    data = {"plaintext": base64_message}
    json_object = json.dumps(data, indent=4)

    response = requests.post(
        f"{settings.VAULT_ADDR}/v1/transit/encrypt/{settings.VAULT_KEY_NAME}",
        headers=_headers,
        data=json_object,
    )

    return response.json()["data"]["ciphertext"]
