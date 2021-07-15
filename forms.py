from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, EqualTo, Length
from flask_ckeditor import CKEditorField


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class CreateUserForm(FlaskForm):
    name = StringField("Your name:", validators=[DataRequired()])
    email = StringField("Your email address", validators=[DataRequired()])
    password = PasswordField("Your Password", validators=[DataRequired(),
                                                          EqualTo('confirm', message='Passwords must match'),
                                                          Length(min=8)])
    confirm = PasswordField("Confirm your password")
    submit = SubmitField("Register user")


class LoginForm(FlaskForm):
    email = StringField("Your email address: ", validators=[DataRequired()])
    password = PasswordField("Your password: ", validators=[DataRequired()])
    submit = SubmitField("Login")


class CommentForm(FlaskForm):
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Comment")
