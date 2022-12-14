from facturacion import db
from models import User
from email.utils import validate_email
from flask_bcrypt import generate_password_hash


def create_user(email: str, password: str) -> User:
    '''Creates a new user'''
    if validate_email(email):
        user = User(email=email, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        return user
    else:
        raise Exception('Invalid email')
