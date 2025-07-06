class PCalendar:
    def __init__(self):
        self.time_slots = []

    def add_slot(self, slot):
        self.time_slots.append(slot)
    
    def is_available(self, slot):
        is_possible = True
        for tslot in self.time_slots:
            if tslot.is_overlapping(slot):
                is_possible = False
        return is_possible