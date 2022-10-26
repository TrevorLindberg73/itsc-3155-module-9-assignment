# TODO: Feature 3
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

def test_get_movie_by_title():
    movie_repository = get_movie_repository()

    default1 = movie_repository.create_movie('Spiderman', 'Sam Raimi', 3)
    default2 = movie_repository.create_movie('Antman', 'Sammy Bammy', 5)
    assert type(default1) == Movie
    assert movie_repository.get_movie_by_title(default1) == 'Spiderman'
    assert movie_repository.get_movie_by_title(default2) == 'Antman'