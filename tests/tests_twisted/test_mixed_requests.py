from scrapy import Spider
from scrapy.http import Request, Response
from scrapy.utils.test import get_crawler
from twisted.internet import defer
from twisted.trial.unittest import TestCase

from scrapy_botright.handler import ScrapyBotrightDownloadHandler
from tests.mockserver import StaticMockServer


class MixedRequestsTestCase(TestCase):
    """
    This test case ensures the handler's 'download_request' method works as expected, and
    non-playwright requests are processed correctly. The rest of the tests directly call
    '_download_request', which is a coroutine ('download_request' returns a Deferred).
    """

    @defer.inlineCallbacks
    def setUp(self):
        self.server = StaticMockServer()
        self.server.__enter__()
        self.handler = ScrapyBotrightDownloadHandler.from_crawler(get_crawler())
        yield self.handler._engine_started()

    @defer.inlineCallbacks
    def tearDown(self):
        self.server.__exit__(None, None, None)
        yield self.handler.close()

    def test_regular_request(self):
        def _test(response):
            self.assertIsInstance(response, Response)
            self.assertEqual(response.css("a::text").getall(), ["Lorem Ipsum", "Infinite Scroll"])
            self.assertEqual(response.url, request.url)
            self.assertEqual(response.status, 200)
            self.assertNotIn("playwright", response.flags)

        request = Request(self.server.urljoin("/index.html"))
        return self.handler.download_request(request, Spider("foo")).addCallback(_test)

    def test_playwright_request(self):
        def _test(response):
            self.assertIsInstance(response, Response)
            self.assertEqual(response.css("a::text").getall(), ["Lorem Ipsum", "Infinite Scroll"])
            self.assertEqual(response.url, request.url)
            self.assertEqual(response.status, 200)
            self.assertIn("playwright", response.flags)

        request = Request(self.server.urljoin("/index.html"), meta={"playwright": True})
        return self.handler.download_request(request, Spider("foo")).addCallback(_test)
