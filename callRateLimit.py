import time

from rateLimit import TokenRequest, RateLimiter

if __name__ == "__main__":
    # Allow max 5 requests per 10 seconds per token
    limiter = RateLimiter(window_size=10, max_requests=5)

    token = "client_123"
    req = TokenRequest(token)

    for i in range(10):
        allowed = limiter.allow(req)
        print(f"Request {i+1}: {'ALLOWED' if allowed else 'DENIED'}")
        time.sleep(1)