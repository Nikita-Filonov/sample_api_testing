from typing import TypedDict

from pydantic import BaseModel, Field, RootModel

from utils.fakers import random_list_of_strings, random_number, random_string


class UpdateQuestion(BaseModel):
    question: str | None = Field(default_factory=random_string)
    possible_answers: list[str] | None = Field(
        alias='possibleAnswers',
        default_factory=random_list_of_strings
    )
    correct_answer: str | None = Field(
        alias='correctAnswer',
        default_factory=random_string
    )


class DefaultQuestion(BaseModel):
    id: int = Field(default_factory=random_number)
    question: str = Field(default_factory=random_string)
    possible_answers: list[str] = Field(
        alias='possibleAnswers',
        default_factory=random_list_of_strings
    )
    correct_answer: str | int = Field(
        alias='correctAnswer',
        default_factory=random_string
    )


class DefaultQuestionsList(RootModel):
    root: list[DefaultQuestion]


class QuestionDict(TypedDict):
    id: int
    question: str
    correctAnswer: str
    possibleAnswers: list[str]
