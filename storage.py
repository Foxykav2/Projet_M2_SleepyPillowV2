from typing import List
from models import SleepSession, RealtimeData

sessions: List[SleepSession] = []
latest_realtime: RealtimeData | None = None

