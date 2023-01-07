from http import HTTPStatus

from utils.assertions.base.expect import expect


def assert_status_code(actual: int, expected: HTTPStatus) -> None:
    expect(expected) \
        .to_be_equal(actual) \
        .set_description('Response status code')
