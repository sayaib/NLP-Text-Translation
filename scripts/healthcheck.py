import requests

response = requests.post(
    url='http://0.0.0.0:8002/translate',
    headers={'Content-Type': 'application/json'},
    json={
         'q': 'Hello ',
         'source': 'en',
         'target': 'en'
    },
    timeout=60
)
# if server unavailable then requests with raise exception and healthcheck will fail
