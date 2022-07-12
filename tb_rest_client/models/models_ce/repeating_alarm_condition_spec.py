# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.4.0-SNAPSHOT
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from .alarm_condition_spec import AlarmConditionSpec  # noqa: F401,E501

class RepeatingAlarmConditionSpec(AlarmConditionSpec):
    """

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
        'predicate': 'FilterPredicateValueint'
    }
    if hasattr(AlarmConditionSpec, "swagger_types"):
        swagger_types.update(AlarmConditionSpec.swagger_types)

    attribute_map = {
        'predicate': 'predicate'
    }
    if hasattr(AlarmConditionSpec, "attribute_map"):
        attribute_map.update(AlarmConditionSpec.attribute_map)

    def __init__(self, predicate=None, *args, **kwargs):  # noqa: E501
        """RepeatingAlarmConditionSpec - a model defined in Swagger"""  # noqa: E501
        self._predicate = None
        self.discriminator = None
        if predicate is not None:
            self.predicate = predicate
        AlarmConditionSpec.__init__(self, *args, **kwargs)

    @property
    def predicate(self):
        """Gets the predicate of this RepeatingAlarmConditionSpec.  # noqa: E501


        :return: The predicate of this RepeatingAlarmConditionSpec.  # noqa: E501
        :rtype: FilterPredicateValueint
        """
        return self._predicate

    @predicate.setter
    def predicate(self, predicate):
        """Sets the predicate of this RepeatingAlarmConditionSpec.


        :param predicate: The predicate of this RepeatingAlarmConditionSpec.  # noqa: E501
        :type: FilterPredicateValueint
        """

        self._predicate = predicate

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
        if issubclass(RepeatingAlarmConditionSpec, dict):
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
        if not isinstance(other, RepeatingAlarmConditionSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
