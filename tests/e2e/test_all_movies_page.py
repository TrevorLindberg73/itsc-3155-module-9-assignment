# TODO: Feature 1
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository
movie_repository = get_movie_repository()

def test_home_page(test_app: FlaskClient):
    # Create movies to be used in this test and get all movies.
    new_movie1 = movie_repository.create_movie("a","b", 1)
    new_movie2 = movie_repository.create_movie("c","d", 2)
    new_movie3 = movie_repository.create_movie("e","f", 3)
    response = test_app.get('/movies')
    response_data = response.data
    # Test Text
    assert b'<h1 class="mb-5">All Movies</h1>' in response_data
    assert b'<p class="mb-3">See our list of movie ratings below</p>' in response_data
    # Test Table Head
    assert b'<table style = "width:50%", border="2px solid black">' in response_data
    assert b'<tr style="outline: thin solid">' in response_data
    assert b'<th tr style="outline: thin solid">Movie Name</th>' in response_data
    assert b'<th tr style="outline: thin solid">Director</th>' in response_data
    assert b'<th tr style="outline: thin solid">Rating</th>' in response_data
    # Test Table Body
    assert b'<tr tr style="outline: thin solid">' in response_data
    assert b'<td tr style="outline: thin solid"> a </td>' in response_data
    assert b'<td tr style="outline: thin solid"> b </td>' in response_data
    assert b'<td tr style="outline: thin solid"> 1 </td>' in response_data
    assert b'<td tr style="outline: thin solid"> c </td>' in response_data
    assert b'<td tr style="outline: thin solid"> d </td>' in response_data
    assert b'<td tr style="outline: thin solid"> 2 </td>' in response_data
    assert b'<td tr style="outline: thin solid"> e </td>' in response_data
    assert b'<td tr style="outline: thin solid"> f </td>' in response_data
    assert b'<td tr style="outline: thin solid"> 3 </td>' in response_data