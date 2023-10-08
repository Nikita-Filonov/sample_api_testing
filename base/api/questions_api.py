import allure
from httpx import Response

from models.questions import DefaultQuestion, UpdateQuestion
from utils.clients.http.client import APIClient
from utils.constants.routes import APIRoutes


class QuestionsClient(APIClient):
    @allure.step(f'Getting all questions')
    def get_questions_api(self) -> Response:
        return self.client.get(APIRoutes.QUESTIONS)

    @allure.step('Getting question with id "{question_id}"')
    def get_question_api(self, question_id: int) -> Response:
        return self.client.get(f'{APIRoutes.QUESTIONS}/{question_id}')

    @allure.step('Creating question')
    def create_question_api(self, payload: DefaultQuestion) -> Response:
        return self.client.post(APIRoutes.QUESTIONS, json=payload.dict(by_alias=True))

    @allure.step('Updating question with id "{question_id}"')
    def update_question_api(self, question_id: int, payload: UpdateQuestion) -> Response:
        return self.client.patch(
            f'{APIRoutes.QUESTIONS}/{question_id}',
            json=payload.dict(by_alias=True)
        )

    @allure.step('Deleting question with id "{question_id}"')
    def delete_question_api(self, question_id: int) -> Response:
        return self.client.delete(f'{APIRoutes.QUESTIONS}/{question_id}')

    def create_question(self) -> DefaultQuestion:
        payload = DefaultQuestion()

        response = self.create_question_api(payload)
        return DefaultQuestion(**response.json())
