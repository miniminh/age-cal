from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from datetime import datetime
import uvicorn

app = FastAPI()

@app.get("/")
async def get():
    return FileResponse("templates/index.html")

def assign():
    now = datetime.now()
    dt_string = now.strftime("%d%m%Y%H%M%S")
    return dt_string
 


if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=14024, reload=True)