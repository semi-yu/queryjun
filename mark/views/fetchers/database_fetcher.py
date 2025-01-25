from submit.models import Guess

class DatabaseFetcher:
    """
        An interface for Database access
    """
    def __init__(self, guess: Guess):
        """

        """
        raise NotImplementedError()
    
    def execute_guess(self) -> list[tuple]:
        """
            Execute the given query & fetch result from database
            :param guess: source of guessed query
        """
        raise NotImplementedError()

    def time(self) -> None | float: 
        """
            Return a query execution time
        """
        raise NotImplementedError()
    
    def result(self) -> None | list[tuple[str | float | int]]:
        """
            Return a fetched result after executing a query
        """
        raise NotImplementedError()
    
    def is_query_overtime(self) -> bool:
        """
            True if query executing time has surpassed its limit
        """
        raise NotImplementedError()
    
    def has_query_exception(self) -> bool:
        """
            True if query have problem executed in DBMS
        """
        raise NotImplementedError()
    
    def query_exception(self) -> str:
        """
            Get query exception hints
        """
        raise NotImplementedError()
