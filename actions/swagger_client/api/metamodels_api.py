# coding: utf-8

"""
    CyberProof Platform Backend API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.3.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class MetamodelsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def copy_metamodel(self, id, body, **kwargs):  # noqa: E501
        """Copy metamodel  # noqa: E501

        Copy default metamodel to organization  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.copy_metamodel(id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Metamodel ID (required)
        :param Body9 body: (required)
        :param str authorization:
        :param str set_cookie:
        :return: Metamodel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.copy_metamodel_with_http_info(id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.copy_metamodel_with_http_info(id, body, **kwargs)  # noqa: E501
            return data

    def copy_metamodel_with_http_info(self, id, body, **kwargs):  # noqa: E501
        """Copy metamodel  # noqa: E501

        Copy default metamodel to organization  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.copy_metamodel_with_http_info(id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Metamodel ID (required)
        :param Body9 body: (required)
        :param str authorization:
        :param str set_cookie:
        :return: Metamodel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body', 'authorization', 'set_cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method copy_metamodel" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `copy_metamodel`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `copy_metamodel`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'set_cookie' in params:
            header_params['Set-Cookie'] = params['set_cookie']  # noqa: E501

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
        auth_settings = ['API key']  # noqa: E501

        return self.api_client.call_api(
            '/metamodel/{id}/copy', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Metamodel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def count_metamodels(self, **kwargs):  # noqa: E501
        """Count metamodels  # noqa: E501

        Count total number of metamodels  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.count_metamodels(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str where:
        :param str organization:
        :param str authorization:
        :param str set_cookie:
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.count_metamodels_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.count_metamodels_with_http_info(**kwargs)  # noqa: E501
            return data

    def count_metamodels_with_http_info(self, **kwargs):  # noqa: E501
        """Count metamodels  # noqa: E501

        Count total number of metamodels  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.count_metamodels_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str where:
        :param str organization:
        :param str authorization:
        :param str set_cookie:
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['where', 'organization', 'authorization', 'set_cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method count_metamodels" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'where' in params:
            query_params.append(('where', params['where']))  # noqa: E501
        if 'organization' in params:
            query_params.append(('organization', params['organization']))  # noqa: E501

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'set_cookie' in params:
            header_params['Set-Cookie'] = params['set_cookie']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API key']  # noqa: E501

        return self.api_client.call_api(
            '/metamodel/count', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_metamodel(self, body, **kwargs):  # noqa: E501
        """Create metamodel  # noqa: E501

        Create a new item  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_metamodel(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Metamodel body: (required)
        :param str authorization:
        :param str set_cookie:
        :return: Metamodel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_metamodel_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_metamodel_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_metamodel_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create metamodel  # noqa: E501

        Create a new item  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_metamodel_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Metamodel body: (required)
        :param str authorization:
        :param str set_cookie:
        :return: Metamodel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'authorization', 'set_cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_metamodel" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_metamodel`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'set_cookie' in params:
            header_params['Set-Cookie'] = params['set_cookie']  # noqa: E501

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
        auth_settings = ['API key']  # noqa: E501

        return self.api_client.call_api(
            '/metamodel', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Metamodel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_metamodel(self, id, **kwargs):  # noqa: E501
        """Get metamodel  # noqa: E501

        Get one metamodel  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_metamodel(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Metamodel ID (required)
        :param str authorization:
        :param str set_cookie:
        :return: list[Metamodel]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_metamodel_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_metamodel_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_metamodel_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get metamodel  # noqa: E501

        Get one metamodel  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_metamodel_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Metamodel ID (required)
        :param str authorization:
        :param str set_cookie:
        :return: list[Metamodel]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'authorization', 'set_cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_metamodel" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_metamodel`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'set_cookie' in params:
            header_params['Set-Cookie'] = params['set_cookie']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API key']  # noqa: E501

        return self.api_client.call_api(
            '/metamodel/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Metamodel]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_metamodel_names(self, **kwargs):  # noqa: E501
        """Get metamodel names  # noqa: E501

        Get list of metamodel names  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_metamodel_names(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization:
        :param str set_cookie:
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_metamodel_names_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_metamodel_names_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_metamodel_names_with_http_info(self, **kwargs):  # noqa: E501
        """Get metamodel names  # noqa: E501

        Get list of metamodel names  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_metamodel_names_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization:
        :param str set_cookie:
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'set_cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_metamodel_names" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'set_cookie' in params:
            header_params['Set-Cookie'] = params['set_cookie']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API key']  # noqa: E501

        return self.api_client.call_api(
            '/metamodel/modelNames', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_metamodels(self, **kwargs):  # noqa: E501
        """Get metamodels  # noqa: E501

        Get list of metamodels  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_metamodels(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str where:
        :param str sort:
        :param int limit:
        :param int skip:
        :param str organization:
        :param str authorization:
        :param str set_cookie:
        :return: list[Metamodel]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_metamodels_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_metamodels_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_metamodels_with_http_info(self, **kwargs):  # noqa: E501
        """Get metamodels  # noqa: E501

        Get list of metamodels  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_metamodels_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str where:
        :param str sort:
        :param int limit:
        :param int skip:
        :param str organization:
        :param str authorization:
        :param str set_cookie:
        :return: list[Metamodel]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['where', 'sort', 'limit', 'skip', 'organization', 'authorization', 'set_cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_metamodels" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'where' in params:
            query_params.append(('where', params['where']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'organization' in params:
            query_params.append(('organization', params['organization']))  # noqa: E501

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'set_cookie' in params:
            header_params['Set-Cookie'] = params['set_cookie']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API key']  # noqa: E501

        return self.api_client.call_api(
            '/metamodel', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Metamodel]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_metamodel(self, id, **kwargs):  # noqa: E501
        """Remove metamodel  # noqa: E501

        Remove existing metamodel  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_metamodel(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Metamodel ID (required)
        :param str authorization:
        :param str set_cookie:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_metamodel_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_metamodel_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def remove_metamodel_with_http_info(self, id, **kwargs):  # noqa: E501
        """Remove metamodel  # noqa: E501

        Remove existing metamodel  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_metamodel_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Metamodel ID (required)
        :param str authorization:
        :param str set_cookie:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'authorization', 'set_cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_metamodel" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_metamodel`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'set_cookie' in params:
            header_params['Set-Cookie'] = params['set_cookie']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['API key']  # noqa: E501

        return self.api_client.call_api(
            '/metamodel/{id}', 'DELETE',
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

    def update_metamodel(self, id, body, **kwargs):  # noqa: E501
        """Update metamodel  # noqa: E501

        Update an existing metamodel  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_metamodel(id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Metamodel ID (required)
        :param Metamodel body: (required)
        :param str authorization:
        :param str set_cookie:
        :return: Metamodel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_metamodel_with_http_info(id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_metamodel_with_http_info(id, body, **kwargs)  # noqa: E501
            return data

    def update_metamodel_with_http_info(self, id, body, **kwargs):  # noqa: E501
        """Update metamodel  # noqa: E501

        Update an existing metamodel  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_metamodel_with_http_info(id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Metamodel ID (required)
        :param Metamodel body: (required)
        :param str authorization:
        :param str set_cookie:
        :return: Metamodel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body', 'authorization', 'set_cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_metamodel" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_metamodel`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_metamodel`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'set_cookie' in params:
            header_params['Set-Cookie'] = params['set_cookie']  # noqa: E501

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
        auth_settings = ['API key']  # noqa: E501

        return self.api_client.call_api(
            '/metamodel/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Metamodel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
