from typing import TypeVar

import allure

from utils.assertions.base.assertion_mixin import AssertionMixin

T = TypeVar('T')


def expect(expected: T) -> AssertionMixin:
    assertion = AssertionMixin(expected=expected)
    assertion.step_provider = allure.step

    return assertion
