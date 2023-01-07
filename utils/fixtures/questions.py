import pytest

from base.api.questions_api import create_question, delete_question_api
from models.questions import DefaultQuestion


@pytest.fixture(scope='function')
def function_question() -> DefaultQuestion:
    question = create_question()
    yield question

    delete_question_api(question.id)
