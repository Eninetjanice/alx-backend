#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns dict with key-value pairs:
            index, next_index, page_size, data.
        Behaviour:
            Use assert to verify that index is in a valid range.
            If user queries index 0, page_size 10, output = index 0-9 included.
            If next index (10) wit page_size 10 is requested, but rows 3, 6 & 7
            were deleted, user shld still receive rows indexed 10-19 included.
        """
        assert isinstance(index, int) and index >= 0
        assert index < len(self.dataset())
        assert isinstance(page_size, int) and page_size > 0

        indexed_dataset = self.indexed_dataset()
        max_index = len(indexed_dataset) - 1

        if index > max_index:
            return {
                'index': max_index + 1,
                'next_index': None,
                'page_size': page_size,
                'data': []
            }

        current_index = index
        data = []
        while len(data) < page_size and current_index <= max_index:
            if current_index not in indexed_dataset:
                current_index += 1
                continue
            data.append(indexed_dataset[current_index])
            current_index += 1

        next_index = current_index if current_index <= max_index else None

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
