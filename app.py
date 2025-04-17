from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "hi its my first fastapi app"}

@app.get("/items")
async def read_items():
    return {"items": ["item1", "item2", "item3"]}
