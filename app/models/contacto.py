from app import db

class Contacto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    correo = db.Column(db.String(100))
    lugar = db.Column(db.String(200))
    fecha = db.Column(db.DateTime, nullable=False)
    motivo = db.Column(db.String(200))
    hora = db.Column(db.Time, nullable=False)

