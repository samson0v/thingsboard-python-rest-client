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
from tb_rest_client.models.models_ce.notification_rule_trigger_config import NotificationRuleTriggerConfig  # noqa: F401,E501

class DeviceActivityNotificationRuleTriggerConfig(NotificationRuleTriggerConfig):
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
        'devices': 'list[str]',
        'device_profiles': 'list[str]',
        'notify_on': 'list[str]'
    }
    if hasattr(NotificationRuleTriggerConfig, "swagger_types"):
        swagger_types.update(NotificationRuleTriggerConfig.swagger_types)

    attribute_map = {
        'devices': 'devices',
        'device_profiles': 'deviceProfiles',
        'notify_on': 'notifyOn'
    }
    if hasattr(NotificationRuleTriggerConfig, "attribute_map"):
        attribute_map.update(NotificationRuleTriggerConfig.attribute_map)

    def __init__(self, devices=None, device_profiles=None, notify_on=None, *args, **kwargs):  # noqa: E501
        """DeviceActivityNotificationRuleTriggerConfig - a model defined in Swagger"""  # noqa: E501
        self._devices = None
        self._device_profiles = None
        self._notify_on = None
        self.discriminator = None
        if devices is not None:
            self.devices = devices
        if device_profiles is not None:
            self.device_profiles = device_profiles
        self.notify_on = notify_on
        NotificationRuleTriggerConfig.__init__(self, *args, **kwargs)

    @property
    def devices(self):
        """Gets the devices of this DeviceActivityNotificationRuleTriggerConfig.  # noqa: E501


        :return: The devices of this DeviceActivityNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this DeviceActivityNotificationRuleTriggerConfig.


        :param devices: The devices of this DeviceActivityNotificationRuleTriggerConfig.  # noqa: E501
        :type: list[str]
        """

        self._devices = devices

    @property
    def device_profiles(self):
        """Gets the device_profiles of this DeviceActivityNotificationRuleTriggerConfig.  # noqa: E501


        :return: The device_profiles of this DeviceActivityNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._device_profiles

    @device_profiles.setter
    def device_profiles(self, device_profiles):
        """Sets the device_profiles of this DeviceActivityNotificationRuleTriggerConfig.


        :param device_profiles: The device_profiles of this DeviceActivityNotificationRuleTriggerConfig.  # noqa: E501
        :type: list[str]
        """

        self._device_profiles = device_profiles

    @property
    def notify_on(self):
        """Gets the notify_on of this DeviceActivityNotificationRuleTriggerConfig.  # noqa: E501


        :return: The notify_on of this DeviceActivityNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._notify_on

    @notify_on.setter
    def notify_on(self, notify_on):
        """Sets the notify_on of this DeviceActivityNotificationRuleTriggerConfig.


        :param notify_on: The notify_on of this DeviceActivityNotificationRuleTriggerConfig.  # noqa: E501
        :type: list[str]
        """
        if notify_on is None:
            raise ValueError("Invalid value for `notify_on`, must not be `None`")  # noqa: E501
        allowed_values = ["ACTIVE", "INACTIVE"]  # noqa: E501
        if not set(notify_on).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `notify_on` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(notify_on) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._notify_on = notify_on

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
        if issubclass(DeviceActivityNotificationRuleTriggerConfig, dict):
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
        if not isinstance(other, DeviceActivityNotificationRuleTriggerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
