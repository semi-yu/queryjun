from ..models import GuessResult, ResultType, GuessResultError
from submit.models import Guess
from member.models import Member

from .database_fetcher import DatabaseFetcher
from .comparer import DefaultComparer

class DefaultMarkingService:
    """
        A service layer for query marking
    """
    def __init__(self, database_fetcher: DatabaseFetcher, comparer: DefaultComparer, guess: Guess):
        """
        :param guess:
        :param database_fetcher:
        :param comparer:
        """
        self.database_fetcher = database_fetcher
        self.comparer = comparer
        self.guess = guess

    def mark(self) -> None:
        """
            Practice total action of 'mark'
                - execute guessing query and fetch the result
                - decode result 
        """
        self.database_fetcher.execute_guess()
        
        result_type = self.decide_result_type()

        guess_result = GuessResult(
            total_execution_time = self.database_fetcher.time(),
            result=result_type,
            guess=self.guess
        )
        guess_result.save()

        if self.is_query_succeed(result_type):
            member = Member.objects.get(id=self.guess.submitter_id)
            member.solved_question.add(self.guess.question)
        elif self.has_query_exception(result_type):
            GuessResultError(
                exception_message=self.database_fetcher.query_exception(),
                guess_result=guess_result
            ).save()

    def decide_result_type(self) -> ResultType:
        """
            Decide which result type should be the guess's mark result
        """
        rto = ResultType.objects

        if self.database_fetcher.has_query_exception():
            return rto.get(result_acronym='ERR')
        elif self.database_fetcher.is_query_overtime():
            return rto.get(result_acronym='OVTM')
        elif not self.comparer.is_match():
            return rto.get(result_acronym='FL')
        else:
            return rto.get(result_acronym='CLR')

    def is_query_succeed(self, result_type) -> bool:
        return result_type == ResultType.objects.get(result_acronym='CLR')

    def has_query_exception(self, result_type) -> bool:
        return result_type == ResultType.objects.get(result_acronym='ERR')