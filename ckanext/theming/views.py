from flask import Blueprint


theming = Blueprint(
    "theming", __name__)


def page():
    return "Hello, theming!"


theming.add_url_rule(
    "/theming/page", view_func=page)


def get_blueprints():
    return [theming]
