from app.models.user_model import User
from config import db

class UserController:

    @staticmethod
    def get_all():
        users = User.query.all()
        return [u.to_dict() for u in users]

    @staticmethod
    def get_by_id(user_id):
        user = User.query.get(user_id)
        return user.to_dict() if user else None

    @staticmethod
    def create(data):
        user = User(
            username=data["username"],
            password=data["password"],
            fullname=data["fullname"],
            status=data["status"]
        )
        db.session.add(user)
        db.session.commit()
        return user.to_dict()

    @staticmethod
    def update(user_id, data):
        user = User.query.get(user_id)
        if not user:
            return None

        user.username = data["username"]
        user.password = data["password"]
        user.fullname = data["fullname"]
        user.status = data["status"]

        db.session.commit()
        return user.to_dict()

    @staticmethod
    def delete(user_id):
        user = User.query.get(user_id)
        if not user:
            return False

        db.session.delete(user)
        db.session.commit()
        return True
