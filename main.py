from room_selection_strategy import FirstComeFirstServeStrategy
from meeting_room_controller import MeetingRoomController
from meeting_room import MeetingRoom
from meeting_scheduler import MeetingScheduler
from observer import Participitant
from time_slot import TimeSlot


def main():
    m1 = MeetingRoom(1)
    m2 = MeetingRoom(2)
    m3 = MeetingRoom(3)

    p1 = Participitant("Hari", "ahkdnid")
    p2 = Participitant("Naeed", "adbjbdd")

    meeting_room_controller = MeetingRoomController()
    meeting_room_controller.add_rooms(m1)
    meeting_room_controller.add_rooms(m2)
    meeting_room_controller.add_rooms(m3)

    

    room_selection_strategy = FirstComeFirstServeStrategy()
    meeting_scheduler = MeetingScheduler(meeting_room_controller, room_selection_strategy)
    participitants = [p1, p2]
    slot = TimeSlot(10, 12)
    meeting_scheduler.schedule_meeting("1ab2", "Aspiration",slot, participitants)
    slot = TimeSlot(9, 11)
    meeting_scheduler.schedule_meeting("1a374", "Retrospective",slot, participitants)

    slot = TimeSlot(9, 13)
    meeting_scheduler.schedule_meeting("1as74", "Townhall",slot, participitants)

    slot = TimeSlot(9, 14)
    meeting_scheduler.schedule_meeting("1ssf4", "FunFriday",slot, participitants)

main()  
