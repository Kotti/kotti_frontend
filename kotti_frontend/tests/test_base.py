class TestApp:

    def required_settings(self):
        from kotti.testing import testing_db_url
        return {'sqlalchemy.url': testing_db_url(),
                'kotti.secret': 'dude'}

    def test_base_configure_no_bind(self):
        # if you run the frontend as a standalone process
        # the DBSession should be initialized
        required_settings = self.required_settings()

        from kotti_frontend import main
        from kotti import DBSession
        from pytest import raises
        from sqlalchemy.exc import UnboundExecutionError
        from mock import patch
        with patch('kotti_frontend.DBSession') as DBSession:
            DBSession.get_bind.side_effect = UnboundExecutionError
            with patch('kotti_frontend.engine_from_config') as engine_from_config:
                with patch('kotti_frontend.initialize_sql') as initialize_sql:
                    main({}, **required_settings)
                    assert engine_from_config.called
                    assert initialize_sql.called
