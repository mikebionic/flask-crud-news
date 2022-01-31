import os
from flask import render_template, request, redirect

from main import app, db
from main.config import Config

from main.models import Post

@app.route('/', methods=["GET", "POST"])
@app.route('/posts/', methods=["GET", "POST"])
def posts_page():

	if request.method == "POST":
		new_post_data = {
			"title": request.form['title'],
			"body": request.form['body'],
		}

		if "image" in request.files:
			file = request.files["image"]
			file_db_url = os.path.join(Config.UPLOAD_FOLDER, file.filename)
			file_location = os.path.join(os.path.abspath(''), 'main/static/', file_db_url)
			file.save(file_location)
			new_post_data["image"] = file_db_url

		new_post = Post(**new_post_data)
		db.session.add(new_post)
		db.session.commit()
		


	posts = Post.query.order_by(Post.id.desc()).all()
	return render_template(
		"posts.html",
		posts = posts
	)

@app.route('/update_post/<id>', methods=["GET", "POST"])
def update_post(id):
	post = Post.query.filter_by(id = id).first_or_404()
	if request.method == "POST":

		if len(request.form['title']) > 2:
			post.title = request.form['title']
		if len(request.form['body']) > 2:
			post.body = request.form['body']

		if "image" in request.files:
			file = request.files["image"]
			if len(file.filename) > 2:
				file_db_url = os.path.join(Config.UPLOAD_FOLDER, file.filename)
				file_location = os.path.join(os.path.abspath(''), 'main/static/', file_db_url)
				file.save(file_location)
				post.image = file_db_url

		db.session.commit()
		return redirect('/posts/')
		


	return render_template(
		"update_post.html",
		post = post
	)