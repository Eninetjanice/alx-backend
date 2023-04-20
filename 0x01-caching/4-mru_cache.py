#!/usr/bin/env python3
""" MRUCache class that inherits from BaseCaching and is a caching system """

from base_caching import BaseCaching
from collections import deque


class MRUCache(BaseCaching):
    """ Most Recently Used caching system """

    def __init__(self):
        """ Initialize MFUCache """
        super().__init__()
        self.load = deque()

    def put(self, key, item):
        """ Add & / del item in the cache """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.load.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.load.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")
        self.load.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        else:
            self.load.remove(key)
            self.load.append(key)
            return self.cache_data[key]
