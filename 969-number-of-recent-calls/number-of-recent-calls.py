from collections import deque
class RecentCounter:

    def __init__(self):
        self.t=deque()

    def ping(self, t: int) -> int:
        self.t.append(t)
        while self.t and self.t[0]<t-3000:
            self.t.popleft()

        return len(self.t)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)