from . import web
from app.forms.auth import RegisterForm, LoginForm
from flask import request, redirect, url_for, flash
from flask_login import login_user, logout_user
from app.models.user import User
from app.models.base import db


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        try:
            user.set_attrs(form.data)
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
        return redirect('/login')
    return {}

@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if not next and not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账号不存在或密码错误')
    return {}