from unittest import mock

from django.http.request import QueryDict
from whatwasthatbookcalled.books.templatetags.query_transform import query_transform
from django.test import TestCase
from datetime import datetime, timezone
from pytz import utc
from whatwasthatbookcalled.books.templatetags.custom_timesince import custom_timesince


class CustomTimesinceTest(TestCase):
    def test_WhenMoreThanAYearAgo_DoesNotContainComma(self):
        date = utc.localize(datetime(2020, 8, 14, 12, 12, 12))
        result = custom_timesince(date)
        self.assertTrue("," not in result)

    def test_WhenNow_ReturnsJustNow(self):
        date = datetime.now(timezone.utc)
        result = custom_timesince(date)
        self.assertEqual(result, "just now")


class QueryTransformTest(TestCase):
    def test_WhenNewQuery_AddToQueries(self):
        m = mock.Mock()
        m.GET = QueryDict("key=value")
        context = {"request": m}
        self.assertEqual(query_transform(context, foo="bar"), "key=value&foo=bar")
