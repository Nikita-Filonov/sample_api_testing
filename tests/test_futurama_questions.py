from http import HTTPStatus

import allure
import pytest

from base.api.questions_api import QuestionsClient
from models.questions import (DefaultQuestion, DefaultQuestionsList,
                              QuestionDict, UpdateQuestion)
from utils.assertions.api.questions import assert_question
from utils.assertions.base.solutions import assert_status_code
from utils.assertions.schema import validate_schema


@pytest.mark.questions
@allure.feature('Questions')
@allure.story('Questions API')
class TestQuestions:
    @allure.title('Get questions')
    def test_get_questions(self, function_questions_client: QuestionsClient):
        response = function_questions_client.get_questions_api()
        json_response: list[QuestionDict] = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_schema(json_response, DefaultQuestionsList.schema())

    @allure.title('Create question')
    def test_create_question(self, function_questions_client: QuestionsClient):
        payload = DefaultQuestion()

        response = function_questions_client.create_question_api(payload)
        json_response: QuestionDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_question(
            expected_question=json_response,
            actual_question=payload
        )

        validate_schema(json_response, DefaultQuestion.schema())

    @allure.title('Get question')
    def test_get_question(
        self,
        function_question: DefaultQuestion,
        function_questions_client: QuestionsClient
    ):
        response = function_questions_client.get_question_api(
            function_question.id
        )
        json_response: QuestionDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_question(
            expected_question=json_response,
            actual_question=function_question
        )

        validate_schema(json_response, DefaultQuestion.schema())

    @allure.title('Update question')
    def test_update_question(
        self,
        function_question: DefaultQuestion,
        function_questions_client: QuestionsClient
    ):
        payload = UpdateQuestion()

        response = function_questions_client.update_question_api(
            function_question.id, payload
        )
        json_response: QuestionDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_question(
            expected_question=json_response,
            actual_question=payload
        )

        validate_schema(json_response, DefaultQuestion.schema())

    @allure.title('Delete question')
    def test_delete_question(
        self,
        function_question: DefaultQuestion,
        function_questions_client: QuestionsClient
    ):
        delete_question_response = function_questions_client.delete_question_api(
            function_question.id
        )
        get_question_response = function_questions_client.get_question_api(
            function_question.id
        )

        assert_status_code(delete_question_response.status_code, HTTPStatus.OK)
        assert_status_code(
            get_question_response.status_code, HTTPStatus.NOT_FOUND
        )
