from flask import render_template
from . import db
from .models import User, Education, Experience, Skill

from flask import current_app as app  # Usar current_app en lugar de importar app directamente

@app.route('/')
def index():
    user = User.query.first()  # Obtiene los datos del usuario
    educations = Education.query.filter_by(user_id=user.id).all()
    experiences = Experience.query.filter_by(user_id=user.id).all()
    skills = Skill.query.filter_by(user_id=user.id).all()
    return render_template('index.html', user=user, educations=educations, experiences=experiences, skills=skills)
