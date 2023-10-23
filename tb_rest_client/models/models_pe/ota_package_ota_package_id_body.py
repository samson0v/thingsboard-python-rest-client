# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.6.0PE-SNAPSHOT
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

#  Copyright 2023. ThingsBoard
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

class OtaPackageOtaPackageIdBody(object):
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
        'checksum': 'str',
        'checksum_algorithm': 'str',
        'file': 'str'
    }

    attribute_map = {
        'checksum': 'checksum',
        'checksum_algorithm': 'checksumAlgorithm',
        'file': 'file'
    }

    def __init__(self, checksum=None, checksum_algorithm=None, file=None):  # noqa: E501
        """OtaPackageOtaPackageIdBody - a model defined in Swagger"""  # noqa: E501
        self._checksum = None
        self._checksum_algorithm = None
        self._file = None
        self.discriminator = None
        if checksum is not None:
            self.checksum = checksum
        self.checksum_algorithm = checksum_algorithm
        self.file = file

    @property
    def checksum(self):
        """Gets the checksum of this OtaPackageOtaPackageIdBody.  # noqa: E501

        OTA Package checksum. For example, '0xd87f7e0c'  # noqa: E501

        :return: The checksum of this OtaPackageOtaPackageIdBody.  # noqa: E501
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this OtaPackageOtaPackageIdBody.

        OTA Package checksum. For example, '0xd87f7e0c'  # noqa: E501

        :param checksum: The checksum of this OtaPackageOtaPackageIdBody.  # noqa: E501
        :type: str
        """

        self._checksum = checksum

    @property
    def checksum_algorithm(self):
        """Gets the checksum_algorithm of this OtaPackageOtaPackageIdBody.  # noqa: E501

        OTA Package checksum algorithm.  # noqa: E501

        :return: The checksum_algorithm of this OtaPackageOtaPackageIdBody.  # noqa: E501
        :rtype: str
        """
        return self._checksum_algorithm

    @checksum_algorithm.setter
    def checksum_algorithm(self, checksum_algorithm):
        """Sets the checksum_algorithm of this OtaPackageOtaPackageIdBody.

        OTA Package checksum algorithm.  # noqa: E501

        :param checksum_algorithm: The checksum_algorithm of this OtaPackageOtaPackageIdBody.  # noqa: E501
        :type: str
        """
        if checksum_algorithm is None:
            raise ValueError("Invalid value for `checksum_algorithm`, must not be `None`")  # noqa: E501

        self._checksum_algorithm = checksum_algorithm

    @property
    def file(self):
        """Gets the file of this OtaPackageOtaPackageIdBody.  # noqa: E501

        OTA Package data.  # noqa: E501

        :return: The file of this OtaPackageOtaPackageIdBody.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this OtaPackageOtaPackageIdBody.

        OTA Package data.  # noqa: E501

        :param file: The file of this OtaPackageOtaPackageIdBody.  # noqa: E501
        :type: str
        """
        if file is None:
            raise ValueError("Invalid value for `file`, must not be `None`")  # noqa: E501

        self._file = file

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
        if issubclass(OtaPackageOtaPackageIdBody, dict):
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
        if not isinstance(other, OtaPackageOtaPackageIdBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
