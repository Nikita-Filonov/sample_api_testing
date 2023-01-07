from enum import Enum


class APIRoutes(str, Enum):
    AUTH = '/auth'
    INFO = '/info'
    CAST = '/cast'
    EPISODES = '/episodes'
    QUESTIONS = '/questions'
    INVENTORY = '/inventory'
    CHARACTERS = '/characters'

    def __str__(self) -> str:
        return self.value
