import os
import json
from schemes import Item
from fastapi import FastAPI

file_path = os.path.join(os.path.dirname(__file__), 'mock_db/items.json')
app = FastAPI()

with open(file_path, 'r') as f:
    items = json.load(f)

@app.get("/")
def read_root():
    return {
        "Hello": "Form My Kubernetes App"
    }

@app.get("/items/")
async def get_itmes():
    return json.dumps(items)

@app.post("/items/")
def create_item(item: Item):
    if item.id is None or item.id in [existing_item['id'] for existing_item in items]:
        item_id = max([p['id'] for p in items]) + 1
    else:
        item_id = item.id
    
    new_item = {
        "id": item_id,
        "name": item.name,
        "price": item.price
    }
    items.append(new_item)
    with open('mock_db/items.json', 'w') as f:
        json.dump(items, f)
    return new_item

@app.get("/items/{item_id}")
async def get_item_by_id(item_id: int):
    item = [i for i in items if i['id' == item_id]]
    return item[0] if len(item) > 0 else {}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    for i, db_item in enumerate(items):
        if db_item["id"] == item.id:
            items[i] = item.model_dump()
            with open('mock_db/items.json', 'w') as f:
                json.dump(items, f)
            return {
                "message": "Item updated successfully!"
            }
        
@app.delete("/items/{item_id}/")
async def remove_item(item_id: int):
    for i, item in enumerate(items):
        if item["id"] == item.id:
            items.pop(i)
            with open("mock_db/items.json", 'w') as f:
                json.dump(items, f)
            
            return {
                "message": "Item remvoed successfully"
            }
        return {

            "message": "Item not found!"
        }