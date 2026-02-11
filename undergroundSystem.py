class underground():
    def __init__(self):
        self.check_in_map = {}
        self.avg_time = {}

    def checkIn (self, id: int, startStation: str, t: int) -> None:
        self.check_in_map[id] = (startStation, t)

    def checkOut(self, id:int, stationName:str, t:int) -> None:
        startStation, startTime = self.check_in_map.pop(id)
        total_time = t - startTime
        route = (startStation, stationName)
        if route not in self.avg_time:
            self.avg_time[route] = [0,0]
        self.avg_time[route][0] += total_time
        self.avg_time[route][0] += 1

    def getAverageTime(self, startStation: str, endStation:str) -> None:
        total, count = self.avg_time[(startStation, endStation)]
        return total/count




if __name__ == "__main__":
    ug = underground()
    ug.checkIn(1,"staA", 1)
    print(ug.check_in_map)
    