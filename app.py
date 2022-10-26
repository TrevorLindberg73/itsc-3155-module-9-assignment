from flask import Flask, redirect, render_template, request

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')



@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    # The line below was to make sure I was making a row for a new movie.
    #new_movie = movie_repository.create_movie("a","b", 1)
    movie_list = movie_repository.get_all_movies()
    return render_template('list_all_movies.html', list_movies_active=True, movie_list = movie_list)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # Completed by Marcel Newman
    movie_title =request.form.get('movie_title')
    movie_director =request.form.get('movie_director')
    movie_rating =request.form.get('movie_rating')
    new_movie = movie_repository.create_movie(movie_title, movie_director,int(movie_rating))
    return redirect('/movies')

default = movie_repository.create_movie('Spiderman', 'Sam Raimi', 3)
@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    #Completed by Trevor Lindberg
    title = request.args.get('search', 'Spiderman')
    mov = movie_repository.get_movie_by_title(title)
    ratings = mov.rating
    return render_template('search_movies.html', rating = ratings, search_active=True)
