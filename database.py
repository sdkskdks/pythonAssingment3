from flask import Flask

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:<password>@localhost/<NameOfTheDatabase>'
db = SQLAlchemy(app)


class Tableuser(db.Model):
    __tablename__ = 'tableuser'
    id = db.Column( db.Integer, primary_key=True)
    login = db.Column(  db.Unicode)
    password = db.Column( db.Unicode)
    token = db.Column(db.Unicode)
    
    def __init__(self,id,login,password,token):
        self.id = id
        self.login = login
        self.password = password
        self.token = token

# Here we have to insert into(registration) at least the 3 users!!

# new_user = Tableuser(3,'syncnine@sbcglobal.net', '7gDJ6spK', '')
# new_user = Tableuser(2,'clkao@verizon.net', 'gAcsvmkp', '')
# new_user = Tableuser(1,'wildfire@aol.com', 'NvzfXXjC', '')
# db.session.add(new_user)
# db.session.commit()
# after registration we just comment the cods about insert
