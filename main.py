from typing import Union
import json
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

f = open('database.json')
data = json.load(f)
@app.get("/")
def get_articles(skip: int = 0, limit: int = 1 , order : str ="Des"):
    if(order == "Aes"):
        
        sorted_data = sorted(data["articles"], key=lambda x: x['pubDate'],reverse=True)
    else:
        sorted_data = data["articles"]
    return {"Articles": sorted_data[skip:limit]}


@app.get("/{item_id}")
def get_specificArticle(item_id: int):
    if item_id != 0:
        return {"Articles": data["articles"][item_id -1]  }
    else:
        return {"Articles": "No article found"  }
    
@app.get("/subscibe")
def save_email(email: str):
    if email != None:
        return {"Saved Successfull" }
    else:
        return {"Not valid Email" }