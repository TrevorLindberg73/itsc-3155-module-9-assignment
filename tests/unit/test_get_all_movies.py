# TODO: Feature 1
from src.repositories.movie_repository import get_movie_repository
movie_repository = get_movie_repository()

def test_get_all_movies():
    # Movies are created in test all movies.
    movie_list = movie_repository.get_all_movies()
    # Check length
    assert(len(movie_list) == 3)
    # Ensure specific parts are correct.
    assert(movie_list[0].title == "a")
    assert(movie_list[0].director == "b")
    assert(movie_list[0].rating == 1)
    assert(movie_list[1].title == "c")
    assert(movie_list[1].director == "d")
    assert(movie_list[1].rating == 2)
    assert(movie_list[2].title == "e")
    assert(movie_list[2].director == "f")
    assert(movie_list[2].rating == 3)