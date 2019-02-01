from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models.user import User


class EmailForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='邮箱不符合规范')])


class RegisterForm(Form):
    username = StringField(validators=[DataRequired(), Length(2, 10, message='用户名需要2~10个字符')])

    password = PasswordField(validators=[DataRequired(), Length(8, 16, message='密码不可以为空，请输入密码')])

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已注册')


class LoginForm(EmailForm):
    password = PasswordField(validators=[DataRequired(), Length(8, 16, message='密码不可以为空，请输入密码')])


class ResetPassword(Form):
    password1 = PasswordField(validators=[DataRequired(), Length(8, 16, message='密码不可以为空，请输入密码')])

    password2 = PasswordField(validators=[DataRequired(), Length(8, 16), EqualTo(
                'password1', message='两次输入密码不相同')])