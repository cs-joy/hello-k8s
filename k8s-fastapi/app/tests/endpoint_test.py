import requests
import json

base_url = "http://localhost:8000"

create_item_url = f"{base_url}/items"

item_data = {
    "id": 1001,
    "name": "New Item",
    "price": 9.99
}

payload = json.dumps(item_data)

headers = {
    "Content-Type": "application/json"
}

res = requests.post(create_item_url, data=payload, headers=headers)

if res.status_code == 200:
    new_item = res.json()
    print("Item created successfully")
    print(new_item)
else:
    print("Error creation item. Status code:", res.status_code)
    print(f"Response content: {res.text}")