# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 4.0.0PE
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

class TenantProfileQueueConfiguration(object):
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
        'name': 'str',
        'topic': 'str',
        'poll_interval': 'int',
        'partitions': 'int',
        'consumer_per_partition': 'bool',
        'pack_processing_timeout': 'int',
        'submit_strategy': 'SubmitStrategy',
        'processing_strategy': 'ProcessingStrategy',
        'additional_info': 'JsonNode'
    }

    attribute_map = {
        'name': 'name',
        'topic': 'topic',
        'poll_interval': 'pollInterval',
        'partitions': 'partitions',
        'consumer_per_partition': 'consumerPerPartition',
        'pack_processing_timeout': 'packProcessingTimeout',
        'submit_strategy': 'submitStrategy',
        'processing_strategy': 'processingStrategy',
        'additional_info': 'additionalInfo'
    }

    def __init__(self, name=None, topic=None, poll_interval=None, partitions=None, consumer_per_partition=None, pack_processing_timeout=None, submit_strategy=None, processing_strategy=None, additional_info=None):  # noqa: E501
        """TenantProfileQueueConfiguration - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._topic = None
        self._poll_interval = None
        self._partitions = None
        self._consumer_per_partition = None
        self._pack_processing_timeout = None
        self._submit_strategy = None
        self._processing_strategy = None
        self._additional_info = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if topic is not None:
            self.topic = topic
        if poll_interval is not None:
            self.poll_interval = poll_interval
        if partitions is not None:
            self.partitions = partitions
        if consumer_per_partition is not None:
            self.consumer_per_partition = consumer_per_partition
        if pack_processing_timeout is not None:
            self.pack_processing_timeout = pack_processing_timeout
        if submit_strategy is not None:
            self.submit_strategy = submit_strategy
        if processing_strategy is not None:
            self.processing_strategy = processing_strategy
        if additional_info is not None:
            self.additional_info = additional_info

    @property
    def name(self):
        """Gets the name of this TenantProfileQueueConfiguration.  # noqa: E501


        :return: The name of this TenantProfileQueueConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TenantProfileQueueConfiguration.


        :param name: The name of this TenantProfileQueueConfiguration.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def topic(self):
        """Gets the topic of this TenantProfileQueueConfiguration.  # noqa: E501


        :return: The topic of this TenantProfileQueueConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this TenantProfileQueueConfiguration.


        :param topic: The topic of this TenantProfileQueueConfiguration.  # noqa: E501
        :type: str
        """

        self._topic = topic

    @property
    def poll_interval(self):
        """Gets the poll_interval of this TenantProfileQueueConfiguration.  # noqa: E501


        :return: The poll_interval of this TenantProfileQueueConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._poll_interval

    @poll_interval.setter
    def poll_interval(self, poll_interval):
        """Sets the poll_interval of this TenantProfileQueueConfiguration.


        :param poll_interval: The poll_interval of this TenantProfileQueueConfiguration.  # noqa: E501
        :type: int
        """

        self._poll_interval = poll_interval

    @property
    def partitions(self):
        """Gets the partitions of this TenantProfileQueueConfiguration.  # noqa: E501


        :return: The partitions of this TenantProfileQueueConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._partitions

    @partitions.setter
    def partitions(self, partitions):
        """Sets the partitions of this TenantProfileQueueConfiguration.


        :param partitions: The partitions of this TenantProfileQueueConfiguration.  # noqa: E501
        :type: int
        """

        self._partitions = partitions

    @property
    def consumer_per_partition(self):
        """Gets the consumer_per_partition of this TenantProfileQueueConfiguration.  # noqa: E501


        :return: The consumer_per_partition of this TenantProfileQueueConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._consumer_per_partition

    @consumer_per_partition.setter
    def consumer_per_partition(self, consumer_per_partition):
        """Sets the consumer_per_partition of this TenantProfileQueueConfiguration.


        :param consumer_per_partition: The consumer_per_partition of this TenantProfileQueueConfiguration.  # noqa: E501
        :type: bool
        """

        self._consumer_per_partition = consumer_per_partition

    @property
    def pack_processing_timeout(self):
        """Gets the pack_processing_timeout of this TenantProfileQueueConfiguration.  # noqa: E501


        :return: The pack_processing_timeout of this TenantProfileQueueConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._pack_processing_timeout

    @pack_processing_timeout.setter
    def pack_processing_timeout(self, pack_processing_timeout):
        """Sets the pack_processing_timeout of this TenantProfileQueueConfiguration.


        :param pack_processing_timeout: The pack_processing_timeout of this TenantProfileQueueConfiguration.  # noqa: E501
        :type: int
        """

        self._pack_processing_timeout = pack_processing_timeout

    @property
    def submit_strategy(self):
        """Gets the submit_strategy of this TenantProfileQueueConfiguration.  # noqa: E501


        :return: The submit_strategy of this TenantProfileQueueConfiguration.  # noqa: E501
        :rtype: SubmitStrategy
        """
        return self._submit_strategy

    @submit_strategy.setter
    def submit_strategy(self, submit_strategy):
        """Sets the submit_strategy of this TenantProfileQueueConfiguration.


        :param submit_strategy: The submit_strategy of this TenantProfileQueueConfiguration.  # noqa: E501
        :type: SubmitStrategy
        """

        self._submit_strategy = submit_strategy

    @property
    def processing_strategy(self):
        """Gets the processing_strategy of this TenantProfileQueueConfiguration.  # noqa: E501


        :return: The processing_strategy of this TenantProfileQueueConfiguration.  # noqa: E501
        :rtype: ProcessingStrategy
        """
        return self._processing_strategy

    @processing_strategy.setter
    def processing_strategy(self, processing_strategy):
        """Sets the processing_strategy of this TenantProfileQueueConfiguration.


        :param processing_strategy: The processing_strategy of this TenantProfileQueueConfiguration.  # noqa: E501
        :type: ProcessingStrategy
        """

        self._processing_strategy = processing_strategy

    @property
    def additional_info(self):
        """Gets the additional_info of this TenantProfileQueueConfiguration.  # noqa: E501


        :return: The additional_info of this TenantProfileQueueConfiguration.  # noqa: E501
        :rtype: JsonNode
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this TenantProfileQueueConfiguration.


        :param additional_info: The additional_info of this TenantProfileQueueConfiguration.  # noqa: E501
        :type: JsonNode
        """

        self._additional_info = additional_info

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
        if issubclass(TenantProfileQueueConfiguration, dict):
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
        if not isinstance(other, TenantProfileQueueConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
