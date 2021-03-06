# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SubJob(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, sub_job_type: str=None, parameters: str=None):  # noqa: E501
        """SubJob - a model defined in Swagger

        :param sub_job_type: The sub_job_type of this SubJob.  # noqa: E501
        :type sub_job_type: str
        :param parameters: The parameters of this SubJob.  # noqa: E501
        :type parameters: str
        """
        self.swagger_types = {
            'sub_job_type': str,
            'parameters': str
        }

        self.attribute_map = {
            'sub_job_type': 'subJobType',
            'parameters': 'parameters'
        }
        self._sub_job_type = sub_job_type
        self._parameters = parameters

    @classmethod
    def from_dict(cls, dikt) -> 'SubJob':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubJob of this SubJob.  # noqa: E501
        :rtype: SubJob
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sub_job_type(self) -> str:
        """Gets the sub_job_type of this SubJob.

        Sub Job Type  # noqa: E501

        :return: The sub_job_type of this SubJob.
        :rtype: str
        """
        return self._sub_job_type

    @sub_job_type.setter
    def sub_job_type(self, sub_job_type: str):
        """Sets the sub_job_type of this SubJob.

        Sub Job Type  # noqa: E501

        :param sub_job_type: The sub_job_type of this SubJob.
        :type sub_job_type: str
        """
        allowed_values = ["hpc", "archive", "unarchive", "copy", "compile"]  # noqa: E501
        if sub_job_type not in allowed_values:
            raise ValueError(
                "Invalid value for `sub_job_type` ({0}), must be one of {1}"
                .format(sub_job_type, allowed_values)
            )

        self._sub_job_type = sub_job_type

    @property
    def parameters(self) -> str:
        """Gets the parameters of this SubJob.

        Job parameters  # noqa: E501

        :return: The parameters of this SubJob.
        :rtype: str
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters: str):
        """Sets the parameters of this SubJob.

        Job parameters  # noqa: E501

        :param parameters: The parameters of this SubJob.
        :type parameters: str
        """
        if parameters is None:
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters
