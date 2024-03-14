from flask import Flask, request, jsonify
from model.database import DBSession, engine
from model import models
import os, uuid, secrets, string
from flask_cors import CORS 
from datetime import datetime, timedelta
from sqlalchemy import text

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "supports_credentials": True}})  # Allow any origin

sessions = {}

def generate_session_token():
    return str(uuid.uuid4())  # Generate a random session token using UUID

def init_flag():
    db = DBSession() # open session with database

    emails = db.query(models.User).filter(models.User.email == "admin@tophack.at").all() # check if email already created 

    if emails:
        return

    flag = os.environ.get("FLAG") # get flag from environment variable

    random_password = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(10)) # create "random" password for account

    new_user = models.User( # create the new user locally
        email='admin@tophack.at', password=random_password, balance=876582, notes="TH{" + flag + "}"
    )
    db.add(new_user) # commit new entry to db
    db.commit()
    db.refresh(new_user)
    db.close()

init_flag()

@app.route('/api/login', methods=['POST'])
def login():
    db = DBSession() # open session with database
    try:
        data = request.get_json()
        email = data.get('email', '') # get email from json request
        password = data.get('password', '') # get password from json request

        emails = db.query(models.User).filter(models.User.email == email).all() # search if the email even exists

        if not emails:
            return jsonify({'message': 'No Such Email Found!'}), 404 # if email wasn't found don't even send the request

        query = text(f"SELECT email FROM accounts WHERE email='{email}' AND password='{password}'") # if email exists send this select query

        with engine.connect() as con: # to directly execute queries we need to open a database session this way
            rs = con.execute(query) # execute query kinda like requests.get()

            rows = rs.fetchall() # format fetched data

            email_exists = any(row[0] == email for row in rows) # check if we got an email back

            if email_exists: 
                session_token = generate_session_token() # generate session cookie

                sessions[session_token] = { # store session cookie
                    'email': email
                }

                expiration_date = datetime.now() + timedelta(minutes=10) # let cookie expire in 10min
                response = jsonify({'message': 'Login successful!'}) # return json response
                response.set_cookie('session_token', session_token, expires=expiration_date, samesite='Strict') # pass cookie in response
                return response
            else:
                return jsonify({'message': 'Login failed!'}), 401 # return auth error if email doesn't exist

    except Exception as e:
        return jsonify({'error': 'An error occured'}), 500


@app.route('/api/signup', methods=['POST'])
def signup():
    db = DBSession() # open session with database

    data = request.get_json()
    email = data.get('email', '') # get email from json request
    password = data.get('password', '') # get password from json request

    emails = db.query(models.User).filter(models.User.email == email).all() # Check if email already exists

    if emails:
        return jsonify({'error': 'A user with this email does already exist!'}), 401 # response if user already exists

    try: # create new user
        new_user = models.User( 
        email=email, password=password, balance=0, notes="V3IwbmdVczNy" # Addign small hint to default user creation
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        db.close()
        return jsonify({'error': 'User successfully created!'}), 200 # return successful response

    except Exception as e:
        return jsonify({'error': 'An error occured'}), 500


@app.route('/api/data', methods=['GET'])
def data():
    session_token = request.cookies.get('session_token') # Check if user has a session cookie

    if not session_token:
        return jsonify({'error': 'No Open-Session Found!'}), 500 # If no cookie found return error

    db = DBSession() # open session with db

    try:
        email = sessions[session_token].get('email') # from session cookie get email
        user = db.query(models.User).filter(models.User.email == email).first() # query user information

        if user: # format user information from query
            user_data = {
                'email': user.email,
                'balance': user.balance,
                'notes': user.notes
            }

            return jsonify(user_data) # return formated data as json
        else:
            return jsonify({'error': 'You dare fiddling with my API?!?!?!'}), 404 # custom error code if they directly try to attack API

    except Exception as e:
        db.close()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)