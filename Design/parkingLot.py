import math
from dataclasses import dataclass
from typing import List

@dataclass
class Ticket:
    ticket_id: str
    check_in: int
    floor_idx: int

class ParkingLot:
    def __init__(self, capacity: List[int]):
        self.floor_capacity = capacity
        self.ticket_store = {}
        self.hourly_rate = 10

    def parking(self, ticket_id:str, time:int):
        for i in range(len(self.floor_capacity)):
            if self.floor_capacity[i] > 0:
                ticket = Ticket(ticket_id, time, i)
                self.ticket_store[ticket_id] = ticket
                self.floor_capacity[i] -= 1
                return ticket
        print("parking lot full")
        return None

    def checkout(self, ticket_id:str, exit_time:int):
        if ticket_id not in self.ticket_store:
            raise KeyError("Invalid ticket Id")
        ticket = self.ticket_store[ticket_id]
        self.floor_capacity[ticket.floor_idx] += 1

        duration = exit_time - ticket.check_in
        cost = self.hourly_rate * math.ceil(duration)
        del self.ticket_store[ticket_id]
        return cost

    def get_floor_count(self,floor_number: int):
        if 0 <= floor_number < len(self.floor_capacity):
            return self.floor_capacity[floor_number]
        raise IndexError("Floor does not exist")



# sol = ParkingLot([2,2,2])
# sol.parking("aaa",1)
# sol.parking("bbb",2)
# sol.parking("ccc",3)
# sol.parking("ddd",4)
# sol.parking("eee",5)
#
# print(sol.get_floor_count(2))
# sol.parking("fff",6)
# sol.checkout("aaa",5)
# sol.parking("ggg",7)





