from typing import List
from models import SleepSession, SleepSettings, SleepAdvice, RealtimeData

sessions: List[SleepSession] = []
settings: SleepSettings | None = None
advice: List[SleepAdvice] = []
latest_realtime: RealtimeData | None = None



