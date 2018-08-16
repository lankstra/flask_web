from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Length
from flask_pagedown.fields import PageDownField


class NameForm(FlaskForm):
    name = StringField('Enter your name', validators=[InputRequired()])
    submit = SubmitField('Submit')


class EditProfileForm(FlaskForm):
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField(u'地址', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    body = TextAreaField("Edit your post", validators=[InputRequired()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    body = StringField('', validators=[InputRequired()])
    submit = SubmitField('Submit')
