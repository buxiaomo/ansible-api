from app import db


class PlayBook(db.Model):
    __tablename__ = "playbook"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    description = db.Column(db.String(100))

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return '' % self.id


db.create_all()