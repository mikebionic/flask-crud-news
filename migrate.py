from main import app, db

from main.models import Post

db.drop_all()
db.create_all()

posts = [
	{
		"title": "New items in marketpace",
		"body": "Hurry uo fior daflhsdlf ioas dfhasd fherkfh rf",
		"image": "uploads/1.jpg",
	},
	{
		"title": "Secon hand products",
		"body": "HKLGHlasdbkLGLB khgILG LKDfsas dfhasd fherkfh rf",
		"image": "uploads/1.jpg",
	},
	{
		"title": "Third theft auto",
		"body": "GTA sucks lskdhf erfiohwe fh89ew fkhsdbfv rf",
		"image": "uploads/1.jpg",
	}
]

for post in posts:
	new_post = Post(**post)
	db.session.add(new_post)
	db.session.commit()