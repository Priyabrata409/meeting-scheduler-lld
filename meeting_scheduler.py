from meeting_room_controller import MeetingRoomController
from room_selection_strategy import RoomSelectionStrategy
from meeting import Meeting

class MeetingScheduler:
    def __init__(self, meeting_controller: MeetingRoomController, room_selection_strategy: RoomSelectionStrategy):
        self.meeting_controller  = meeting_controller
        self.room_selection_strategy = room_selection_strategy

    def schedule_meeting(self, meeting_id, meeting_name, slot, participitants):
        available_rooms = self.meeting_controller.get_available_rooms(slot)
        if len(available_rooms) == 0:
            print("Sorry No room available at this time")
            return
        selected_room = self.room_selection_strategy.get_available_room(available_rooms)
        selected_room.book(slot)
        selected_room.meeting = Meeting(meeting_id, meeting_name, selected_room.room_id, slot, participitants)
        selected_room.meeting.notify_participitants()



    






    


    