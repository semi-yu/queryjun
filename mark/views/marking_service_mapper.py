from mark.models import Guess

from mark.views.marking_service import DefaultMarkingService
from mark.views.fetchers.database_fetcher import DatabaseFetcher
from mark.views.comparer import DefaultComparer

class MarkingServiceMapper:
    @classmethod
    def determine(cls, fetcher: DatabaseFetcher, comparer: DefaultComparer, guess: Guess):
        return DefaultMarkingService(fetcher, comparer, guess)
