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

class VersionLoadConfig(object):
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
        'load_relations': 'bool',
        'load_attributes': 'bool',
        'load_credentials': 'bool'
    }

    attribute_map = {
        'load_relations': 'loadRelations',
        'load_attributes': 'loadAttributes',
        'load_credentials': 'loadCredentials'
    }

    def __init__(self, load_relations=None, load_attributes=None, load_credentials=None):  # noqa: E501
        """VersionLoadConfig - a model defined in Swagger"""  # noqa: E501
        self._load_relations = None
        self._load_attributes = None
        self._load_credentials = None
        self.discriminator = None
        if load_relations is not None:
            self.load_relations = load_relations
        if load_attributes is not None:
            self.load_attributes = load_attributes
        if load_credentials is not None:
            self.load_credentials = load_credentials

    @property
    def load_relations(self):
        """Gets the load_relations of this VersionLoadConfig.  # noqa: E501


        :return: The load_relations of this VersionLoadConfig.  # noqa: E501
        :rtype: bool
        """
        return self._load_relations

    @load_relations.setter
    def load_relations(self, load_relations):
        """Sets the load_relations of this VersionLoadConfig.


        :param load_relations: The load_relations of this VersionLoadConfig.  # noqa: E501
        :type: bool
        """

        self._load_relations = load_relations

    @property
    def load_attributes(self):
        """Gets the load_attributes of this VersionLoadConfig.  # noqa: E501


        :return: The load_attributes of this VersionLoadConfig.  # noqa: E501
        :rtype: bool
        """
        return self._load_attributes

    @load_attributes.setter
    def load_attributes(self, load_attributes):
        """Sets the load_attributes of this VersionLoadConfig.


        :param load_attributes: The load_attributes of this VersionLoadConfig.  # noqa: E501
        :type: bool
        """

        self._load_attributes = load_attributes

    @property
    def load_credentials(self):
        """Gets the load_credentials of this VersionLoadConfig.  # noqa: E501


        :return: The load_credentials of this VersionLoadConfig.  # noqa: E501
        :rtype: bool
        """
        return self._load_credentials

    @load_credentials.setter
    def load_credentials(self, load_credentials):
        """Sets the load_credentials of this VersionLoadConfig.


        :param load_credentials: The load_credentials of this VersionLoadConfig.  # noqa: E501
        :type: bool
        """

        self._load_credentials = load_credentials

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
        if issubclass(VersionLoadConfig, dict):
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
        if not isinstance(other, VersionLoadConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
