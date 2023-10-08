import pytest

from base.api.questions_api import QuestionsClient
from models.authentication import Authentication
from models.questions import DefaultQuestion
from utils.clients.http.builder import get_http_client


@pytest.fixture(scope="class")
def class_questions_client() -> QuestionsClient:
    client = get_http_client(auth=Authentication())

    return QuestionsClient(client=client)


@pytest.fixture(scope='function')
def function_question(class_questions_client: QuestionsClient) -> DefaultQuestion:
    question = class_questions_client.create_question()
    yield question

    class_questions_client.delete_question_api(question.id)
