from django import views
from django.http import HttpRequest
from django.shortcuts import render

from submit.models import Guess

from .marking_service import DefaultMarkingService
from .fetcher_vendor_determiner_service import FetcherVendorDeterminerService
from .comparer import DefaultComparer

class MarkGuessView(views.View):
    """
        A CBV for marking gussed query and displaying guess result page
    """
    def get(self, request: HttpRequest, *args, **kwargs):
        """
            Returns guess-result page

            :param request:
            :param *args:
            :param **kwargs: 
        """
        guess = Guess.objects.get(id=kwargs['guess_id'])

        self.request_mark(guess)

        context = {
            'guess': guess,
            'question': guess.question,
        }

        return render(request, '../templates/guess_result.html', context)
    
    def request_mark(self, guess: Guess):
        """
            Make a marking request
        """
        database_fetcher = FetcherVendorDeterminerService.determine_vendor(guess)

        comparer = DefaultComparer(database_fetcher, guess.question)
        marking_service = DefaultMarkingService(database_fetcher, comparer, guess)

        marking_service.mark()

        # request_marking.delay()