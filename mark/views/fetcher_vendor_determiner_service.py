from submit.models import Guess

from mark.views.fetchers.database_fetcher import DatabaseFetcher
from mark.views.fetchers.postgresql_fetcher import PostgresqlFetcher

class FetcherVendorDeterminerService(object):
    @classmethod
    def determine(cls, guess: Guess) -> DatabaseFetcher:
        vendor_name = guess.selected_vendor.system_name

        if vendor_name == 'postgresql':
            return PostgresqlFetcher(guess)
        
        raise Exception('No existing vendor name')