from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def home_page():
    return {"massege":"wolcome hero"}


@app.get("/items")
def get_items():
    return {"massege":"you are fucking the best"}

if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)