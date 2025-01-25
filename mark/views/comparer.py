from question.models import Question
from .database_fetcher import DatabaseFetcher

class DefaultComparer:
    """
        Service layer module for comparing question answer and its guessing query
    """
    def __init__(self, database_fetcher: DatabaseFetcher, question: Question):
        """
        :param question:
        :param database_fetcher:
        """
        self.question = question
        self.database_fetcher = database_fetcher

    def is_match(self) -> bool:
        """
            Compare a query result and answer
        """
        return self.clean_guess() == self.clean_answer()

    def clean_guess(self) -> str:
        """
            Get a string from query result
        """
        return str(self.database_fetcher.result())
    
    def clean_answer(self) -> str:
        """
            Get a answer string from quetion
        """
        return self.question.answer