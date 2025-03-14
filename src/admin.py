import os
from flask_admin import Admin
from models import db, User, Personajes, Planetas, Vehiculos, Starships, Favoritos
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    class FavoritosAdmin(ModelView):
        column_list = ("id", "user_id", "personajes_id","planetas_id", "vehiculos_id", "starships_id")
        form_columns = ("user_id", "personajes_id","planetas_id", "vehiculos_id", "starships_id")
        column_hide_backrefs = False

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Personajes, db.session))
    admin.add_view(ModelView(Planetas, db.session))
    admin.add_view(ModelView(Vehiculos, db.session))
    admin.add_view(ModelView(Starships, db.session))
    admin.add_view(FavoritosAdmin(Favoritos, db.session))






    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))