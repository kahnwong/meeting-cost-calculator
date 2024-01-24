from pydantic import BaseModel


class MeetingInfo(BaseModel):
    attendees: int = 5
    meeting_duration_minutes: int = 30
    times_per_week: int = 1
    avg_salary: int = 100000
