# TODO: Feature 3
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository

# Still rather confused with e2e tests
def test_search_page(test_app: FlaskClient):
    responce = test_app.get('/movies/search')
    assert b'<p>The rating for that movie is {{ rating }}</p>' in responce.data