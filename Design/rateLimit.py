import time
from collections import deque
from threading import Lock


class TokenRequest:
    def __init__(self,token: str):
        self.token = token

class SlidingWindowLog:
    def __init__(self, window_size: float, max_requests: int):
        self.window_size  = window_size
        self.max_requests = max_requests
        self.timestamps = deque()
        self.lock = Lock()

    def allow_request(self) -> bool:
        now = time.time()
        with self.lock:
            while self.timestamps and self.timestamps[0] <= now - self.window_size:
                self.timestamps.popleft()

            if len(self.timestamps) < self.max_requests:
                self.timestamps.append(now)
                return True
            return False

class RateLimiter:
    def __init__(self, window_size: float, max_requests: int):
        self.window_size = window_size
        self.max_requests = max_requests
        self.buckets = {}
        self.lock = Lock()

    def get_bucket(self, token: str) -> SlidingWindowLog:
        with self.lock:
            if token not in self.buckets:
                self.buckets[token] = SlidingWindowLog(self.window_size, self.max_requests)
            return self.buckets[token]

    def allow(self, request: TokenRequest) -> bool:
        bucket = self.get_bucket(request.token)
        return bucket.allow_request()



