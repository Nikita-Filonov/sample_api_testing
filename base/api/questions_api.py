import allure
from httpx import Response

from base.client import get_client
from models.authentication import Authentication
from models.questions import DefaultQuestion, UpdateQuestion
from utils.constants.routes import APIRoutes


@allure.step(f'Getting all questions')
def get_questions_api(auth: Authentication = Authentication()) -> Response:
    client = get_client(auth=auth)
    return client.get(APIRoutes.QUESTIONS)


@allure.step('Getting question with id "{question_id}"')
def get_question_api(
    question_id: int,
    auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    return client.get(f'{APIRoutes.QUESTIONS}/{question_id}')


@allure.step('Creating question')
def create_question_api(
    payload: DefaultQuestion,
    auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    return client.post(APIRoutes.QUESTIONS, json=payload.dict(by_alias=True))


@allure.step('Updating question with id "{question_id}"')
def update_question_api(
    question_id: int,
    payload: UpdateQuestion,
    auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    return client.patch(
        f'{APIRoutes.QUESTIONS}/{question_id}',
        json=payload.dict(by_alias=True)
    )


@allure.step('Deleting question with id "{question_id}"')
def delete_question_api(
    question_id: int,
    auth: Authentication = Authentication()
) -> Response:
    client = get_client(auth=auth)
    return client.delete(f'{APIRoutes.QUESTIONS}/{question_id}')


def create_question(auth: Authentication = Authentication()) -> DefaultQuestion:
    payload = DefaultQuestion()

    response = create_question_api(payload=payload, auth=auth)
    return DefaultQuestion(**response.json())
