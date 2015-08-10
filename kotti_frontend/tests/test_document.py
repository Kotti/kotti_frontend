class TestHome:

    def test_public_document_anonymous(self, root, webtest, db_session):
        resp = webtest.get('/', status=404)
        # the document is private
        assert resp.status_code == 404
