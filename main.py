from http.client import HTTPResponse
from itertools import count
from fastapi import FastAPI, WebSocket
from typing import List
import __queue
from fastapi import HTTPException, status, Depends

app = FastAPI()

def numToStr(num: int) -> str:
    return format(num, "04") 

"""The program assumes that the max number of digits in the ticketing system is 4, and if the max digit(9999) is reached then counter
will reset to 0 automatically, unless the couter variable is manually reset using GET /clear"""

app_queue = None
counter: int
latestServingNo: str
counterServing: List[str]
counterStatus: List[bool]

@app.on_event("startup")
async def startup_event():
    """Ensure start with empty queue"""
    global app_queue, counter, latestServingNo, counterServing, counterStatus
    latestServingNo = ""
    app_queue = __queue.Queue()
    counter = 0
    counterServing = ["","","",""]
    counterStatus = [True, True, True, True]


@app.get("/ping")
def ping():
    return "pong"


@app.get("/clear")
def clear_queue():
    """This is just a basic clear operation, so I'll use get"""
    global app_queue, counter, latestServingNo, counterServing, counterStatus
    latestServingNo = ""
    app_queue = __queue.Queue()
    counter = 0
    counterServing = ["","","",""]
    counterStatus = [True, True, True, True]
    return "cleared"

@app.get("/newTicket")
def gen_ticket():
    global counter
    app_queue.enqueue(numToStr(counter))
    if (counter <= 9999):
        counter += 1
    else:
        counter = 0
    return f"Ticket {numToStr(counter - 1)} generated"
    

@app.post("/callNext")
def call_next(counterNo: int):
    global latestServingNo, counterServing, counterStatus
    if (not counterStatus[counterNo - 1]):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="cannot call next when counter is offline")
    elif (counterServing[counterNo - 1] != ""):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="cannot call next when still serving ticket")
    """dequeue the first in queue"""
    latestServingNo = app_queue.dequeue()
    """make counter who made this req busy then update with the number they are serving"""
    counterServing[counterNo - 1] = latestServingNo
    return f"Counter {counterNo} is now serving {counterServing[counterNo - 1]}"

@app.post("/compCurr")
def complete_current(counterNo: int):
    global counterServing, counterStatus
    if (not counterStatus[counterNo - 1]):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="invalid function call when counter is offline")
    counterServing[counterNo - 1] = ""
    return f"Counter {counterNo} is now free"

@app.post("/toggleOnline")
def toggle_online(counterNo: int):
    global counterStatus, counterServing
    if (counterServing[counterNo - 1] != "" and counterStatus[counterNo - 1]):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="cannot go offline when still serving ticket")
    counterStatus[counterNo - 1] = not counterStatus[counterNo - 1]
    return f"Counter # {counterNo} is now " + str(counterStatus[counterNo - 1])

@app.get("/queue")
def get_queue():
    return app_queue.getQueue()

@app.websocket("/ws/test")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    global app_queue, counter, latestServingNo, counterServing, counterStatus,app_queue
    await websocket.accept()
    while True:
        await websocket.receive_text()
        data = {
            "queue": app_queue.getQueue(),
            "latestServingNo":  latestServingNo,
            "lastIssuedNo": numToStr(counter - 1),
            "counter": counterServing,
            "counterStatus": counterStatus
        }
        await websocket.send_json(data)
        pass

