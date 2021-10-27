# User Authentification project

Made by: f_name l_name, (groupName)

# Installing

Flask_SQLAlchemy==2.5.1
```bash
pip install sqlalchemy
```
Flask
```bash
pip install Flask
```
flaskr
```bash
pip install Flask
```
psycopg2
```bash
pip install psycopg2-binary
```

# Usage examples
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username 
```

# Example
```python
from datetime import datetime, timedelta
from flask import Flask
from flask.helpers import make_response
from flask import request
from flask.json import jsonify
import jwt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'

@app.route('/login')

def login():
    auth = request.authorization
    if auth and auth.password == 'password':
        token = jwt.encode({'user':auth.username, 'exp':datetime.utcnow() + timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token': token})
    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login required'})
@app.route('/protected')

def protection():
    token = request.args.get('token')
    return '''<h1> The token is {} <h1>'''.format(token)


if __name__ == '__main__':
    app.run(debug=True)
```

## Database.py

```python
from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:hashirama@localhost/python'
db = SQLAlchemy(app)

class Example(db.Model):

    __tablename__ = 'example'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column( db.Unicode)
    def __init__(self,id,name):
        self.id = id
        self.name = name


update_this = Example.query.filter_by(id=6).first()
update_this.name = 'updated!'
db.session.commit()
```

