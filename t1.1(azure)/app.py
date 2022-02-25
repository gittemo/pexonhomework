from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
    
db = SQLAlchemy()

db.init_app(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70))
    year = db.Column(db.Integer)
    rating = db.Column(db.Integer)

@app.route('/', methods=['GET', 'POST'])
def movie():

    if request.method == 'GET':

        movie_list = Movie.query.all()
        movies = []
        
        for movie in movie_list:
            movies.append({'title' : movie.title, 'year' : movie.year, 'rating' : movie.rating})

        return jsonify({'movies' : movies})

    else:
        movie_data = request.get_json()

        new_movie = Movie(title=movie_data['title'], year=movie_data['year'], rating=movie_data['rating'])

        db.session.add(new_movie)
        db.session.commit()

        return 'Done', 201


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)