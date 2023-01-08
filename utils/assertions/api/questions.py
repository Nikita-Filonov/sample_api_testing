from models.questions import DefaultQuestion, QuestionDict, UpdateQuestion
from utils.assertions.base.expect import expect


def assert_question(
    expected_question: QuestionDict,
    actual_question: DefaultQuestion | UpdateQuestion
):
    if isinstance(actual_question, DefaultQuestion):
        expect(expected_question['id']) \
            .set_description('Question "id"')\
            .to_be_equal(actual_question.id)

    expect(expected_question['question']) \
        .set_description('Question "question"') \
        .to_be_equal(actual_question.question)

    expect(expected_question['possibleAnswers']) \
        .set_description('Question "possibleAnswers"') \
        .to_be_equal(actual_question.possible_answers)

    expect(expected_question['correctAnswer']) \
        .set_description('Question "correctAnswer"') \
        .to_be_equal(actual_question.correct_answer)
