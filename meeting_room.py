from pcalendar import PCalendar

class MeetingRoom:
    def __init__(self, room_id):
        self.room_id = room_id
        self.calendar = PCalendar()
        self.meeting = None

    def is_booking_possible(self, slot):
        if self.calendar.is_available(slot):
            return True
        return False
    
    def book(self, slot):
        self.calendar.add_slot(slot)



    
