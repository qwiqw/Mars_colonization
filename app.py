from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from jobs_api import blueprint
from data import db_session
from flask_restful import Api
from user_resourse import UserResourse, UserListResourse

app = Flask(__name__)
app.config['SECRET_KEY'] = 'qwe'

api = Api(app)
api.add_resource(UserResourse, '/api/v2/users/<int:user_id>')
api.add_resource(UserListResourse, '/api/v2/users')


class LoginForm(FlaskForm):
    astronaut_id = StringField('ID астронавта', validators=[DataRequired()])
    astronaut_password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    capitan_id = StringField('ID капитана', validators=[DataRequired()])
    capitan_password = PasswordField('Пароль капитана', validators=[DataRequired()])
    access = SubmitField('Доступ')


@app.route('/')
def main():
    return render_template('base.html')


@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/promotion')
def promotion():
    return '''<h1>Человечество вырастает из детства.<br>
Человечеству мала одна планета.<br>
Мы сделаем обитаемыми безжизненные пока планеты.<br>
И начнем с Марса!<br>
Присоединяйся!<br></h1>'''


@app.route('/image_mars')
def image_mars():
    return render_template('image_mars.html')


@app.route('/promotion_image')
def promotion_image():
    return render_template('promotion_image.html')


@app.route('/astronaut_selection')
def astronaut_selection():
    return render_template('astronaut_selection.html')


@app.route('/answer', methods=['POST'])
@app.route('/auto_answer', methods=['POST'])
def answer():
    context = {
        'title': 'Анкета',
        'surname': request.form['surname'],
        'name': request.form['name'],
        'education': request.form['education'],
        'profession': ', '.join(request.form.getlist('profession')),
        'gender': request.form['gender'],
        'motivation': request.form['motivation'],
        'ready': request.form.get('ready', '') == 'Готов'
    }
    return render_template('answer.html', **context)


@app.route('/training/<prof>')
def training(prof):
    context = {
        'prof': prof
    }
    return render_template('training.html', **context)


@app.route('/list_prof/<lst>')
def list_prof(lst):
    context = {
        'profs': ['инженер', 'сварщик', 'повар', 'машинист', 'дворник'],
        'list': lst
    }
    return render_template('list_prof.html', **context)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            return redirect('/')


if __name__ == '__main__':
    db_session.global_init('database/mars_exploer.db')
    app.register_blueprint(blueprint)
    app.run(host='127.0.0.1', port=8080)
