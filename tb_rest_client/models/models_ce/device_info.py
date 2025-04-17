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

class DeviceInfo(object):
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
        'id': 'DeviceId',
        'created_time': 'int',
        'tenant_id': 'TenantId',
        'customer_id': 'CustomerId',
        'name': 'str',
        'type': 'str',
        'label': 'str',
        'device_profile_id': 'DeviceProfileId',
        'firmware_id': 'OtaPackageId',
        'software_id': 'OtaPackageId',
        'version': 'int',
        'customer_title': 'str',
        'customer_is_public': 'bool',
        'device_profile_name': 'str',
        'active': 'bool',
        'additional_info': 'JsonNode',
        'device_data': 'DeviceData'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'tenant_id': 'tenantId',
        'customer_id': 'customerId',
        'name': 'name',
        'type': 'type',
        'label': 'label',
        'device_profile_id': 'deviceProfileId',
        'firmware_id': 'firmwareId',
        'software_id': 'softwareId',
        'version': 'version',
        'customer_title': 'customerTitle',
        'customer_is_public': 'customerIsPublic',
        'device_profile_name': 'deviceProfileName',
        'active': 'active',
        'additional_info': 'additionalInfo',
        'device_data': 'deviceData'
    }

    def __init__(self, id=None, created_time=None, tenant_id=None, customer_id=None, name=None, type=None, label=None, device_profile_id=None, firmware_id=None, software_id=None, version=None, customer_title=None, customer_is_public=None, device_profile_name=None, active=None, additional_info=None, device_data=None):  # noqa: E501
        """DeviceInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._tenant_id = None
        self._customer_id = None
        self._name = None
        self._type = None
        self._label = None
        self._device_profile_id = None
        self._firmware_id = None
        self._software_id = None
        self._version = None
        self._customer_title = None
        self._customer_is_public = None
        self._device_profile_name = None
        self._active = None
        self._additional_info = None
        self._device_data = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if customer_id is not None:
            self.customer_id = customer_id
        self.name = name
        if type is not None:
            self.type = type
        if label is not None:
            self.label = label
        self.device_profile_id = device_profile_id
        if firmware_id is not None:
            self.firmware_id = firmware_id
        if software_id is not None:
            self.software_id = software_id
        if version is not None:
            self.version = version
        if customer_title is not None:
            self.customer_title = customer_title
        if customer_is_public is not None:
            self.customer_is_public = customer_is_public
        if device_profile_name is not None:
            self.device_profile_name = device_profile_name
        if active is not None:
            self.active = active
        if additional_info is not None:
            self.additional_info = additional_info
        if device_data is not None:
            self.device_data = device_data

    @property
    def id(self):
        """Gets the id of this DeviceInfo.  # noqa: E501


        :return: The id of this DeviceInfo.  # noqa: E501
        :rtype: DeviceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceInfo.


        :param id: The id of this DeviceInfo.  # noqa: E501
        :type: DeviceId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this DeviceInfo.  # noqa: E501

        Timestamp of the device creation, in milliseconds  # noqa: E501

        :return: The created_time of this DeviceInfo.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this DeviceInfo.

        Timestamp of the device creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this DeviceInfo.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this DeviceInfo.  # noqa: E501


        :return: The tenant_id of this DeviceInfo.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this DeviceInfo.


        :param tenant_id: The tenant_id of this DeviceInfo.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def customer_id(self):
        """Gets the customer_id of this DeviceInfo.  # noqa: E501


        :return: The customer_id of this DeviceInfo.  # noqa: E501
        :rtype: CustomerId
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this DeviceInfo.


        :param customer_id: The customer_id of this DeviceInfo.  # noqa: E501
        :type: CustomerId
        """

        self._customer_id = customer_id

    @property
    def name(self):
        """Gets the name of this DeviceInfo.  # noqa: E501

        Unique Device Name in scope of Tenant  # noqa: E501

        :return: The name of this DeviceInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceInfo.

        Unique Device Name in scope of Tenant  # noqa: E501

        :param name: The name of this DeviceInfo.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this DeviceInfo.  # noqa: E501

        Device Profile Name  # noqa: E501

        :return: The type of this DeviceInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeviceInfo.

        Device Profile Name  # noqa: E501

        :param type: The type of this DeviceInfo.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def label(self):
        """Gets the label of this DeviceInfo.  # noqa: E501

        Label that may be used in widgets  # noqa: E501

        :return: The label of this DeviceInfo.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this DeviceInfo.

        Label that may be used in widgets  # noqa: E501

        :param label: The label of this DeviceInfo.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def device_profile_id(self):
        """Gets the device_profile_id of this DeviceInfo.  # noqa: E501


        :return: The device_profile_id of this DeviceInfo.  # noqa: E501
        :rtype: DeviceProfileId
        """
        return self._device_profile_id

    @device_profile_id.setter
    def device_profile_id(self, device_profile_id):
        """Sets the device_profile_id of this DeviceInfo.


        :param device_profile_id: The device_profile_id of this DeviceInfo.  # noqa: E501
        :type: DeviceProfileId
        """
        if device_profile_id is None:
            raise ValueError("Invalid value for `device_profile_id`, must not be `None`")  # noqa: E501

        self._device_profile_id = device_profile_id

    @property
    def firmware_id(self):
        """Gets the firmware_id of this DeviceInfo.  # noqa: E501


        :return: The firmware_id of this DeviceInfo.  # noqa: E501
        :rtype: OtaPackageId
        """
        return self._firmware_id

    @firmware_id.setter
    def firmware_id(self, firmware_id):
        """Sets the firmware_id of this DeviceInfo.


        :param firmware_id: The firmware_id of this DeviceInfo.  # noqa: E501
        :type: OtaPackageId
        """

        self._firmware_id = firmware_id

    @property
    def software_id(self):
        """Gets the software_id of this DeviceInfo.  # noqa: E501


        :return: The software_id of this DeviceInfo.  # noqa: E501
        :rtype: OtaPackageId
        """
        return self._software_id

    @software_id.setter
    def software_id(self, software_id):
        """Sets the software_id of this DeviceInfo.


        :param software_id: The software_id of this DeviceInfo.  # noqa: E501
        :type: OtaPackageId
        """

        self._software_id = software_id

    @property
    def version(self):
        """Gets the version of this DeviceInfo.  # noqa: E501


        :return: The version of this DeviceInfo.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DeviceInfo.


        :param version: The version of this DeviceInfo.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def customer_title(self):
        """Gets the customer_title of this DeviceInfo.  # noqa: E501

        Title of the Customer that owns the device.  # noqa: E501

        :return: The customer_title of this DeviceInfo.  # noqa: E501
        :rtype: str
        """
        return self._customer_title

    @customer_title.setter
    def customer_title(self, customer_title):
        """Sets the customer_title of this DeviceInfo.

        Title of the Customer that owns the device.  # noqa: E501

        :param customer_title: The customer_title of this DeviceInfo.  # noqa: E501
        :type: str
        """

        self._customer_title = customer_title

    @property
    def customer_is_public(self):
        """Gets the customer_is_public of this DeviceInfo.  # noqa: E501

        Indicates special 'Public' Customer that is auto-generated to use the devices on public dashboards.  # noqa: E501

        :return: The customer_is_public of this DeviceInfo.  # noqa: E501
        :rtype: bool
        """
        return self._customer_is_public

    @customer_is_public.setter
    def customer_is_public(self, customer_is_public):
        """Sets the customer_is_public of this DeviceInfo.

        Indicates special 'Public' Customer that is auto-generated to use the devices on public dashboards.  # noqa: E501

        :param customer_is_public: The customer_is_public of this DeviceInfo.  # noqa: E501
        :type: bool
        """

        self._customer_is_public = customer_is_public

    @property
    def device_profile_name(self):
        """Gets the device_profile_name of this DeviceInfo.  # noqa: E501

        Name of the corresponding Device Profile.  # noqa: E501

        :return: The device_profile_name of this DeviceInfo.  # noqa: E501
        :rtype: str
        """
        return self._device_profile_name

    @device_profile_name.setter
    def device_profile_name(self, device_profile_name):
        """Sets the device_profile_name of this DeviceInfo.

        Name of the corresponding Device Profile.  # noqa: E501

        :param device_profile_name: The device_profile_name of this DeviceInfo.  # noqa: E501
        :type: str
        """

        self._device_profile_name = device_profile_name

    @property
    def active(self):
        """Gets the active of this DeviceInfo.  # noqa: E501

        Device active flag.  # noqa: E501

        :return: The active of this DeviceInfo.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this DeviceInfo.

        Device active flag.  # noqa: E501

        :param active: The active of this DeviceInfo.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def additional_info(self):
        """Gets the additional_info of this DeviceInfo.  # noqa: E501


        :return: The additional_info of this DeviceInfo.  # noqa: E501
        :rtype: JsonNode
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this DeviceInfo.


        :param additional_info: The additional_info of this DeviceInfo.  # noqa: E501
        :type: JsonNode
        """

        self._additional_info = additional_info

    @property
    def device_data(self):
        """Gets the device_data of this DeviceInfo.  # noqa: E501


        :return: The device_data of this DeviceInfo.  # noqa: E501
        :rtype: DeviceData
        """
        return self._device_data

    @device_data.setter
    def device_data(self, device_data):
        """Sets the device_data of this DeviceInfo.


        :param device_data: The device_data of this DeviceInfo.  # noqa: E501
        :type: DeviceData
        """

        self._device_data = device_data

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
        if issubclass(DeviceInfo, dict):
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
        if not isinstance(other, DeviceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
