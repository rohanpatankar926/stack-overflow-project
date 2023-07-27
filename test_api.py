from fastapi import FastAPI,Response
from fastapi.responses import HTMLResponse
import uvicorn

app=FastAPI()

@app.get("/hello_world")
def helloworld():
    return HTMLResponse("<p>hello world</p>")


uvicorn.run(app=app)