from flask import render_template
from . import db
from .models import User, Education, Experience, Skill

from flask import current_app as app  

@app.route('/')
def index():
    user = {
        "name": "Gaby Costilla",
        "bio": "Hola soy Gaby aunque me conocen como Gabdiz, gabygamer2hello,gabnzana en compota, soy programador en c++,js,pytoh,c#. Hize videojuegos en unity y godot y actualmente trabajo en la AGRM, siendo compositor y productor"
    }
    return render_template('index.html', user=user)


#no hay POO ni herencia ;( 