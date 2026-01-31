from pydantic import BaseModel
from typing import List, Literal


class SleepPhase(BaseModel):
    phase: Literal["awake", "light", "deep", "rem"]
    startTime: int
    duration: int


class SleepSession(BaseModel):
    id: str
    date: str
    bedTime: str
    wakeTime: str
    totalDuration: int
    sleepDuration: int
    phases: List[SleepPhase]
    movements: int
    heartRate: int
    respirationRate: int
    sleepQuality: int
    cycles: int
    energyLevel: int
    fatigueLevel: int


class RealtimeData(BaseModel):
    deviceId: str
    timestamp: int
    isAsleep: bool
    currentPhase: str
    heartRate: int
    respirationRate: int
    movements: int
    elapsedTime: int
    estimatedCycles: int
