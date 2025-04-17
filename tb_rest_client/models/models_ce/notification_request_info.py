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

class NotificationRequestInfo(object):
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
        'id': 'NotificationRequestId',
        'created_time': 'int',
        'tenant_id': 'TenantId',
        'targets': 'list[str]',
        'template_id': 'NotificationTemplateId',
        'template': 'NotificationTemplate',
        'info': 'NotificationInfo',
        'additional_config': 'NotificationRequestConfig',
        'originator_entity_id': 'EntityId',
        'rule_id': 'NotificationRuleId',
        'status': 'str',
        'stats': 'NotificationRequestStats',
        'template_name': 'str',
        'delivery_methods': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'tenant_id': 'tenantId',
        'targets': 'targets',
        'template_id': 'templateId',
        'template': 'template',
        'info': 'info',
        'additional_config': 'additionalConfig',
        'originator_entity_id': 'originatorEntityId',
        'rule_id': 'ruleId',
        'status': 'status',
        'stats': 'stats',
        'template_name': 'templateName',
        'delivery_methods': 'deliveryMethods'
    }

    def __init__(self, id=None, created_time=None, tenant_id=None, targets=None, template_id=None, template=None, info=None, additional_config=None, originator_entity_id=None, rule_id=None, status=None, stats=None, template_name=None, delivery_methods=None):  # noqa: E501
        """NotificationRequestInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._tenant_id = None
        self._targets = None
        self._template_id = None
        self._template = None
        self._info = None
        self._additional_config = None
        self._originator_entity_id = None
        self._rule_id = None
        self._status = None
        self._stats = None
        self._template_name = None
        self._delivery_methods = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        self.targets = targets
        if template_id is not None:
            self.template_id = template_id
        if template is not None:
            self.template = template
        if info is not None:
            self.info = info
        if additional_config is not None:
            self.additional_config = additional_config
        if originator_entity_id is not None:
            self.originator_entity_id = originator_entity_id
        if rule_id is not None:
            self.rule_id = rule_id
        if status is not None:
            self.status = status
        if stats is not None:
            self.stats = stats
        if template_name is not None:
            self.template_name = template_name
        if delivery_methods is not None:
            self.delivery_methods = delivery_methods

    @property
    def id(self):
        """Gets the id of this NotificationRequestInfo.  # noqa: E501


        :return: The id of this NotificationRequestInfo.  # noqa: E501
        :rtype: NotificationRequestId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NotificationRequestInfo.


        :param id: The id of this NotificationRequestInfo.  # noqa: E501
        :type: NotificationRequestId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this NotificationRequestInfo.  # noqa: E501


        :return: The created_time of this NotificationRequestInfo.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this NotificationRequestInfo.


        :param created_time: The created_time of this NotificationRequestInfo.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NotificationRequestInfo.  # noqa: E501


        :return: The tenant_id of this NotificationRequestInfo.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NotificationRequestInfo.


        :param tenant_id: The tenant_id of this NotificationRequestInfo.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def targets(self):
        """Gets the targets of this NotificationRequestInfo.  # noqa: E501


        :return: The targets of this NotificationRequestInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this NotificationRequestInfo.


        :param targets: The targets of this NotificationRequestInfo.  # noqa: E501
        :type: list[str]
        """
        if targets is None:
            raise ValueError("Invalid value for `targets`, must not be `None`")  # noqa: E501

        self._targets = targets

    @property
    def template_id(self):
        """Gets the template_id of this NotificationRequestInfo.  # noqa: E501


        :return: The template_id of this NotificationRequestInfo.  # noqa: E501
        :rtype: NotificationTemplateId
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this NotificationRequestInfo.


        :param template_id: The template_id of this NotificationRequestInfo.  # noqa: E501
        :type: NotificationTemplateId
        """

        self._template_id = template_id

    @property
    def template(self):
        """Gets the template of this NotificationRequestInfo.  # noqa: E501


        :return: The template of this NotificationRequestInfo.  # noqa: E501
        :rtype: NotificationTemplate
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this NotificationRequestInfo.


        :param template: The template of this NotificationRequestInfo.  # noqa: E501
        :type: NotificationTemplate
        """

        self._template = template

    @property
    def info(self):
        """Gets the info of this NotificationRequestInfo.  # noqa: E501


        :return: The info of this NotificationRequestInfo.  # noqa: E501
        :rtype: NotificationInfo
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this NotificationRequestInfo.


        :param info: The info of this NotificationRequestInfo.  # noqa: E501
        :type: NotificationInfo
        """

        self._info = info

    @property
    def additional_config(self):
        """Gets the additional_config of this NotificationRequestInfo.  # noqa: E501


        :return: The additional_config of this NotificationRequestInfo.  # noqa: E501
        :rtype: NotificationRequestConfig
        """
        return self._additional_config

    @additional_config.setter
    def additional_config(self, additional_config):
        """Sets the additional_config of this NotificationRequestInfo.


        :param additional_config: The additional_config of this NotificationRequestInfo.  # noqa: E501
        :type: NotificationRequestConfig
        """

        self._additional_config = additional_config

    @property
    def originator_entity_id(self):
        """Gets the originator_entity_id of this NotificationRequestInfo.  # noqa: E501


        :return: The originator_entity_id of this NotificationRequestInfo.  # noqa: E501
        :rtype: EntityId
        """
        return self._originator_entity_id

    @originator_entity_id.setter
    def originator_entity_id(self, originator_entity_id):
        """Sets the originator_entity_id of this NotificationRequestInfo.


        :param originator_entity_id: The originator_entity_id of this NotificationRequestInfo.  # noqa: E501
        :type: EntityId
        """

        self._originator_entity_id = originator_entity_id

    @property
    def rule_id(self):
        """Gets the rule_id of this NotificationRequestInfo.  # noqa: E501


        :return: The rule_id of this NotificationRequestInfo.  # noqa: E501
        :rtype: NotificationRuleId
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this NotificationRequestInfo.


        :param rule_id: The rule_id of this NotificationRequestInfo.  # noqa: E501
        :type: NotificationRuleId
        """

        self._rule_id = rule_id

    @property
    def status(self):
        """Gets the status of this NotificationRequestInfo.  # noqa: E501


        :return: The status of this NotificationRequestInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NotificationRequestInfo.


        :param status: The status of this NotificationRequestInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["PROCESSING", "SENT", "SCHEDULED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def stats(self):
        """Gets the stats of this NotificationRequestInfo.  # noqa: E501


        :return: The stats of this NotificationRequestInfo.  # noqa: E501
        :rtype: NotificationRequestStats
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this NotificationRequestInfo.


        :param stats: The stats of this NotificationRequestInfo.  # noqa: E501
        :type: NotificationRequestStats
        """

        self._stats = stats

    @property
    def template_name(self):
        """Gets the template_name of this NotificationRequestInfo.  # noqa: E501


        :return: The template_name of this NotificationRequestInfo.  # noqa: E501
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this NotificationRequestInfo.


        :param template_name: The template_name of this NotificationRequestInfo.  # noqa: E501
        :type: str
        """

        self._template_name = template_name

    @property
    def delivery_methods(self):
        """Gets the delivery_methods of this NotificationRequestInfo.  # noqa: E501


        :return: The delivery_methods of this NotificationRequestInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._delivery_methods

    @delivery_methods.setter
    def delivery_methods(self, delivery_methods):
        """Sets the delivery_methods of this NotificationRequestInfo.


        :param delivery_methods: The delivery_methods of this NotificationRequestInfo.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["WEB", "EMAIL", "SMS", "SLACK", "MICROSOFT_TEAMS", "MOBILE_APP"]  # noqa: E501
        if not set(delivery_methods).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `delivery_methods` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(delivery_methods) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._delivery_methods = delivery_methods

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
        if issubclass(NotificationRequestInfo, dict):
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
        if not isinstance(other, NotificationRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
