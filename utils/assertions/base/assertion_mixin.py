from typing import TypeVar

from utils.assertions.base.assertion_base import AssertionBase
from utils.assertions.base.assertion_types import AssertionTypes

T = TypeVar('T')


class AssertionMixin(AssertionBase):

    def is_length(self, length: int):
        step_name = f'Checking that "{self._description}" has {length} length'
        with self.step_provider(step_name):

            if not hasattr(self.expected, '__len__'):
                raise NotImplementedError(
                    f'The expected value "{self.expected}" {type(self.expected)} has no length attribute'
                )

            template = self._error_template(length, AssertionTypes.LENGTH)
            assert length == len(self.expected), template

        return self

    def to_be_equal(self, actual: T):
        step_name = f'Checking that "{self._description}" equals to "{self.expected}"'
        with self.step_provider(step_name):
            template = self._error_template(actual, AssertionTypes.EQUAL)
            assert self.expected == actual, template

        return self

    def not_to_be_equal(self, actual: T):
        step_name = f'Checking that "{self._description}" not equals to "{self.expected}"'
        with self.step_provider(step_name):
            template = self._error_template(actual, AssertionTypes.NOT_EQUAL)
            assert self.expected != actual, template

        return self

    def in_(self, actual: T):
        step_name = f'Checking that "{self._description}" in "{self.expected}"'
        with self.step_provider(step_name):
            template = self._error_template(actual, AssertionTypes.IN_)
            assert self.expected != actual, template

        return self
