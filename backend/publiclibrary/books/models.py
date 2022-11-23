from publiclibrary import db

class Books(db.Model):
    
    __tablename__="books"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    author = db.Column(db.String(20))
    year_published  = db.Column(db.Integer)
    type = db.Column(db.Integer)
    books_loans = db.relationship("Loans", backref="Books", lazy=True)

    def __init__(self,name,author,year_published,type):
        self.name=name
        self.author=author
        self.year_published=year_published
        self.type=type
