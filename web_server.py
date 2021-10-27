from datetime import datetime, timedelta
from flask import Flask
from flask.helpers import make_response
from flask import request
from flask.json import jsonify
from database import Tableuser, app, db
import jwt

app.config['SECRET_KEY'] = 'thisismyflasksecretkey'


@app.route('/login/<login>/<password>')
def login(login, password):
    auth = request.authorization
    person = Tableuser.query.filter_by(login = login, password = password).first_or_404(description='Could not found a person Wrong login and password values:  {}'.format(login))
    if auth and auth.username == login and auth.password == password:
        token = jwt.encode({'user':auth.username, 'exp':datetime.utcnow() + timedelta(minutes=30)}, app.config['SECRET_KEY'])
        update_that = Tableuser.query.filter_by(login = login, password = password).first()
        update_that.token = token
        db.session.commit()
        output = "Congratulations, you are stored the token on database!!! "
        return jsonify({'token': token}, output )
    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login required'})


@app.route('/protected')
def protection():
    token = request.args.get('token')
    person = Tableuser.query.filter_by(token = token).first_or_404(description=' <h1>Hello, Could not verify the token </h1>  {}'.format(token))
    return '''<h1> Hello, token which is provided is correct {} <h1>'''.format(token)

if __name__ == '__main__':
    app.run(debug=True)