# app.py
from flask import Flask  
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trails.sqlite3'
db = SQLAlchemy(app)

db.Model.metadata.reflect(db.engine)

class Trail(db.Model):
    __tablename__ = 'Trails'
    __table_args__ = { 'extend_existing': True }
    TRAIL_ID = db.Column(db.Text, primary_key=True)

@app.route('/')
def hello():
    trailCount = Trail.query.count()

    good_trails = Trail.query.filter_by(CONDITION='Good').all()

    return render_template("index.html", count=trailCount, trails=good_trails)

@app.route('/trails/<slug>')
def detail(slug):
    trail = Trail.query.filter_by(TRAIL_ID=slug).first()

    return render_template("detail.html", trail=trail)

if __name__=='__main__':
    app.run(debug=True)