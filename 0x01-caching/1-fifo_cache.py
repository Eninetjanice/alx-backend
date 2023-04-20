#!/usr/bin/env python3
""" FIFOCache class that inherits from BaseCaching and is a caching system """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ A caching system that uses the FIFO algorithm """

    def __init__(self):
        """ Initialize FIFOCache """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        #  if len(self.cache_data) >= self.MAX_ITEMS:
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.keys:
                first_key = self.keys[0]
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")
                self.keys.pop(0)
        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
