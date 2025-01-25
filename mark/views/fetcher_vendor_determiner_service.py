from .database_fetcher import DatabaseFetcher, PostgresqlFetcher
from submit.models import Guess

class FetcherVendorDeterminerService(object):
    @classmethod
    def determine_vendor(cls, guess: Guess) -> DatabaseFetcher:
        vendor_name = guess.selected_vendor.system_name

        if vendor_name == 'postgresql':
            return PostgresqlFetcher(guess)
        
        raise Exception('No existing vendor name')