import bisect

class logstorage:
    def __init__(self):
        self.storage = []
        self.sorted_storage = []
        self.is_sorted = True
        self.time_dict = {
            "Year": 1,
            "Month": 2,
            "Day": 3,
            "Hour": 4,
            "Minute": 5,
            "Second": 6
        }

    def put(self, id, timestamp):
        self.storage.append((timestamp, id))
        self.is_sorted = False

    def retrive(self, start, end, granularity):
        idx = self.time_dict[granularity]
        st_sp = start.split(":")
        et_sp = end.split(":")
        st = st_sp[:idx]
        et = et_sp[:idx]
        print(idx, et_sp)
        s_time = ":".join(st + ["00"] * (6 - idx))
        e_time = ":".join(et + ["99"] * (6 - idx))

        print(s_time)
        if not self.is_sorted:
            self.sorted_storage = sorted(self.storage)
            self.is_sorted = True
        print(self.sorted_storage)
        left = bisect.bisect_left(self.sorted_storage,(s_time, -1))
        right = bisect.bisect_right(self.sorted_storage,(e_time, float('inf')))
        resp = []
        for i in range(left, right):
            resp.append(self.sorted_storage[i][1])
        return resp


if __name__ == "__main__":

    obj = logstorage()
    obj.put(1, "2017:01:01:23:59:59")
    obj.put(2, "2017:01:01:22:59:59")
    obj.put(3, "2016:01:01:00:00:00")
    print(obj.retrive("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"))
    param2 = obj.retrive("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour")
    print(param2)

