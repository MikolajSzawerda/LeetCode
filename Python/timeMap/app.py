from typing import *

class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        l = self.store.get(key, [])
        l.append((timestamp, value))
        self.store[key]=l

    # 10 20 
    def get(self, key, timestamp):
        kl = self.store.get(key, [])
        l, r = 0, len(kl)-1
        res = ""
        while l<=r:
            p = (l+r)//2
            if kl[p][0] > timestamp:
                r = p-1
            else:
                res = kl[p][1]
                l = p+1
        return res
