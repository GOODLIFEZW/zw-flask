from app.models.base import db
from sqlalchemy import Column, String, Integer
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True, nullable=False)
    mail = Column(String(32), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)  # 不保存明文密码

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)