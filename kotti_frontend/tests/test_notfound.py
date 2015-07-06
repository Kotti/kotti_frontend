class TestNotFound:

    def test_not_found_view_webtest(self, webtest):
        resp = webtest.get('/doesnotexists', status=404)
        assert resp.status_code == 404
        # TODO: fix me! assert 'kotti_frontend' in resp.body

    def test_not_found_view(self):
        from kotti_frontend.views.notfound import notfound_view
        from kotti.testing import DummyRequest
        dummy_request = DummyRequest()
        notfound_view(dummy_request)

        assert dummy_request.response.status == '404 Not Found'
