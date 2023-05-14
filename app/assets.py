"""Create and bundle CSS and JS files."""
from flask_assets import Bundle, Environment


def compile_static_assets(app):
    """Configure static asset bundles."""
    Environment.auto_build = True
    Environment.debug = False


