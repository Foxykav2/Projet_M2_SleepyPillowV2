from fastapi import FastAPI, Depends
from models import SleepSession, SleepSettings, SleepAdvice, RealtimeData
from storage import sessions, settings, advice, latest_realtime
from security import verify_iot_key

app = FastAPI(title="Sleepy Pillow Cloud API")

@app.get("/")
def home():
    return {"status": "Sleepy Pillow API online"}

# 🔽 IOT → CLOUD
@app.post("/ingest/session")
def ingest_session(session: SleepSession, _: str = Depends(verify_iot_key)):
    sessions.append(session)
    return {"message": "session stored"}

@app.post("/ingest/realtime")
def ingest_realtime(data: RealtimeData, _: str = Depends(verify_iot_key)):
    global latest_realtime
    latest_realtime = data
    return {"message": "realtime updated"}

@app.post("/ingest/settings")
def ingest_settings(new_settings: SleepSettings, _: str = Depends(verify_iot_key)):
    global settings
    settings = new_settings
    return {"message": "settings updated"}

@app.post("/ingest/advice")
def ingest_advice(new_advice: SleepAdvice, _: str = Depends(verify_iot_key)):
    advice.append(new_advice)
    return {"message": "advice stored"}

# 🔼 CLOUD → APP
@app.get("/data")
def get_all_data():
    return {
        "sessions": sessions,
        "realtime": latest_realtime,
        "settings": settings,
        "advice": advice
    }
