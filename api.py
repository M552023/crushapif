
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

history = []

@app.post("/add/{value}")
def add_round(value: float):
    history.append(value)
    return {"status": "ok", "count": len(history)}

@app.get("/predict")
def predict():
    if not history:
        return {"prediction": "no_data"}
    avg = sum(history[-10:]) / min(10, len(history))
    return {"prediction": round(avg * 0.92, 2)}

@app.post("/reset")
def reset_data():
    history.clear()
    return {"status": "reset"}

@app.get("/status")
def status():
    return {"status": "API Running"}
