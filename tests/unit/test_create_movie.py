from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie
#Completed by Marcel Newman
def test_create_movie_GOOD():
    movie_repository = get_movie_repository()
    
    new_movie01 = movie_repository.create_movie("Micheal's First Scream", "Robert Upey", 5)
    new_movie02 = movie_repository.create_movie("Micheal's Second Horror", "Robert Upey", 1)
    assert type(new_movie01) == Movie
    assert new_movie01.director == "Robert Upey"
    assert new_movie01.rating == 5
    assert new_movie01.title == "Micheal's First Scream"
    assert movie_repository._db.count == 2 
    assert movie_repository._db.pop() == new_movie01
    assert movie_repository._db.pop() == new_movie02

def test_create_movie_BAD():
    movie_repository = get_movie_repository()

    new_movie01 = movie_repository.create_movie("Micheal's First Scream", "Robert Upey", 5)
    new_movie02 = movie_repository.create_movie("Micheal's Second Horror", "Robert Upey", 1)
    assert movie_repository._db.count !=0
    assert movie_repository._db.count != 1
    assert movie_repository.get_movie_by_title("Micheal's Second Horror") != new_movie01