from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/items")
async def read_items():
    return {"items": ["item1", "item2", "item3"]}
