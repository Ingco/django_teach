# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Question

# Create your tests here.


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        # Будущее время
        time = timezone.now() + datetime.timedelta(days=1)
        # Вопрос из будущего
        future_question = Question(pub_date=time)
        # Должнв получить False
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the old.
        """
        # Прошлое (больше дня) время
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        # Вопрос старше 1 дня
        old_question = Question(pub_date=time)
        # Должны вернуть False
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the recent.
        """
        # Прошлое время (не старше дня назад)
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        # Вопрос не старше 1 дня
        recent_question = Question(pub_date=time)
        # Должны вернуть True
        self.assertIs(recent_question.was_published_recently(), True)

