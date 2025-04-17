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

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tb_rest_client.api_client import ApiClient


class GroupPermissionControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_group_permission_using_delete(self, group_permission_id, **kwargs):  # noqa: E501
        """Delete group permission (deleteGroupPermission)  # noqa: E501

        Deletes the group permission. Referencing non-existing group permission Id will cause an error.   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_group_permission_using_delete(group_permission_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_permission_id: A string value representing the group permission id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_group_permission_using_delete_with_http_info(group_permission_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_group_permission_using_delete_with_http_info(group_permission_id, **kwargs)  # noqa: E501
            return data

    def delete_group_permission_using_delete_with_http_info(self, group_permission_id, **kwargs):  # noqa: E501
        """Delete group permission (deleteGroupPermission)  # noqa: E501

        Deletes the group permission. Referencing non-existing group permission Id will cause an error.   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_group_permission_using_delete_with_http_info(group_permission_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_permission_id: A string value representing the group permission id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_permission_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_group_permission_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_permission_id' is set
        if ('group_permission_id' not in params or
                params['group_permission_id'] is None):
            raise ValueError("Missing the required parameter `group_permission_id` when calling `delete_group_permission_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_permission_id' in params:
            path_params['groupPermissionId'] = params['group_permission_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/groupPermission/{groupPermissionId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_entity_group_permissions_using_get(self, entity_group_id, **kwargs):  # noqa: E501
        """Get group permissions by Entity Group Id (getEntityGroupPermissions)  # noqa: E501

        Returns a list of group permission objects that is assigned for the specified Entity Group Id. Group permission entity represents list of allowed operations for certain User Group to perform against certain Entity Group. Basically, this entity wires three other entities:    * Role that defines set of allowed operations;  * User Group that defines set of users who may perform the operations;   * Entity Group that defines set of entities which will be accessible to users;   Group Permission Info object extends the Group Permissions with the full information about Role and User and/or Entity Groups.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_entity_group_permissions_using_get(entity_group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_group_id: A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: list[GroupPermissionInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_entity_group_permissions_using_get_with_http_info(entity_group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_entity_group_permissions_using_get_with_http_info(entity_group_id, **kwargs)  # noqa: E501
            return data

    def get_entity_group_permissions_using_get_with_http_info(self, entity_group_id, **kwargs):  # noqa: E501
        """Get group permissions by Entity Group Id (getEntityGroupPermissions)  # noqa: E501

        Returns a list of group permission objects that is assigned for the specified Entity Group Id. Group permission entity represents list of allowed operations for certain User Group to perform against certain Entity Group. Basically, this entity wires three other entities:    * Role that defines set of allowed operations;  * User Group that defines set of users who may perform the operations;   * Entity Group that defines set of entities which will be accessible to users;   Group Permission Info object extends the Group Permissions with the full information about Role and User and/or Entity Groups.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_entity_group_permissions_using_get_with_http_info(entity_group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_group_id: A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: list[GroupPermissionInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_group_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_entity_group_permissions_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_group_id' is set
        if ('entity_group_id' not in params or
                params['entity_group_id'] is None):
            raise ValueError("Missing the required parameter `entity_group_id` when calling `get_entity_group_permissions_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity_group_id' in params:
            path_params['entityGroupId'] = params['entity_group_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/entityGroup/{entityGroupId}/groupPermissions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GroupPermissionInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_group_permission_by_id_using_get(self, group_permission_id, **kwargs):  # noqa: E501
        """Get Group Permission (getGroupPermissionById)  # noqa: E501

        Fetch the Group Permission object based on the provided Group Permission Id. Group permission entity represents list of allowed operations for certain User Group to perform against certain Entity Group. Basically, this entity wires three other entities:    * Role that defines set of allowed operations;  * User Group that defines set of users who may perform the operations;   * Entity Group that defines set of entities which will be accessible to users;   Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_permission_by_id_using_get(group_permission_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_permission_id: A string value representing the group permission id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: GroupPermission
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_group_permission_by_id_using_get_with_http_info(group_permission_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_group_permission_by_id_using_get_with_http_info(group_permission_id, **kwargs)  # noqa: E501
            return data

    def get_group_permission_by_id_using_get_with_http_info(self, group_permission_id, **kwargs):  # noqa: E501
        """Get Group Permission (getGroupPermissionById)  # noqa: E501

        Fetch the Group Permission object based on the provided Group Permission Id. Group permission entity represents list of allowed operations for certain User Group to perform against certain Entity Group. Basically, this entity wires three other entities:    * Role that defines set of allowed operations;  * User Group that defines set of users who may perform the operations;   * Entity Group that defines set of entities which will be accessible to users;   Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_permission_by_id_using_get_with_http_info(group_permission_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_permission_id: A string value representing the group permission id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: GroupPermission
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_permission_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_group_permission_by_id_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_permission_id' is set
        if ('group_permission_id' not in params or
                params['group_permission_id'] is None):
            raise ValueError("Missing the required parameter `group_permission_id` when calling `get_group_permission_by_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_permission_id' in params:
            path_params['groupPermissionId'] = params['group_permission_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/groupPermission/{groupPermissionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GroupPermission',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_group_permission_info_by_id_using_get(self, group_permission_id, is_user_group, **kwargs):  # noqa: E501
        """Get Group Permission Info (getGroupPermissionInfoById)  # noqa: E501

        Fetch the Group Permission Info object based on the provided Group Permission Id and the flag that controls what additional information to load: User or Entity Group. Group permission entity represents list of allowed operations for certain User Group to perform against certain Entity Group. Basically, this entity wires three other entities:    * Role that defines set of allowed operations;  * User Group that defines set of users who may perform the operations;   * Entity Group that defines set of entities which will be accessible to users;   Group Permission Info object extends the Group Permissions with the full information about Role and User and/or Entity Groups.  Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_permission_info_by_id_using_get(group_permission_id, is_user_group, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_permission_id: A string value representing the group permission id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param bool is_user_group: Load additional information about User('true') or Entity Group('false). (required)
        :return: GroupPermissionInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_group_permission_info_by_id_using_get_with_http_info(group_permission_id, is_user_group, **kwargs)  # noqa: E501
        else:
            (data) = self.get_group_permission_info_by_id_using_get_with_http_info(group_permission_id, is_user_group, **kwargs)  # noqa: E501
            return data

    def get_group_permission_info_by_id_using_get_with_http_info(self, group_permission_id, is_user_group, **kwargs):  # noqa: E501
        """Get Group Permission Info (getGroupPermissionInfoById)  # noqa: E501

        Fetch the Group Permission Info object based on the provided Group Permission Id and the flag that controls what additional information to load: User or Entity Group. Group permission entity represents list of allowed operations for certain User Group to perform against certain Entity Group. Basically, this entity wires three other entities:    * Role that defines set of allowed operations;  * User Group that defines set of users who may perform the operations;   * Entity Group that defines set of entities which will be accessible to users;   Group Permission Info object extends the Group Permissions with the full information about Role and User and/or Entity Groups.  Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_group_permission_info_by_id_using_get_with_http_info(group_permission_id, is_user_group, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_permission_id: A string value representing the group permission id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param bool is_user_group: Load additional information about User('true') or Entity Group('false). (required)
        :return: GroupPermissionInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_permission_id', 'is_user_group']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_group_permission_info_by_id_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_permission_id' is set
        if ('group_permission_id' not in params or
                params['group_permission_id'] is None):
            raise ValueError("Missing the required parameter `group_permission_id` when calling `get_group_permission_info_by_id_using_get`")  # noqa: E501
        # verify the required parameter 'is_user_group' is set
        if ('is_user_group' not in params or
                params['is_user_group'] is None):
            raise ValueError("Missing the required parameter `is_user_group` when calling `get_group_permission_info_by_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_permission_id' in params:
            path_params['groupPermissionId'] = params['group_permission_id']  # noqa: E501

        query_params = []
        if 'is_user_group' in params:
            query_params.append(('isUserGroup', params['is_user_group']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/groupPermission/info/{groupPermissionId}{?isUserGroup}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GroupPermissionInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_group_permissions_using_get(self, user_group_id, **kwargs):  # noqa: E501
        """Get group permissions by User Group Id (getUserGroupPermissions)  # noqa: E501

        Returns a list of group permission objects that belongs to specified User Group Id. Group permission entity represents list of allowed operations for certain User Group to perform against certain Entity Group. Basically, this entity wires three other entities:    * Role that defines set of allowed operations;  * User Group that defines set of users who may perform the operations;   * Entity Group that defines set of entities which will be accessible to users;   Group Permission Info object extends the Group Permissions with the full information about Role and User and/or Entity Groups.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_group_permissions_using_get(user_group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_group_id: A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: list[GroupPermissionInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_group_permissions_using_get_with_http_info(user_group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_group_permissions_using_get_with_http_info(user_group_id, **kwargs)  # noqa: E501
            return data

    def get_user_group_permissions_using_get_with_http_info(self, user_group_id, **kwargs):  # noqa: E501
        """Get group permissions by User Group Id (getUserGroupPermissions)  # noqa: E501

        Returns a list of group permission objects that belongs to specified User Group Id. Group permission entity represents list of allowed operations for certain User Group to perform against certain Entity Group. Basically, this entity wires three other entities:    * Role that defines set of allowed operations;  * User Group that defines set of users who may perform the operations;   * Entity Group that defines set of entities which will be accessible to users;   Group Permission Info object extends the Group Permissions with the full information about Role and User and/or Entity Groups.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_user_group_permissions_using_get_with_http_info(user_group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_group_id: A string value representing the Entity Group Id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: list[GroupPermissionInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_group_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_group_permissions_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_group_id' is set
        if ('user_group_id' not in params or
                params['user_group_id'] is None):
            raise ValueError("Missing the required parameter `user_group_id` when calling `get_user_group_permissions_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_group_id' in params:
            path_params['userGroupId'] = params['user_group_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/userGroup/{userGroupId}/groupPermissions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GroupPermissionInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def load_user_group_permission_infos_using_post(self, **kwargs):  # noqa: E501
        """Load User Group Permissions (loadUserGroupPermissionInfos)  # noqa: E501

        Enrich a list of group permission objects with the information about Role, User and Entity Groups. Group permission entity represents list of allowed operations for certain User Group to perform against certain Entity Group. Basically, this entity wires three other entities:    * Role that defines set of allowed operations;  * User Group that defines set of users who may perform the operations;   * Entity Group that defines set of entities which will be accessible to users;   Group Permission Info object extends the Group Permissions with the full information about Role and User and/or Entity Groups.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.load_user_group_permission_infos_using_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[GroupPermission] body:
        :return: list[GroupPermissionInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.load_user_group_permission_infos_using_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.load_user_group_permission_infos_using_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def load_user_group_permission_infos_using_post_with_http_info(self, **kwargs):  # noqa: E501
        """Load User Group Permissions (loadUserGroupPermissionInfos)  # noqa: E501

        Enrich a list of group permission objects with the information about Role, User and Entity Groups. Group permission entity represents list of allowed operations for certain User Group to perform against certain Entity Group. Basically, this entity wires three other entities:    * Role that defines set of allowed operations;  * User Group that defines set of users who may perform the operations;   * Entity Group that defines set of entities which will be accessible to users;   Group Permission Info object extends the Group Permissions with the full information about Role and User and/or Entity Groups.    Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.load_user_group_permission_infos_using_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[GroupPermission] body:
        :return: list[GroupPermissionInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method load_user_group_permission_infos_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/userGroup/groupPermissions/info', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GroupPermissionInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def save_group_permission_using_post(self, **kwargs):  # noqa: E501
        """Create Or Update Group Permission (saveGroupPermission)  # noqa: E501

        Creates or Updates the Group Permission. When creating group permission, platform generates Group Permission Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Group Permission id will be present in the response. Specify existing Group Permission id to update the permission. Referencing non-existing Group Permission Id will cause 'Not Found' error.  Group permission entity represents list of allowed operations for certain User Group to perform against certain Entity Group. Basically, this entity wires three other entities:    * Role that defines set of allowed operations;  * User Group that defines set of users who may perform the operations;   * Entity Group that defines set of entities which will be accessible to users;   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_group_permission_using_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GroupPermission body:
        :return: GroupPermission
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_group_permission_using_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.save_group_permission_using_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def save_group_permission_using_post_with_http_info(self, **kwargs):  # noqa: E501
        """Create Or Update Group Permission (saveGroupPermission)  # noqa: E501

        Creates or Updates the Group Permission. When creating group permission, platform generates Group Permission Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Group Permission id will be present in the response. Specify existing Group Permission id to update the permission. Referencing non-existing Group Permission Id will cause 'Not Found' error.  Group permission entity represents list of allowed operations for certain User Group to perform against certain Entity Group. Basically, this entity wires three other entities:    * Role that defines set of allowed operations;  * User Group that defines set of users who may perform the operations;   * Entity Group that defines set of entities which will be accessible to users;   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_group_permission_using_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GroupPermission body:
        :return: GroupPermission
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_group_permission_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/groupPermission', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GroupPermission',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
