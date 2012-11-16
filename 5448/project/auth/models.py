from google.appengine.ext import db
import hashlib


class User(db.Model):
    email = db.EmailProperty()
    uc_email = db.EmailProperty()
    password = db.StringProperty()
    creation_date = db.DateTimeProperty(auto_now_add=True)
    validated = db.BooleanProperty()

    @staticmethod
    def fetch_user(email):
        result = User.all().filter('uc_email =', email.upper()).get()
        if result:
            return {'email': result.email}
        else:
            return None

    @staticmethod
    def create(email, password):
        if User.fetch_user(email):
            return {'status': 'UserExists'}

        password = hashlib.sha512(password).hexdigest()
        User(email=email, uc_email=email.upper(), password=password, validated=False).put()

        if User.fetch_user(email):
            #Try to send Email with auth token
            return {'status': 'UserCreated'}
        return {'status': 'Error'}

    @staticmethod
    def authenticate(email, password):
        password = hashlib.sha512(password).hexdigest()
        result = User.all().filter('uc_email =', email.upper()).get()

        if result:
            if result.password == password:
                if result.validated:
                    return {'status': 'Authenticated', 'email': email}
                else:
                    return {'status': 'NeedsValidation', 'email': email}
            else:
                return {'status': 'Invalid', 'email': email}
        else:
            return {'status': 'Unknown', 'email': email}


