from pinterest_p import database, app
from pinterest_p.models import Usuario, Foto

with app.app_context():
    database.create_all()