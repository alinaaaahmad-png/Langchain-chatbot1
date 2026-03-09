from fastapi import FastAPI

app = FastAPI()



# 1st api- Get API

@app.get


@app.get("/")
def read_root():
    return {"Hello": "World"}


