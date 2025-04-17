# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 4.0.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

#  Copyright 2025. ThingsBoard
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import pprint
import re  # noqa: F401

import six

class NotificationRequestStats(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'sent': 'dict(str, BulkImportResultAssetCreated)',
        'errors': 'dict(str, dict(str, str))',
        'total_errors': 'BulkImportResultAssetCreated',
        'error': 'str'
    }

    attribute_map = {
        'sent': 'sent',
        'errors': 'errors',
        'total_errors': 'totalErrors',
        'error': 'error'
    }

    def __init__(self, sent=None, errors=None, total_errors=None, error=None):  # noqa: E501
        """NotificationRequestStats - a model defined in Swagger"""  # noqa: E501
        self._sent = None
        self._errors = None
        self._total_errors = None
        self._error = None
        self.discriminator = None
        if sent is not None:
            self.sent = sent
        if errors is not None:
            self.errors = errors
        if total_errors is not None:
            self.total_errors = total_errors
        if error is not None:
            self.error = error

    @property
    def sent(self):
        """Gets the sent of this NotificationRequestStats.  # noqa: E501


        :return: The sent of this NotificationRequestStats.  # noqa: E501
        :rtype: dict(str, BulkImportResultAssetCreated)
        """
        return self._sent

    @sent.setter
    def sent(self, sent):
        """Sets the sent of this NotificationRequestStats.


        :param sent: The sent of this NotificationRequestStats.  # noqa: E501
        :type: dict(str, BulkImportResultAssetCreated)
        """

        self._sent = sent

    @property
    def errors(self):
        """Gets the errors of this NotificationRequestStats.  # noqa: E501


        :return: The errors of this NotificationRequestStats.  # noqa: E501
        :rtype: dict(str, dict(str, str))
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this NotificationRequestStats.


        :param errors: The errors of this NotificationRequestStats.  # noqa: E501
        :type: dict(str, dict(str, str))
        """

        self._errors = errors

    @property
    def total_errors(self):
        """Gets the total_errors of this NotificationRequestStats.  # noqa: E501


        :return: The total_errors of this NotificationRequestStats.  # noqa: E501
        :rtype: BulkImportResultAssetCreated
        """
        return self._total_errors

    @total_errors.setter
    def total_errors(self, total_errors):
        """Sets the total_errors of this NotificationRequestStats.


        :param total_errors: The total_errors of this NotificationRequestStats.  # noqa: E501
        :type: BulkImportResultAssetCreated
        """

        self._total_errors = total_errors

    @property
    def error(self):
        """Gets the error of this NotificationRequestStats.  # noqa: E501


        :return: The error of this NotificationRequestStats.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this NotificationRequestStats.


        :param error: The error of this NotificationRequestStats.  # noqa: E501
        :type: str
        """

        self._error = error

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(NotificationRequestStats, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NotificationRequestStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
