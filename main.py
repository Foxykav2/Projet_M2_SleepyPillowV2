from fastapi import FastAPI, Depends
from models import SleepSession, RealtimeData
from storage import sessions, latest_realtime
from security import verify_iot_key

app = FastAPI(title="Sleepy Pillow Cloud API")


@app.get("/")
def home():
    return {"status": "Sleepy Pillow API online"}


# 🔽 IOT → CLOUD
@app.post("/ingest/session")
def ingest_session(
    session: SleepSession,
    _: str = Depends(verify_iot_key)
):
    sessions.append(session)
    return {"message": "session stored"}


@app.post("/ingest/realtime")
def ingest_realtime(
    data: RealtimeData,
    _: str = Depends(verify_iot_key)
):
    global latest_realtime
    latest_realtime = data
    return {"message": "realtime updated"}


# 🔼 CLOUD → APP
@app.get("/sessions")
def get_sessions():
    return sessions


@app.get("/realtime")
def get_realtime():
    return latest_realtime

