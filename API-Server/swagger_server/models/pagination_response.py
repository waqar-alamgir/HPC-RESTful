# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.job import Job  # noqa: F401,E501
from swagger_server import util


class PaginationResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, total_pages: float=None, current_page: float=None, page_length: float=None, jobs: List[Job]=None):  # noqa: E501
        """PaginationResponse - a model defined in Swagger

        :param total_pages: The total_pages of this PaginationResponse.  # noqa: E501
        :type total_pages: float
        :param current_page: The current_page of this PaginationResponse.  # noqa: E501
        :type current_page: float
        :param page_length: The page_length of this PaginationResponse.  # noqa: E501
        :type page_length: float
        :param jobs: The jobs of this PaginationResponse.  # noqa: E501
        :type jobs: List[Job]
        """
        self.swagger_types = {
            'total_pages': float,
            'current_page': float,
            'page_length': float,
            'jobs': List[Job]
        }

        self.attribute_map = {
            'total_pages': 'totalPages',
            'current_page': 'currentPage',
            'page_length': 'pageLength',
            'jobs': 'jobs'
        }
        self._total_pages = total_pages
        self._current_page = current_page
        self._page_length = page_length
        self._jobs = jobs

    @classmethod
    def from_dict(cls, dikt) -> 'PaginationResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PaginationResponse of this PaginationResponse.  # noqa: E501
        :rtype: PaginationResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def total_pages(self) -> float:
        """Gets the total_pages of this PaginationResponse.


        :return: The total_pages of this PaginationResponse.
        :rtype: float
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages: float):
        """Sets the total_pages of this PaginationResponse.


        :param total_pages: The total_pages of this PaginationResponse.
        :type total_pages: float
        """

        self._total_pages = total_pages

    @property
    def current_page(self) -> float:
        """Gets the current_page of this PaginationResponse.


        :return: The current_page of this PaginationResponse.
        :rtype: float
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page: float):
        """Sets the current_page of this PaginationResponse.


        :param current_page: The current_page of this PaginationResponse.
        :type current_page: float
        """

        self._current_page = current_page

    @property
    def page_length(self) -> float:
        """Gets the page_length of this PaginationResponse.


        :return: The page_length of this PaginationResponse.
        :rtype: float
        """
        return self._page_length

    @page_length.setter
    def page_length(self, page_length: float):
        """Sets the page_length of this PaginationResponse.


        :param page_length: The page_length of this PaginationResponse.
        :type page_length: float
        """

        self._page_length = page_length

    @property
    def jobs(self) -> List[Job]:
        """Gets the jobs of this PaginationResponse.


        :return: The jobs of this PaginationResponse.
        :rtype: List[Job]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs: List[Job]):
        """Sets the jobs of this PaginationResponse.


        :param jobs: The jobs of this PaginationResponse.
        :type jobs: List[Job]
        """

        self._jobs = jobs
