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


class SleepSettings(BaseModel):
    targetCycles: int
    targetBedTime: str
    targetWakeTime: str
    enableNotifications: bool
    enableSmartAlarm: bool
    theme: Literal["auto", "dark", "light"]
    fatigueThreshold: int
    connectedDevice: str


class SleepAdvice(BaseModel):
    id: str
    title: str
    description: str
    category: str
    priority: Literal["low", "medium", "high"]


class RealtimeData(BaseModel):
    isAsleep: bool
    currentPhase: str
    heartRate: int
    respirationRate: int
    movements: int
    elapsedTime: int
    estimatedCycles: int
