import typing
from functools import lru_cache

import allure
from httpx import Client as HttpxClient
from httpx import Response
from httpx._client import UseClientDefault
from httpx._types import (AuthTypes, CookieTypes, HeaderTypes, QueryParamTypes,
                          RequestContent, RequestData, RequestExtensions,
                          RequestFiles, TimeoutTypes, URLTypes)

from base.api.authentication_api import get_auth_token
from models.authentication import Authentication
from settings import base_settings


class Client(HttpxClient):
    @allure.step('Making GET request to "{url}"')
    def get(
        self,
        url: URLTypes,
        *,
        params: typing.Optional[QueryParamTypes] = None,
        headers: typing.Optional[HeaderTypes] = None,
        cookies: typing.Optional[CookieTypes] = None,
        auth: typing.Union[AuthTypes, UseClientDefault] = None,
        follow_redirects: typing.Union[bool, UseClientDefault] = None,
        timeout: typing.Union[TimeoutTypes, UseClientDefault] = None,
        extensions: typing.Optional[RequestExtensions] = None
    ) -> Response:
        return super().get(
            url=url,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
            follow_redirects=follow_redirects,
            timeout=timeout,
            extensions=extensions
        )

    @allure.step('Making POST request to "{url}"')
    def post(
        self,
        url: URLTypes,
        *,
        content: typing.Optional[RequestContent] = None,
        data: typing.Optional[RequestData] = None,
        files: typing.Optional[RequestFiles] = None,
        json: typing.Optional[typing.Any] = None,
        params: typing.Optional[QueryParamTypes] = None,
        headers: typing.Optional[HeaderTypes] = None,
        cookies: typing.Optional[CookieTypes] = None,
        auth: typing.Union[AuthTypes, UseClientDefault] = None,
        follow_redirects: typing.Union[bool, UseClientDefault] = None,
        timeout: typing.Union[TimeoutTypes, UseClientDefault] = None,
        extensions: typing.Optional[RequestExtensions] = None
    ) -> Response:
        return super().post(
            url=url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
            follow_redirects=follow_redirects,
            timeout=timeout,
            extensions=extensions
        )

    @allure.step('Making PATCH request to "{url}"')
    def patch(
        self,
        url: URLTypes,
        *,
        content: typing.Optional[RequestContent] = None,
        data: typing.Optional[RequestData] = None,
        files: typing.Optional[RequestFiles] = None,
        json: typing.Optional[typing.Any] = None,
        params: typing.Optional[QueryParamTypes] = None,
        headers: typing.Optional[HeaderTypes] = None,
        cookies: typing.Optional[CookieTypes] = None,
        auth: typing.Union[AuthTypes, UseClientDefault] = None,
        follow_redirects: typing.Union[bool, UseClientDefault] = None,
        timeout: typing.Union[TimeoutTypes, UseClientDefault] = None,
        extensions: typing.Optional[RequestExtensions] = None
    ) -> Response:
        return super().patch(
            url=url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
            follow_redirects=follow_redirects,
            timeout=timeout,
            extensions=extensions
        )

    @allure.step('Making DELETE request to "{url}"')
    def delete(
        self,
        url: URLTypes,
        *,
        params: typing.Optional[QueryParamTypes] = None,
        headers: typing.Optional[HeaderTypes] = None,
        cookies: typing.Optional[CookieTypes] = None,
        auth: typing.Union[AuthTypes, UseClientDefault] = None,
        follow_redirects: typing.Union[bool, UseClientDefault] = None,
        timeout: typing.Union[TimeoutTypes, UseClientDefault] = None,
        extensions: typing.Optional[RequestExtensions] = None
    ) -> Response:
        return super().delete(
            url=url,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
            follow_redirects=follow_redirects,
            timeout=timeout,
            extensions=extensions
        )


@lru_cache(maxsize=None)
def get_client(
    auth: Authentication | None = None,
    base_url: str = base_settings.api_url
) -> Client:
    headers: dict[str, str] = {}

    if auth is None:
        return Client(base_url=base_url, trust_env=True)

    if (not auth.auth_token) and (not auth.user):
        raise NotImplementedError(
            'Please provide "username" and "password" or "auth_token"'
        )

    if (not auth.auth_token) and auth.user:
        token = get_auth_token(auth.user)
        headers = {**headers, 'Authorization': f'Token {token}'}

    if auth.auth_token and (not auth.user):
        headers = {**headers, 'Authorization': f'Token {auth.auth_token}'}

    return Client(base_url=base_url, headers=headers, trust_env=True)
