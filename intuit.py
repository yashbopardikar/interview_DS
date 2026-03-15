from collections import deque

class Solution:
    def __init__(self):
        self.standard_que = deque()
        self.vip_que = deque()
        self.std_time = 5
        self.vip_count = 0

    def checkIn(self, id: str, isVip: bool):
        if isVip:
            que_len = len(self.vip_que)
            cal_time = que_len * self.std_time
            self.vip_que.append(id)
            #print("Wait time VIP" , id, cal_time)
            return cal_time
        else:
            que_len = len(self.standard_que) +  len(self.vip_que)
            cal_time = que_len * self.std_time
            self.standard_que.append(id)
            #print("Wait time Regular" , id, cal_time)
            return cal_time

    def getNextCustomer(self):
        if not self.vip_que and not self.standard_que:
            return None
        if (self.vip_que and self.vip_count < 2) or not self.standard_que:
            self.vip_count +=1
            return (self.vip_que.popleft(), "VIP")
        else:
            self.vip_count = 0
            return (self.standard_que.popleft(), "Regular")



sol = Solution()
# sol.checkIn("1", True)
# sol.checkIn("2", True)
# sol.checkIn("3", True)
# sol.checkIn("4", True)
# sol.checkIn("5", True)
# sol.checkIn("6", True)
# sol.checkIn("7", False)
# sol.checkIn("8", False)
# sol.checkIn("9", False)
# sol.checkIn("10", False)
# sol.checkIn("11", True)

for i in range(6):
    print(sol.getNextCustomer())



