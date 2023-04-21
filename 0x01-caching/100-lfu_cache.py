#!/usr/bin/env python3
""" LFUCache class that inherits from BaseCaching and is a caching system """

from base_caching import BaseCaching
from collections import deque
from collections import defaultdict


class LFUCache(BaseCaching):
    """ Least Frequently Used caching system """

    def __init__(self):
        """ Initialize LFUCache """
        super().__init__()
        self.load = deque()
        self.freq = defaultdict(int)

    def put(self, key, item):
        """ Add & / del item in the cache """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.freq[key] += 1
            self.load.remove(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.freq.values())
                lfu_keys = [k for k, v in self.freq.items() if v == min_freq]
                for k in self.load:
                    if k in lfu_keys:
                        self.load.remove(k)
                        break
                for k in lfu_keys:
                    if k in self.cache_data:
                        del self.cache_data[k]
                        del self.freq[k]
                        print(f"DISCARD: {k}")
                        break
            self.freq[key] = 1
        self.load.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        self.freq[key] += 1
        self.load.remove(key)
        self.load.append(key)
        return self.cache_data[key]
