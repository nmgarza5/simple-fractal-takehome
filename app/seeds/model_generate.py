from app.models import db, Company, Record



def seed_companies():
    db.session.commit()
def seed_records():
    db.session.commit()

def undo_companies():
    db.session.execute('TRUNCATE companies RESTART IDENTITY CASCADE;')
    db.session.commit()
def undo_records():
    db.session.execute('TRUNCATE records RESTART IDENTITY CASCADE;')
    db.session.commit()
