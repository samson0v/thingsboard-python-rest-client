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

class SolutionInstallResponse(object):
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
        'dashboard_group_id': 'EntityGroupId',
        'dashboard_id': 'DashboardId',
        'public_id': 'CustomerId',
        'main_dashboard_public': 'bool',
        'details': 'str',
        'success': 'bool'
    }

    attribute_map = {
        'dashboard_group_id': 'dashboardGroupId',
        'dashboard_id': 'dashboardId',
        'public_id': 'publicId',
        'main_dashboard_public': 'mainDashboardPublic',
        'details': 'details',
        'success': 'success'
    }

    def __init__(self, dashboard_group_id=None, dashboard_id=None, public_id=None, main_dashboard_public=None, details=None, success=None):  # noqa: E501
        """SolutionInstallResponse - a model defined in Swagger"""  # noqa: E501
        self._dashboard_group_id = None
        self._dashboard_id = None
        self._public_id = None
        self._main_dashboard_public = None
        self._details = None
        self._success = None
        self.discriminator = None
        if dashboard_group_id is not None:
            self.dashboard_group_id = dashboard_group_id
        if dashboard_id is not None:
            self.dashboard_id = dashboard_id
        if public_id is not None:
            self.public_id = public_id
        if main_dashboard_public is not None:
            self.main_dashboard_public = main_dashboard_public
        if details is not None:
            self.details = details
        if success is not None:
            self.success = success

    @property
    def dashboard_group_id(self):
        """Gets the dashboard_group_id of this SolutionInstallResponse.  # noqa: E501


        :return: The dashboard_group_id of this SolutionInstallResponse.  # noqa: E501
        :rtype: EntityGroupId
        """
        return self._dashboard_group_id

    @dashboard_group_id.setter
    def dashboard_group_id(self, dashboard_group_id):
        """Sets the dashboard_group_id of this SolutionInstallResponse.


        :param dashboard_group_id: The dashboard_group_id of this SolutionInstallResponse.  # noqa: E501
        :type: EntityGroupId
        """

        self._dashboard_group_id = dashboard_group_id

    @property
    def dashboard_id(self):
        """Gets the dashboard_id of this SolutionInstallResponse.  # noqa: E501


        :return: The dashboard_id of this SolutionInstallResponse.  # noqa: E501
        :rtype: DashboardId
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """Sets the dashboard_id of this SolutionInstallResponse.


        :param dashboard_id: The dashboard_id of this SolutionInstallResponse.  # noqa: E501
        :type: DashboardId
        """

        self._dashboard_id = dashboard_id

    @property
    def public_id(self):
        """Gets the public_id of this SolutionInstallResponse.  # noqa: E501


        :return: The public_id of this SolutionInstallResponse.  # noqa: E501
        :rtype: CustomerId
        """
        return self._public_id

    @public_id.setter
    def public_id(self, public_id):
        """Sets the public_id of this SolutionInstallResponse.


        :param public_id: The public_id of this SolutionInstallResponse.  # noqa: E501
        :type: CustomerId
        """

        self._public_id = public_id

    @property
    def main_dashboard_public(self):
        """Gets the main_dashboard_public of this SolutionInstallResponse.  # noqa: E501

        Is the main dashboard public  # noqa: E501

        :return: The main_dashboard_public of this SolutionInstallResponse.  # noqa: E501
        :rtype: bool
        """
        return self._main_dashboard_public

    @main_dashboard_public.setter
    def main_dashboard_public(self, main_dashboard_public):
        """Sets the main_dashboard_public of this SolutionInstallResponse.

        Is the main dashboard public  # noqa: E501

        :param main_dashboard_public: The main_dashboard_public of this SolutionInstallResponse.  # noqa: E501
        :type: bool
        """

        self._main_dashboard_public = main_dashboard_public

    @property
    def details(self):
        """Gets the details of this SolutionInstallResponse.  # noqa: E501

        Markdown with solution usage instructions  # noqa: E501

        :return: The details of this SolutionInstallResponse.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this SolutionInstallResponse.

        Markdown with solution usage instructions  # noqa: E501

        :param details: The details of this SolutionInstallResponse.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def success(self):
        """Gets the success of this SolutionInstallResponse.  # noqa: E501

        Indicates that template was installed successfully  # noqa: E501

        :return: The success of this SolutionInstallResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this SolutionInstallResponse.

        Indicates that template was installed successfully  # noqa: E501

        :param success: The success of this SolutionInstallResponse.  # noqa: E501
        :type: bool
        """

        self._success = success

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
        if issubclass(SolutionInstallResponse, dict):
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
        if not isinstance(other, SolutionInstallResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
