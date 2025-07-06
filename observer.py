from abc import ABC, abstractmethod
from time_slot import TimeSlot

class Observer(ABC):
    @abstractmethod
    def update(self):
        pass


class Participitant(Observer):
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def update(self, meeting, time_slot: TimeSlot):
        print(f"Hey {self.name}: Meeting {meeting.meeting_name} has been scheduled from {time_slot.start_time} to  {time_slot.end_time} in room {meeting.meeting_room}")

