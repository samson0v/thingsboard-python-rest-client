# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.5.0PE
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FeaturesInfo(object):
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
        'email_enabled': 'bool',
        'notification_enabled': 'bool',
        'oauth_enabled': 'bool',
        'sms_enabled': 'bool',
        'two_fa_enabled': 'bool',
        'white_labeling_enabled': 'bool'
    }

    attribute_map = {
        'email_enabled': 'emailEnabled',
        'notification_enabled': 'notificationEnabled',
        'oauth_enabled': 'oauthEnabled',
        'sms_enabled': 'smsEnabled',
        'two_fa_enabled': 'twoFaEnabled',
        'white_labeling_enabled': 'whiteLabelingEnabled'
    }

    def __init__(self, email_enabled=None, notification_enabled=None, oauth_enabled=None, sms_enabled=None, two_fa_enabled=None, white_labeling_enabled=None):  # noqa: E501
        """FeaturesInfo - a model defined in Swagger"""  # noqa: E501
        self._email_enabled = None
        self._notification_enabled = None
        self._oauth_enabled = None
        self._sms_enabled = None
        self._two_fa_enabled = None
        self._white_labeling_enabled = None
        self.discriminator = None
        if email_enabled is not None:
            self.email_enabled = email_enabled
        if notification_enabled is not None:
            self.notification_enabled = notification_enabled
        if oauth_enabled is not None:
            self.oauth_enabled = oauth_enabled
        if sms_enabled is not None:
            self.sms_enabled = sms_enabled
        if two_fa_enabled is not None:
            self.two_fa_enabled = two_fa_enabled
        if white_labeling_enabled is not None:
            self.white_labeling_enabled = white_labeling_enabled

    @property
    def email_enabled(self):
        """Gets the email_enabled of this FeaturesInfo.  # noqa: E501


        :return: The email_enabled of this FeaturesInfo.  # noqa: E501
        :rtype: bool
        """
        return self._email_enabled

    @email_enabled.setter
    def email_enabled(self, email_enabled):
        """Sets the email_enabled of this FeaturesInfo.


        :param email_enabled: The email_enabled of this FeaturesInfo.  # noqa: E501
        :type: bool
        """

        self._email_enabled = email_enabled

    @property
    def notification_enabled(self):
        """Gets the notification_enabled of this FeaturesInfo.  # noqa: E501


        :return: The notification_enabled of this FeaturesInfo.  # noqa: E501
        :rtype: bool
        """
        return self._notification_enabled

    @notification_enabled.setter
    def notification_enabled(self, notification_enabled):
        """Sets the notification_enabled of this FeaturesInfo.


        :param notification_enabled: The notification_enabled of this FeaturesInfo.  # noqa: E501
        :type: bool
        """

        self._notification_enabled = notification_enabled

    @property
    def oauth_enabled(self):
        """Gets the oauth_enabled of this FeaturesInfo.  # noqa: E501


        :return: The oauth_enabled of this FeaturesInfo.  # noqa: E501
        :rtype: bool
        """
        return self._oauth_enabled

    @oauth_enabled.setter
    def oauth_enabled(self, oauth_enabled):
        """Sets the oauth_enabled of this FeaturesInfo.


        :param oauth_enabled: The oauth_enabled of this FeaturesInfo.  # noqa: E501
        :type: bool
        """

        self._oauth_enabled = oauth_enabled

    @property
    def sms_enabled(self):
        """Gets the sms_enabled of this FeaturesInfo.  # noqa: E501


        :return: The sms_enabled of this FeaturesInfo.  # noqa: E501
        :rtype: bool
        """
        return self._sms_enabled

    @sms_enabled.setter
    def sms_enabled(self, sms_enabled):
        """Sets the sms_enabled of this FeaturesInfo.


        :param sms_enabled: The sms_enabled of this FeaturesInfo.  # noqa: E501
        :type: bool
        """

        self._sms_enabled = sms_enabled

    @property
    def two_fa_enabled(self):
        """Gets the two_fa_enabled of this FeaturesInfo.  # noqa: E501


        :return: The two_fa_enabled of this FeaturesInfo.  # noqa: E501
        :rtype: bool
        """
        return self._two_fa_enabled

    @two_fa_enabled.setter
    def two_fa_enabled(self, two_fa_enabled):
        """Sets the two_fa_enabled of this FeaturesInfo.


        :param two_fa_enabled: The two_fa_enabled of this FeaturesInfo.  # noqa: E501
        :type: bool
        """

        self._two_fa_enabled = two_fa_enabled

    @property
    def white_labeling_enabled(self):
        """Gets the white_labeling_enabled of this FeaturesInfo.  # noqa: E501


        :return: The white_labeling_enabled of this FeaturesInfo.  # noqa: E501
        :rtype: bool
        """
        return self._white_labeling_enabled

    @white_labeling_enabled.setter
    def white_labeling_enabled(self, white_labeling_enabled):
        """Sets the white_labeling_enabled of this FeaturesInfo.


        :param white_labeling_enabled: The white_labeling_enabled of this FeaturesInfo.  # noqa: E501
        :type: bool
        """

        self._white_labeling_enabled = white_labeling_enabled

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
        if issubclass(FeaturesInfo, dict):
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
        if not isinstance(other, FeaturesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other