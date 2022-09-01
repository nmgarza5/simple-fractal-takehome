from .db import db

class Record(db.Model):
    __tablename__ = 'score_records'

    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    candidate_id = db.Column(db.Integer, nullable=False)
    coding_score = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(255), nullable=False)

    company = db.relationship("Company", back_populates="score_records")

    def to_dict(self):
        return {
            'id': self.id,
            'company_id': self.company_id,
            'candidate_id': self.candidate_id,
            'coding_score': self.coding_score,
            'title': self.title,
            'company': self.company.to_simple_dict()
        }
