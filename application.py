from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from sqlalchemy import desc

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/numbersappdb'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(application)

application.config['SECRET_KEY'] = "secret_key"


class HighScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer)
    score = db.Column(db.Integer)


@application.route('/', methods=['GET'])
def main():
    high_score_1 = 0
    high_score_2 = 0
    high_score_3 = 0
    high_score_4 = 0
    high_score_5 = 0

    # Retrieve the high score for level 1 from the database
    high_score_query = HighScore.query.filter_by(level=1).order_by(desc(HighScore.score)).first()
    if high_score_query:
        high_score_1 = high_score_query.score
    high_score_query = HighScore.query.filter_by(level=2).order_by(desc(HighScore.score)).first()
    if high_score_query:
        high_score_2 = high_score_query.score
    high_score_query = HighScore.query.filter_by(level=3).order_by(desc(HighScore.score)).first()
    if high_score_query:
        high_score_3 = high_score_query.score
    high_score_query = HighScore.query.filter_by(level=4).order_by(desc(HighScore.score)).first()
    if high_score_query:
        high_score_4 = high_score_query.score
    high_score_query = HighScore.query.filter_by(level=5).order_by(desc(HighScore.score)).first()
    if high_score_query:
        high_score_5 = high_score_query.score

    return render_template('home.html', HighScore1=high_score_1, HighScore2=high_score_2, HighScore3=high_score_3, HighScore4=high_score_4, HighScore5=high_score_5)


@application.route('/instructions')
def instructions():
    return render_template('instructions.html')


@application.route('/levels', methods=['GET'])
def levels():
    high_score_1 = 0
    high_score_2 = 0
    high_score_3 = 0
    high_score_4 = 0
    high_score_5 = 0

    # Retrieve the high score for level 1 from the database
    high_score_query = HighScore.query.filter_by(level=1).order_by(desc(HighScore.score)).first()
    if high_score_query:
        high_score_1 = high_score_query.score
    high_score_query = HighScore.query.filter_by(level=2).order_by(desc(HighScore.score)).first()
    if high_score_query:
        high_score_2 = high_score_query.score
    high_score_query = HighScore.query.filter_by(level=3).order_by(desc(HighScore.score)).first()
    if high_score_query:
        high_score_3 = high_score_query.score
    high_score_query = HighScore.query.filter_by(level=4).order_by(desc(HighScore.score)).first()
    if high_score_query:
        high_score_4 = high_score_query.score
    high_score_query = HighScore.query.filter_by(level=5).order_by(desc(HighScore.score)).first()
    if high_score_query:
        high_score_5 = high_score_query.score

    return render_template('levels.html', HighScore1=high_score_1, HighScore2=high_score_2, HighScore3=high_score_3, HighScore4=high_score_4, HighScore5=high_score_5)


@application.route('/level1', methods=['GET', 'POST'])
def level1():
    high_score = None  # Initialize high_score with None

    # Retrieve the high score from the database
    high_score_query = HighScore.query.first()
    if high_score_query:
        high_score = high_score_query.score

    return render_template('level1.html', HighScore=high_score)


@application.route('/level2', methods=['GET', 'POST'])
def level2():
    high_score = None  # Initialize high_score with None

    # Retrieve the high score from the database
    high_score_query = HighScore.query.first()
    if high_score_query:
        high_score = high_score_query.score

    return render_template('level2.html', HighScore=high_score)


@application.route('/level3', methods=['GET', 'POST'])
def level3():
    high_score = None  # Initialize high_score with None

    # Retrieve the high score from the database
    high_score_query = HighScore.query.first()
    if high_score_query:
        high_score = high_score_query.score

    return render_template('level3.html', HighScore=high_score)


@application.route('/level4', methods=['GET', 'POST'])
def level4():
    high_score = None  # Initialize high_score with None

    # Retrieve the high score from the database
    high_score_query = HighScore.query.first()
    if high_score_query:
        high_score = high_score_query.score

    return render_template('level4.html', HighScore=high_score)


@application.route('/level5', methods=['GET', 'POST'])
def level5():
    high_score = None  # Initialize high_score with None

    # Retrieve the high score from the database
    high_score_query = HighScore.query.first()
    if high_score_query:
        high_score = high_score_query.score

    return render_template('level5.html', HighScore=high_score)


@application.route('/show_score/<int:level>/<int:score>')
def show_score(level, score):
    return f"Level: {level}<br>Score: {score}"


@application.route('/save_score', methods=['POST'])
def save_score():
    data = json.loads(request.data)
    level = data['level']
    score = data['score']

    # Create a new HighScore object and save it in the database
    high_score = HighScore(level=level, score=score)
    db.session.add(high_score)
    db.session.commit()

    return jsonify(message='Score saved successfully')


if __name__ == "__main__":
    application.run(debug=True)
