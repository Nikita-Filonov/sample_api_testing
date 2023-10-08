from base.api.authentication_api import AuthenticationClient
from models.authentication import Authentication
from settings import base_settings
from utils.clients.http.client import HTTPClient


def get_http_client(
    auth: Authentication | None = None,
    base_url: str = base_settings.api_url
) -> HTTPClient:
    if auth is None:
        return HTTPClient(base_url=base_url, trust_env=True)

    headers: dict[str, str] = {}

    client = HTTPClient(base_url=base_settings.api_url)
    authentication_client = AuthenticationClient(client=client)

    if (not auth.auth_token) and auth.user:
        token = authentication_client.get_auth_token(auth.user)
        headers = {**headers, 'Authorization': f'Token {token}'}

    if auth.auth_token and (not auth.user):
        headers = {**headers, 'Authorization': f'Token {auth.auth_token}'}

    return HTTPClient(base_url=base_url, headers=headers, trust_env=True)
