from django import views
from django.http import HttpRequest
from django.shortcuts import render

from submit.models import Guess
from mark.tasks import request_marking_guess

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
        request_marking_guess.delay({ 'guess_id': kwargs['guess_id'] })

        guess = Guess.objects.get(id=kwargs['guess_id'])
        context = {
            'guess': guess,
            'question': guess.question,
        }

        return render(request, '../templates/guess_result.html', context)