from flask import Blueprint
from .controller import get_list

weather_bp = Blueprint('weather_bp', __name__)
# print(weather_bp)
weather_bp.route('/', methods=['GET'])(get_list)
