from .db import db

class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    fractal_index = db.Column(db.Float, nullable=False)

    score_records = db.relationship("Record", back_populates="company")

    def to_dict(self):
        return {
            'id': self.id,
            'fractal_index': self.fractal_index,
            'score_records': {record.id: record.to_dict() for record in self.score_records},
        }
    def to_simple_dict(self):
        return {
            'id': self.id,
            'fractal_index': self.fractal_index,
        }
