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
from tb_rest_client.models.models_ce.notification_target_config import NotificationTargetConfig  # noqa: F401,E501

class MicrosoftTeamsNotificationTargetConfig(NotificationTargetConfig):
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
        'webhook_url': 'str',
        'channel_name': 'str',
        'use_old_api': 'bool',
        'title': 'str',
        'id': 'object',
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str'
    }
    if hasattr(NotificationTargetConfig, "swagger_types"):
        swagger_types.update(NotificationTargetConfig.swagger_types)

    attribute_map = {
        'webhook_url': 'webhookUrl',
        'channel_name': 'channelName',
        'use_old_api': 'useOldApi',
        'title': 'title',
        'id': 'id',
        'email': 'email',
        'first_name': 'firstName',
        'last_name': 'lastName'
    }
    if hasattr(NotificationTargetConfig, "attribute_map"):
        attribute_map.update(NotificationTargetConfig.attribute_map)

    def __init__(self, webhook_url=None, channel_name=None, use_old_api=None, title=None, id=None, email=None, first_name=None, last_name=None, *args, **kwargs):  # noqa: E501
        """MicrosoftTeamsNotificationTargetConfig - a model defined in Swagger"""  # noqa: E501
        self._webhook_url = None
        self._channel_name = None
        self._use_old_api = None
        self._title = None
        self._id = None
        self._email = None
        self._first_name = None
        self._last_name = None
        self.discriminator = None
        self.webhook_url = webhook_url
        self.channel_name = channel_name
        if use_old_api is not None:
            self.use_old_api = use_old_api
        if title is not None:
            self.title = title
        if id is not None:
            self.id = id
        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        NotificationTargetConfig.__init__(self, *args, **kwargs)

    @property
    def webhook_url(self):
        """Gets the webhook_url of this MicrosoftTeamsNotificationTargetConfig.  # noqa: E501


        :return: The webhook_url of this MicrosoftTeamsNotificationTargetConfig.  # noqa: E501
        :rtype: str
        """
        return self._webhook_url

    @webhook_url.setter
    def webhook_url(self, webhook_url):
        """Sets the webhook_url of this MicrosoftTeamsNotificationTargetConfig.


        :param webhook_url: The webhook_url of this MicrosoftTeamsNotificationTargetConfig.  # noqa: E501
        :type: str
        """
        if webhook_url is None:
            raise ValueError("Invalid value for `webhook_url`, must not be `None`")  # noqa: E501

        self._webhook_url = webhook_url

    @property
    def channel_name(self):
        """Gets the channel_name of this MicrosoftTeamsNotificationTargetConfig.  # noqa: E501


        :return: The channel_name of this MicrosoftTeamsNotificationTargetConfig.  # noqa: E501
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name):
        """Sets the channel_name of this MicrosoftTeamsNotificationTargetConfig.


        :param channel_name: The channel_name of this MicrosoftTeamsNotificationTargetConfig.  # noqa: E501
        :type: str
        """
        if channel_name is None:
            raise ValueError("Invalid value for `channel_name`, must not be `None`")  # noqa: E501

        self._channel_name = channel_name

    @property
    def use_old_api(self):
        """Gets the use_old_api of this MicrosoftTeamsNotificationTargetConfig.  # noqa: E501


        :return: The use_old_api of this MicrosoftTeamsNotificationTargetConfig.  # noqa: E501
        :rtype: bool
        """
        return self._use_old_api

    @use_old_api.setter
    def use_old_api(self, use_old_api):
        """Sets the use_old_api of this MicrosoftTeamsNotificationTargetConfig.


        :param use_old_api: The use_old_api of this MicrosoftTeamsNotificationTargetConfig.  # noqa: E501
        :type: bool
        """

        self._use_old_api = use_old_api

    @property
    def title(self):
        """Gets the title of this MicrosoftTeamsNotificationTargetConfig.  # noqa: E501


        :return: The title of this MicrosoftTeamsNotificationTargetConfig.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this MicrosoftTeamsNotificationTargetConfig.


        :param title: The title of this MicrosoftTeamsNotificationTargetConfig.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def id(self):
        """Gets the id of this MicrosoftTeamsNotificationTargetConfig.  # noqa: E501


        :return: The id of this MicrosoftTeamsNotificationTargetConfig.  # noqa: E501
        :rtype: object
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MicrosoftTeamsNotificationTargetConfig.


        :param id: The id of this MicrosoftTeamsNotificationTargetConfig.  # noqa: E501
        :type: object
        """

        self._id = id

    @property
    def email(self):
        """Gets the email of this MicrosoftTeamsNotificationTargetConfig.  # noqa: E501


        :return: The email of this MicrosoftTeamsNotificationTargetConfig.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this MicrosoftTeamsNotificationTargetConfig.


        :param email: The email of this MicrosoftTeamsNotificationTargetConfig.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this MicrosoftTeamsNotificationTargetConfig.  # noqa: E501


        :return: The first_name of this MicrosoftTeamsNotificationTargetConfig.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this MicrosoftTeamsNotificationTargetConfig.


        :param first_name: The first_name of this MicrosoftTeamsNotificationTargetConfig.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this MicrosoftTeamsNotificationTargetConfig.  # noqa: E501


        :return: The last_name of this MicrosoftTeamsNotificationTargetConfig.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this MicrosoftTeamsNotificationTargetConfig.


        :param last_name: The last_name of this MicrosoftTeamsNotificationTargetConfig.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

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
        if issubclass(MicrosoftTeamsNotificationTargetConfig, dict):
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
        if not isinstance(other, MicrosoftTeamsNotificationTargetConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
