from flask import render_template, request, Blueprint

from webapp.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def index():
  page = request.args.get('page', 1, type=int)
  posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
  return render_template('main/index.html.j2', posts=posts)


@main.route("/about")
def about():
  return render_template('main/about.html.j2', title='About')
