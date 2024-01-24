from pydantic import BaseModel
from pydantic import computed_field


class MeetingInfo(BaseModel):
    attendees: int = 5
    meeting_duration_minutes: int = 30
    times_per_week: int = 1
    avg_salary: int = 100000

    @computed_field
    @property
    def avg_salary_per_hour(self) -> float:
        # one month has 174 work hours
        return self.avg_salary / 12 / 174

    @computed_field
    @property
    def meeting_duration_hours(self) -> float:
        return self.meeting_duration_minutes / 60

    @computed_field
    @property
    def cost_per_hour(self) -> float:
        return (
            self.attendees
            * self.meeting_duration_hours
            * self.times_per_week
            * self.avg_salary_per_hour
        )

    @computed_field
    @property
    def cost_per_minute(self) -> float:
        return self.cost_per_hour / self.meeting_duration_minutes

    @computed_field
    @property
    def cost_per_year(self) -> float:
        return self.cost_per_hour * 52
