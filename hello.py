from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required, ValidationError

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'hard to guess string'


def validate_email(form, field):
    if '@' not in field.data:
        raise ValidationError("Please include an '@' in the email address. '{}' is missing an '@'.".format(field.data))

class InfoForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    email = StringField('What is your UofT Email address?', validators=[Required(), validate_email])
    submit = SubmitField('Submit')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        prev_name = session.get('name')
        prev_email = session.get('email')
        if prev_name is not None and prev_name != form.name.data:
            flash('Looks like you have changed your name!')
        if prev_email is not None and prev_email != form.email.data:
            flash('Looks like you have changed your email!')
        session['name'] = form.name.data
        session['email'] = form.email.data

    return render_template('index.html', form=form, name=session.get('name'), email=session.get('email'))


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, current_time=datetime.utcnow())


if __name__ == '__main__':
    app.run(debug=True)