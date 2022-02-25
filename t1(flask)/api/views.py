from flask import Blueprint, request, jsonify
from . import db
from .models import Movie

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def movie():

    if request.method == 'POST':
        movie_data = request.get_json()

        new_movie = Movie(title=movie_data['title'], year=movie_data['year'], rating=movie_data['rating'])

        db.session.add(new_movie)
        db.session.commit()

        return 'Done', 201

    else:
        movie_list = Movie.query.all()
        movies = []
        
        for movie in movie_list:
            movies.append({'rating' : movie.rating, 'year' : movie.year, 'title' : movie.title})

        return jsonify({'movies' : movies})
