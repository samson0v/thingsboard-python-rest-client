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

class DeviceProfileProvisionConfiguration(object):
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
        'provision_device_secret': 'str',
        'type': 'str'
    }

    attribute_map = {
        'provision_device_secret': 'provisionDeviceSecret',
        'type': 'type'
    }

    discriminator_value_class_map = {
        'DisabledDeviceProfileProvisionConfiguration': 'DisabledDeviceProfileProvisionConfiguration',
        'AllowCreateNewDevicesDeviceProfileProvisionConfiguration': 'AllowCreateNewDevicesDeviceProfileProvisionConfiguration',  # noqa: E501
        'CheckPreProvisionedDevicesDeviceProfileProvisionConfiguration': 'CheckPreProvisionedDevicesDeviceProfileProvisionConfiguration',  # noqa: E501
        'X509CertificateChainProvisionConfiguration': 'X509CertificateChainProvisionConfiguration'}

    def __init__(self, provision_device_secret=None, type=None):  # noqa: E501
        """DeviceProfileProvisionConfiguration - a model defined in Swagger"""  # noqa: E501
        self._provision_device_secret = None
        self._type = None
        self.discriminator = 'type'
        if provision_device_secret is not None:
            self.provision_device_secret = provision_device_secret
        self.type = type

    @property
    def provision_device_secret(self):
        """Gets the provision_device_secret of this DeviceProfileProvisionConfiguration.  # noqa: E501


        :return: The provision_device_secret of this DeviceProfileProvisionConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._provision_device_secret

    @provision_device_secret.setter
    def provision_device_secret(self, provision_device_secret):
        """Sets the provision_device_secret of this DeviceProfileProvisionConfiguration.


        :param provision_device_secret: The provision_device_secret of this DeviceProfileProvisionConfiguration.  # noqa: E501
        :type: str
        """

        self._provision_device_secret = provision_device_secret

    @property
    def type(self):
        """Gets the type of this DeviceProfileProvisionConfiguration.  # noqa: E501


        :return: The type of this DeviceProfileProvisionConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeviceProfileProvisionConfiguration.


        :param type: The type of this DeviceProfileProvisionConfiguration.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(DeviceProfileProvisionConfiguration, dict):
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
        if not isinstance(other, DeviceProfileProvisionConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
