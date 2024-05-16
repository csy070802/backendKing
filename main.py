from typing import Union
from fastapi import FastAPI

app = FastAPI()


f = open("count.txt", 'r')
line = f.read()


count = int(line)


f.close() 

# f = open("count.txt", 'w')
# f.write("hi")
# f.close

@app.get("/plus")
def counter():
    global count
    count = count + 1
    f = open("count.txt", 'w')
    f.write(str(count))
    f.close
    
    
    return "1 증가" 


@app.get("/lookup")
def look():
    global count 
    return count




@app.get("/mul/{item1}/{item2}")
def mul(item1:int, item2:int):
    return {item1*item2}

@app.get("/add/{item1}/{item2}")
def add(item1: int, item2: int):
    return {"result": item1 + item2}

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}