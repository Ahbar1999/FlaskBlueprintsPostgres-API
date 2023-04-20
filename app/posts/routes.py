from flask import Blueprint
from .controller import submit_post, get_nearby_posts, get_posts


posts_bp = Blueprint('posts_bp', __name__)
posts_bp.route('/', methods=['GET'])(get_posts)
posts_bp.route('/nearby', methods=['GET'])(get_nearby_posts)
posts_bp.route('/', methods=['POST'])(submit_post)

