class MeetingRoomController:
    def __init__(self):
        self.meeting_rooms = []


    def add_rooms(self, room):
        self.meeting_rooms.append(room)


    def get_available_rooms(self, slot):
        available_rooms = []
        for room in self.meeting_rooms:
            if room.is_booking_possible(slot):
                available_rooms.append(room)

        return available_rooms
    




    