from question.models import Question

from mark.views.comparer import DefaultComparer
from mark.views.fetchers.database_fetcher import DatabaseFetcher

class ComparerMapper:
    @classmethod
    def determine(cls, fetcher: DatabaseFetcher, question: Question):
        return DefaultComparer(fetcher, question)

        raise Exception('No valid comparer')