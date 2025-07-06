class TimeSlot:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def is_overlapping(self, slot):
        if self.end_time <= slot.start_time or self.start_time >= slot.end_time:
            return False
        return True
    

    