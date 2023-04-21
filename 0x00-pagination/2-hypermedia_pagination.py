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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Hypermedia Pagination
        :Args:
            page (int, optional): The page number to return. Defaults to 1.
            page_size (int, optional): Number of rows per page. Defaults to 10.
        :Returns:
            dict: Dictionary containing hypermedia information for the dataset
            (page_size, page, data, next_page, prev_page, total_page)
        Raises:
            AssertionError: If page or page_size are not positive integers
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        """data = self.get_page(page, page_size)

        # Calculate total num of pages
        total_pages = math.ceil(len(self.dataset()) / page_size)
"""
        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)

        if start_index >= len(dataset):
            return {"page_size": page_size, "page": page, "data": [],
                    "next_page": None, "prev_page": None, "total_pages": 0}

        data = dataset[start_index:end_index]
        total_pages = math.ceil(len(dataset) / page_size)

        if page == 1:
            prev_page = None
        else:
            prev_page = page - 1

        if page == total_pages:
            next_page = None
        else:
            next_page = page + 1

        result = {
            "page_size": page_size,
            "page": page,
            "data": data,
            "total_pages": total_pages,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
        return result
