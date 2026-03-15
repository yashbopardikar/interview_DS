class LogSystem:

    def __init__(self):
        self.logs = []  # store (timestamp, id)

        # mapping granularity to index up to which to compare
        self.g = {
            "Year": 4,
            "Month": 7,
            "Day": 10,
            "Hour": 13,
            "Minute": 16,
            "Second": 19
        }

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((timestamp, id))

    def retrieve(self, start: str, end: str, granularity: str):
        res = []
        idx = self.g[granularity]

        start_cut = start[:idx]
        end_cut = end[:idx]
        print(start_cut, end_cut)

        for ts, log_id in self.logs:
            ts_cut = ts[:idx]
            print("compare with ts_cut :", ts_cut)
            if start_cut <= ts_cut <= end_cut:
                res.append(log_id)

        return res


if __name__ == "__main__":

    obj = LogSystem()
    obj.put(1, "2017:01:01:23:59:59")
    obj.put(2, "2017:01:01:22:59:59")
    obj.put(3, "2016:01:01:00:00:00")
    print(obj.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"))
    param2 = obj.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour")
    print(param2)