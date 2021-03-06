from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, FileField
from wtforms.validators import DataRequired, FileRequired, Length, Email, EqualTo, ValidationError
from application.models import Posts, User
from application import login_manager
from flask_login import current_user

class PostForm(FlaskForm):
    
    title = StringField("Title",
        validators=[
            DataRequired(),
            Length(min=1, max=100)
         ]
    )

    content = StringField("Content",
        validators=[
            DataRequired(),
            Length(min=1, max=500)
        ]
    )

    photos = FileField(validators=['Pictures'])

    submit = SubmitField("Post Content")

class RegistrationForm(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    first_name = StringField("First Name",
        validators=[
            DataRequired(),
            Length(min=1, max=30)
        ]
    )

    last_name = StringField("Last Name",
        validators=[
            DataRequired(),
            Length(min=1, max=30)
        ]
    )

    profile_picture = FileField(validators=['Profile Picture', FileRequired()])

    password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )

    confirm_password = PasswordField('Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password')
        ]
    )

    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already in use!')

class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    first_name = StringField("First Name",
        validators=[
            DataRequired(),
            Length(min=1, max=30)
        ]
    )

    last_name = StringField("Last Name",
        validators=[
            DataRequired(),
            Length(min=1, max=30)
        ]
    )

    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    profile_picture = FileField(validators=['Profile picture', FileRequired()])

    submit = SubmitField('Update')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use - please choose another')
