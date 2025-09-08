from flask import Blueprint, render_template, request
from flaskblog.models import Post

main = Blueprint('main',__name__) 

@main.route("/")
@main.route("/home")
def home():
    
    page = request.args.get('page',1,type=int) # default page is 1 and 1 is integer type
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=3) # for each page total post is 2
    #paginate for post in single pages
    # order_by for which post want to be in 1st pages 
    return render_template('home.html',posts=posts)

@main.route("/about")
def about():
    return render_template('about.html',title='About')

