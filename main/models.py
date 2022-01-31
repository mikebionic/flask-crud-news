from main import db

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String, nullable=False)
	body = db.Column(db.String)
	image = db.Column(db.String)