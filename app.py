from flask import Flask, redirect, render_template,request

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')



@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    return render_template('list_all_movies.html', list_movies_active=True)


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


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)
app.run()
