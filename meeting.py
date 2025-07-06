class Meeting:
    def __init__(self, meeting_id: int, meeting_name: str, room_id: int, slot, participitants):
        self.meeting_id = meeting_id
        self.meeting_name = meeting_name
        self.meeting_room = room_id
        self.time_slot = slot
        self.participitants = participitants
    
    def add_participitant(self, p):
        self.participitants.add(p)

    def remove_participitant(self, p):
        self.participitants.remove(p)

    def notify_participitants(self):
        for p in self.participitants:
            p.update(self, self.time_slot)


    