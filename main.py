from fastapi import FastAPI, Depends
from models import SleepSession, RealtimeData, SleepSettings, SleepAdvice
from storage import sessions, latest_realtime, settings, advice
from security import verify_iot_key

app = FastAPI(title="Sleepy Pillow Cloud API")

@app.get("/")
def home():
    return {"status": "Sleepy Pillow API online"}

# 🔽 IOT → CLOUD
@app.post("/ingest/all")
def ingest_all(data: dict, _: str = Depends(verify_iot_key)):
    # Stocker les sessions
    for s in data.get("sessions", []):
        sessions.append(SleepSession(**s))

    # Stocker le realtime
    global latest_realtime
    if "realtime" in data:
        latest_realtime = RealtimeData(**data["realtime"])

    # Stocker les settings
    global settings
    if "settings" in data:
        settings = SleepSettings(**data["settings"])

    # Stocker les conseils
    for a in data.get("advice", []):
        advice.append(SleepAdvice(**a))

    return {"message": "all data stored"}

# 🔼 CLOUD → APP
@app.get("/sessions")
def get_sessions():
    return sessions

@app.get("/realtime")
def get_realtime():
    return latest_realtime

@app.get("/settings")
def get_settings():
    return settings

@app.get("/advice")
def get_advice():
    return advice

@app.get("/all")
def get_all_data():
    return {
        "sessions": sessions,
        "realtime": latest_realtime,
        "settings": settings,
        "advice": advice
    }


