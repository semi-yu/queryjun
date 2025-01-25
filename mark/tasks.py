from __future__ import absolute_import, unicode_literals

from celery import shared_task

from question.models import Question
from mark.models import Guess

from mark.views.fetcher_vendor_determiner_service import FetcherVendorDeterminerService
from mark.views.comparer_mapper import ComparerMapper
from mark.views.marking_service_mapper import MarkingServiceMapper


@shared_task
def request_marking_guess(json):
    guess = Guess.objects.get(id=json['guess_id'])
    question = Question.objects.get(id=guess.question_id)

    fetcher = FetcherVendorDeterminerService.determine(guess)
    comparer = ComparerMapper.determine(fetcher, question)

    MarkingServiceMapper.determine(fetcher, comparer, guess).mark()