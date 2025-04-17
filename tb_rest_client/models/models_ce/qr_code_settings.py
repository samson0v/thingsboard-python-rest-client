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

class QrCodeSettings(object):
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
        'id': 'QrCodeSettingsId',
        'created_time': 'int',
        'tenant_id': 'TenantId',
        'use_system_settings': 'bool',
        'use_default_app': 'bool',
        'mobile_app_bundle_id': 'MobileAppBundleId',
        'qr_code_config': 'QRCodeConfig',
        'android_enabled': 'bool',
        'ios_enabled': 'bool',
        'google_play_link': 'str',
        'app_store_link': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'tenant_id': 'tenantId',
        'use_system_settings': 'useSystemSettings',
        'use_default_app': 'useDefaultApp',
        'mobile_app_bundle_id': 'mobileAppBundleId',
        'qr_code_config': 'qrCodeConfig',
        'android_enabled': 'androidEnabled',
        'ios_enabled': 'iosEnabled',
        'google_play_link': 'googlePlayLink',
        'app_store_link': 'appStoreLink'
    }

    def __init__(self, id=None, created_time=None, tenant_id=None, use_system_settings=None, use_default_app=None, mobile_app_bundle_id=None, qr_code_config=None, android_enabled=None, ios_enabled=None, google_play_link=None, app_store_link=None):  # noqa: E501
        """QrCodeSettings - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._tenant_id = None
        self._use_system_settings = None
        self._use_default_app = None
        self._mobile_app_bundle_id = None
        self._qr_code_config = None
        self._android_enabled = None
        self._ios_enabled = None
        self._google_play_link = None
        self._app_store_link = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if use_system_settings is not None:
            self.use_system_settings = use_system_settings
        if use_default_app is not None:
            self.use_default_app = use_default_app
        if mobile_app_bundle_id is not None:
            self.mobile_app_bundle_id = mobile_app_bundle_id
        self.qr_code_config = qr_code_config
        if android_enabled is not None:
            self.android_enabled = android_enabled
        if ios_enabled is not None:
            self.ios_enabled = ios_enabled
        if google_play_link is not None:
            self.google_play_link = google_play_link
        if app_store_link is not None:
            self.app_store_link = app_store_link

    @property
    def id(self):
        """Gets the id of this QrCodeSettings.  # noqa: E501


        :return: The id of this QrCodeSettings.  # noqa: E501
        :rtype: QrCodeSettingsId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QrCodeSettings.


        :param id: The id of this QrCodeSettings.  # noqa: E501
        :type: QrCodeSettingsId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this QrCodeSettings.  # noqa: E501


        :return: The created_time of this QrCodeSettings.  # noqa: E501
        :rtype: object
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this QrCodeSettings.


        :param created_time: The created_time of this QrCodeSettings.  # noqa: E501
        :type: object
        """

        self._created_time = created_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this QrCodeSettings.  # noqa: E501

        JSON object with Tenant Id.  # noqa: E501

        :return: The tenant_id of this QrCodeSettings.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this QrCodeSettings.

        JSON object with Tenant Id.  # noqa: E501

        :param tenant_id: The tenant_id of this QrCodeSettings.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def use_system_settings(self):
        """Gets the use_system_settings of this QrCodeSettings.  # noqa: E501

        Use settings from system level  # noqa: E501

        :return: The use_system_settings of this QrCodeSettings.  # noqa: E501
        :rtype: object
        """
        return self._use_system_settings

    @use_system_settings.setter
    def use_system_settings(self, use_system_settings):
        """Sets the use_system_settings of this QrCodeSettings.

        Use settings from system level  # noqa: E501

        :param use_system_settings: The use_system_settings of this QrCodeSettings.  # noqa: E501
        :type: object
        """

        self._use_system_settings = use_system_settings

    @property
    def use_default_app(self):
        """Gets the use_default_app of this QrCodeSettings.  # noqa: E501

        Type of application: true means use default Thingsboard app  # noqa: E501

        :return: The use_default_app of this QrCodeSettings.  # noqa: E501
        :rtype: object
        """
        return self._use_default_app

    @use_default_app.setter
    def use_default_app(self, use_default_app):
        """Sets the use_default_app of this QrCodeSettings.

        Type of application: true means use default Thingsboard app  # noqa: E501

        :param use_default_app: The use_default_app of this QrCodeSettings.  # noqa: E501
        :type: object
        """

        self._use_default_app = use_default_app

    @property
    def mobile_app_bundle_id(self):
        """Gets the mobile_app_bundle_id of this QrCodeSettings.  # noqa: E501

        Mobile app bundle.  # noqa: E501

        :return: The mobile_app_bundle_id of this QrCodeSettings.  # noqa: E501
        :rtype: MobileAppBundleId
        """
        return self._mobile_app_bundle_id

    @mobile_app_bundle_id.setter
    def mobile_app_bundle_id(self, mobile_app_bundle_id):
        """Sets the mobile_app_bundle_id of this QrCodeSettings.

        Mobile app bundle.  # noqa: E501

        :param mobile_app_bundle_id: The mobile_app_bundle_id of this QrCodeSettings.  # noqa: E501
        :type: MobileAppBundleId
        """

        self._mobile_app_bundle_id = mobile_app_bundle_id

    @property
    def qr_code_config(self):
        """Gets the qr_code_config of this QrCodeSettings.  # noqa: E501

        QR code config configuration.  # noqa: E501

        :return: The qr_code_config of this QrCodeSettings.  # noqa: E501
        :rtype: QRCodeConfig
        """
        return self._qr_code_config

    @qr_code_config.setter
    def qr_code_config(self, qr_code_config):
        """Sets the qr_code_config of this QrCodeSettings.

        QR code config configuration.  # noqa: E501

        :param qr_code_config: The qr_code_config of this QrCodeSettings.  # noqa: E501
        :type: QRCodeConfig
        """
        if qr_code_config is None:
            raise ValueError("Invalid value for `qr_code_config`, must not be `None`")  # noqa: E501

        self._qr_code_config = qr_code_config

    @property
    def android_enabled(self):
        """Gets the android_enabled of this QrCodeSettings.  # noqa: E501

        Indicates if google play link is available  # noqa: E501

        :return: The android_enabled of this QrCodeSettings.  # noqa: E501
        :rtype: object
        """
        return self._android_enabled

    @android_enabled.setter
    def android_enabled(self, android_enabled):
        """Sets the android_enabled of this QrCodeSettings.

        Indicates if google play link is available  # noqa: E501

        :param android_enabled: The android_enabled of this QrCodeSettings.  # noqa: E501
        :type: object
        """

        self._android_enabled = android_enabled

    @property
    def ios_enabled(self):
        """Gets the ios_enabled of this QrCodeSettings.  # noqa: E501

        Indicates if apple store link is available  # noqa: E501

        :return: The ios_enabled of this QrCodeSettings.  # noqa: E501
        :rtype: object
        """
        return self._ios_enabled

    @ios_enabled.setter
    def ios_enabled(self, ios_enabled):
        """Sets the ios_enabled of this QrCodeSettings.

        Indicates if apple store link is available  # noqa: E501

        :param ios_enabled: The ios_enabled of this QrCodeSettings.  # noqa: E501
        :type: object
        """

        self._ios_enabled = ios_enabled

    @property
    def google_play_link(self):
        """Gets the google_play_link of this QrCodeSettings.  # noqa: E501


        :return: The google_play_link of this QrCodeSettings.  # noqa: E501
        :rtype: object
        """
        return self._google_play_link

    @google_play_link.setter
    def google_play_link(self, google_play_link):
        """Sets the google_play_link of this QrCodeSettings.


        :param google_play_link: The google_play_link of this QrCodeSettings.  # noqa: E501
        :type: object
        """

        self._google_play_link = google_play_link

    @property
    def app_store_link(self):
        """Gets the app_store_link of this QrCodeSettings.  # noqa: E501


        :return: The app_store_link of this QrCodeSettings.  # noqa: E501
        :rtype: object
        """
        return self._app_store_link

    @app_store_link.setter
    def app_store_link(self, app_store_link):
        """Sets the app_store_link of this QrCodeSettings.


        :param app_store_link: The app_store_link of this QrCodeSettings.  # noqa: E501
        :type: object
        """

        self._app_store_link = app_store_link

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
        if issubclass(QrCodeSettings, dict):
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
        if not isinstance(other, QrCodeSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
