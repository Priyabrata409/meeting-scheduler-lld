from abc import ABC, abstractmethod


class RoomSelectionStrategy(ABC):
    @abstractmethod
    def get_available_room(self):
        pass


class FirstComeFirstServeStrategy(RoomSelectionStrategy):
    def get_available_room(self, available_rooms):
        return available_rooms[0]
    

    
        