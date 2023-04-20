#!/usr/bin/env python3
""" BasicCache that inherits from BaseCaching and is a caching system """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Child of BaseCaching, which is a caching system without limits"""


    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None or item is not None:
            self.cache_data[key] = item
        else:
            return


    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]