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

class EntitiesLimitNotificationRuleTriggerConfig(NotificationRuleTriggerConfig):
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
        'entity_types': 'list[str]',
        'threshold': 'float'
    }
    if hasattr(NotificationRuleTriggerConfig, "swagger_types"):
        swagger_types.update(NotificationRuleTriggerConfig.swagger_types)

    attribute_map = {
        'entity_types': 'entityTypes',
        'threshold': 'threshold'
    }
    if hasattr(NotificationRuleTriggerConfig, "attribute_map"):
        attribute_map.update(NotificationRuleTriggerConfig.attribute_map)

    def __init__(self, entity_types=None, threshold=None, *args, **kwargs):  # noqa: E501
        """EntitiesLimitNotificationRuleTriggerConfig - a model defined in Swagger"""  # noqa: E501
        self._entity_types = None
        self._threshold = None
        self.discriminator = None
        if entity_types is not None:
            self.entity_types = entity_types
        if threshold is not None:
            self.threshold = threshold
        NotificationRuleTriggerConfig.__init__(self, *args, **kwargs)

    @property
    def entity_types(self):
        """Gets the entity_types of this EntitiesLimitNotificationRuleTriggerConfig.  # noqa: E501


        :return: The entity_types of this EntitiesLimitNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._entity_types

    @entity_types.setter
    def entity_types(self, entity_types):
        """Sets the entity_types of this EntitiesLimitNotificationRuleTriggerConfig.


        :param entity_types: The entity_types of this EntitiesLimitNotificationRuleTriggerConfig.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["TENANT", "CUSTOMER", "USER", "DASHBOARD", "ASSET", "DEVICE", "ALARM", "RULE_CHAIN", "RULE_NODE", "ENTITY_VIEW", "WIDGETS_BUNDLE", "WIDGET_TYPE", "TENANT_PROFILE", "DEVICE_PROFILE", "ASSET_PROFILE", "API_USAGE_STATE", "TB_RESOURCE", "OTA_PACKAGE", "EDGE", "RPC", "QUEUE", "NOTIFICATION_TARGET", "NOTIFICATION_TEMPLATE", "NOTIFICATION_REQUEST", "NOTIFICATION", "NOTIFICATION_RULE", "QUEUE_STATS", "OAUTH2_CLIENT", "DOMAIN", "MOBILE_APP"]  # noqa: E501
        if not set(entity_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `entity_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(entity_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._entity_types = entity_types

    @property
    def threshold(self):
        """Gets the threshold of this EntitiesLimitNotificationRuleTriggerConfig.  # noqa: E501


        :return: The threshold of this EntitiesLimitNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this EntitiesLimitNotificationRuleTriggerConfig.


        :param threshold: The threshold of this EntitiesLimitNotificationRuleTriggerConfig.  # noqa: E501
        :type: float
        """

        self._threshold = threshold

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
        if issubclass(EntitiesLimitNotificationRuleTriggerConfig, dict):
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
        if not isinstance(other, EntitiesLimitNotificationRuleTriggerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
