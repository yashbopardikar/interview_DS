from collections import deque

class AppleStore:
    def __init__(self):
        self.vip_que = deque()
        self.standard_que = deque()
        self.count = 0

    def checkin(self, name: str, vip_status: bool):
        if vip_status:
            self.vip_que.append(name)
        else:
            self.standard_que.append(name)

    def processing(self):
        if (self.vip_que and self.count < 2) or (self.vip_que and not self.standard_que) :
            self.count +=1
            return self.vip_que.popleft()
        elif self.standard_que:
            self.count = 0
            return self.standard_que.popleft()
        else:
            return None


sol = AppleStore()
sol.checkin("Yash", True)
sol.checkin("kal", True)
sol.checkin("vihaan", True)
sol.checkin("Aai", True)
sol.checkin("Baba", True)
sol.checkin("Deep", True)
print(sol.processing())
print(sol.processing())
print(sol.processing())
print(sol.processing())
print(sol.processing())
print(sol.processing())




