from config import create_app, db
from app.routes.user_routes import user_bp

app = create_app()

with app.app_context():
    db.create_all()

app.register_blueprint(user_bp, url_prefix="/api/user")
