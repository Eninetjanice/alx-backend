#!/usr/bin/env python3
""" LIFOCache class that inherits from BaseCaching and is a caching system """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ A caching system that uses the LIFO algorithm """

    def __init__(self):
        """ Initialize LIFOCache """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add & / del item in the cache """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.keys:
                last_key = self.keys[-1]
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")
                self.keys.pop()
        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
