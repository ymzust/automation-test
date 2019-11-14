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


class SearchApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def global_search(self, search, **kwargs):  # noqa: E501
        """Global search  # noqa: E501

        Global search  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.global_search(search, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search: Search query (required)
        :param str where:
        :param int limit:
        :param int skip:
        :param str authorization:
        :param str set_cookie:
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.global_search_with_http_info(search, **kwargs)  # noqa: E501
        else:
            (data) = self.global_search_with_http_info(search, **kwargs)  # noqa: E501
            return data

    def global_search_with_http_info(self, search, **kwargs):  # noqa: E501
        """Global search  # noqa: E501

        Global search  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.global_search_with_http_info(search, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search: Search query (required)
        :param str where:
        :param int limit:
        :param int skip:
        :param str authorization:
        :param str set_cookie:
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search', 'where', 'limit', 'skip', 'authorization', 'set_cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method global_search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search' is set
        if ('search' not in params or
                params['search'] is None):
            raise ValueError("Missing the required parameter `search` when calling `global_search`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501
        if 'where' in params:
            query_params.append(('where', params['where']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501

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
            '/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20012',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_alerts(self, **kwargs):  # noqa: E501
        """Search alerts  # noqa: E501

        Note that this list includes arhived and irrelevant alets, unlike default GET request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_alerts(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search:
        :param str where:
        :param str sort:
        :param int limit:
        :param int skip:
        :param str select:
        :param str authorization:
        :param str set_cookie:
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_alerts_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_alerts_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_alerts_with_http_info(self, **kwargs):  # noqa: E501
        """Search alerts  # noqa: E501

        Note that this list includes arhived and irrelevant alets, unlike default GET request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_alerts_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search:
        :param str where:
        :param str sort:
        :param int limit:
        :param int skip:
        :param str select:
        :param str authorization:
        :param str set_cookie:
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search', 'where', 'sort', 'limit', 'skip', 'select', 'authorization', 'set_cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_alerts" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501
        if 'where' in params:
            query_params.append(('where', params['where']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'select' in params:
            query_params.append(('select', params['select']))  # noqa: E501

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
            '/alert/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_incidents(self, **kwargs):  # noqa: E501
        """Search incidents  # noqa: E501

        Full text search within incidents. Note that list include arhived and closed incidents, unlike default GET request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_incidents(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search:
        :param str where:
        :param str sort:
        :param int limit:
        :param int skip:
        :param str authorization:
        :param str set_cookie:
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_incidents_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_incidents_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_incidents_with_http_info(self, **kwargs):  # noqa: E501
        """Search incidents  # noqa: E501

        Full text search within incidents. Note that list include arhived and closed incidents, unlike default GET request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_incidents_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search:
        :param str where:
        :param str sort:
        :param int limit:
        :param int skip:
        :param str authorization:
        :param str set_cookie:
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search', 'where', 'sort', 'limit', 'skip', 'authorization', 'set_cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_incidents" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501
        if 'where' in params:
            query_params.append(('where', params['where']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501

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
            '/incident/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2006',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_messages(self, **kwargs):  # noqa: E501
        """Search messages  # noqa: E501

        Full text search within messages. Note that list includes archived and deleted messages, unlike default GET request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_messages(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search:
        :param str sort:
        :param int limit:
        :param int skip:
        :param str authorization:
        :param str set_cookie:
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_messages_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_messages_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_messages_with_http_info(self, **kwargs):  # noqa: E501
        """Search messages  # noqa: E501

        Full text search within messages. Note that list includes archived and deleted messages, unlike default GET request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_messages_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search:
        :param str sort:
        :param int limit:
        :param int skip:
        :param str authorization:
        :param str set_cookie:
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search', 'sort', 'limit', 'skip', 'authorization', 'set_cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_messages" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501

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
            '/message/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2007',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_observables(self, **kwargs):  # noqa: E501
        """Search observables  # noqa: E501

        Note that this list includes arhived observables, unlike default GET request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_observables(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search:
        :param str sort:
        :param int limit:
        :param int skip:
        :param str authorization:
        :param str set_cookie:
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_observables_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_observables_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_observables_with_http_info(self, **kwargs):  # noqa: E501
        """Search observables  # noqa: E501

        Note that this list includes arhived observables, unlike default GET request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_observables_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search:
        :param str sort:
        :param int limit:
        :param int skip:
        :param str authorization:
        :param str set_cookie:
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search', 'sort', 'limit', 'skip', 'authorization', 'set_cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_observables" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501

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
            '/observable/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2004',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def tags_suggest(self, query, **kwargs):  # noqa: E501
        """Tags suggest  # noqa: E501

        Tags search, used in autocomplete  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tags_suggest(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str query: Case-insensitive search by tag value (required)
        :param str organization:
        :param str where:
        :param str sort:
        :param str limit:
        :param str skip:
        :param str select:
        :param str authorization:
        :param str set_cookie:
        :return: list[Tag]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.tags_suggest_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.tags_suggest_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def tags_suggest_with_http_info(self, query, **kwargs):  # noqa: E501
        """Tags suggest  # noqa: E501

        Tags search, used in autocomplete  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tags_suggest_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str query: Case-insensitive search by tag value (required)
        :param str organization:
        :param str where:
        :param str sort:
        :param str limit:
        :param str skip:
        :param str select:
        :param str authorization:
        :param str set_cookie:
        :return: list[Tag]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'organization', 'where', 'sort', 'limit', 'skip', 'select', 'authorization', 'set_cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tags_suggest" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if ('query' not in params or
                params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `tags_suggest`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'organization' in params:
            query_params.append(('organization', params['organization']))  # noqa: E501
        if 'where' in params:
            query_params.append(('where', params['where']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'select' in params:
            query_params.append(('select', params['select']))  # noqa: E501

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
            '/tag/suggest', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Tag]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def users_suggest(self, query, **kwargs):  # noqa: E501
        """Users suggest  # noqa: E501

        Users autocomplete  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.users_suggest(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str query: Search query. Can contain displayName or fullName. (required)
        :param int limit: Number or results
        :param str organization: Filter by organization id
        :param str authorization:
        :param str set_cookie:
        :return: list[InlineResponse2009]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.users_suggest_with_http_info(query, **kwargs)  # noqa: E501
        else:
            (data) = self.users_suggest_with_http_info(query, **kwargs)  # noqa: E501
            return data

    def users_suggest_with_http_info(self, query, **kwargs):  # noqa: E501
        """Users suggest  # noqa: E501

        Users autocomplete  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.users_suggest_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str query: Search query. Can contain displayName or fullName. (required)
        :param int limit: Number or results
        :param str organization: Filter by organization id
        :param str authorization:
        :param str set_cookie:
        :return: list[InlineResponse2009]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'limit', 'organization', 'authorization', 'set_cookie']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method users_suggest" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if ('query' not in params or
                params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `users_suggest`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
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
            '/user/suggest', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InlineResponse2009]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
