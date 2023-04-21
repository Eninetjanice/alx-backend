#!/usr/bin/env python3
"""Simple pagination"""

from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Helper function.
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Get page function
        :Args: 2 parameters
            page (int, default value = 1)
            page_size (int, default = 10)
        :Return: List of requested dataset page
        """
        pass
        # Assert both args are int and > 0
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Calculate total num of pages
        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)

        # If input args are out of range for dataset return []:
        if page > total_pages:
            return []

        # With index_range find and return appropriate page of dataset
        start_index, end_index = index_range(page, page_size)
        return dataset[start_index:end_index]
