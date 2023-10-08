from httpx import Response

from models.authentication import AuthUser
from utils.clients.http.client import APIClient
from utils.constants.routes import APIRoutes


class AuthenticationClient(APIClient):
    def get_auth_token_api(self, payload: AuthUser) -> Response:
        return self.client.post(f'{APIRoutes.AUTH}/token', json=payload.model_dump())

    def get_auth_token(self, payload: AuthUser) -> str:
        """
        Should be used like this:

        response = self.get_auth_token_api(payload)
        json_response = response.json()

        assert response.status_code == HTTPStatus.OK
        assert json_response.get('token')

        return json_response['token']
        """
        return 'token'
