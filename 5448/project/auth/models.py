from google.appengine.ext import db
from google.appengine.api import mail
from core import utils


class User(db.Model):
    email = db.EmailProperty()
    uc_email = db.EmailProperty()
    password = db.StringProperty()
    creation_date = db.DateTimeProperty(auto_now_add=True)
    active = db.BooleanProperty()

    def _can_login(self):
        return self.active == True

    def _send_welcome_email(self):
        token = utils.EncUtil.encrypt('{0}'.format(self.key().id()))
        mail.send_mail(sender='Activity Tracker <subrat7@gmail.com>', to=self.email, subject='Email Validation', body='''
                You need to validate your account before you can access the website.
                Please click on the link below to validate your account.

                http://pyexp5448.appspot.com/validate/{0}

                Thank you.
            '''.format(token))

    @staticmethod
    def _get_user_by_email(email):
        return User.all().filter('uc_email =', email.upper()).get()

    @staticmethod
    def create(email, password):
        user = User._get_user_by_email(email)
        if user:
            return {'status': 'UserExists'}

        password = utils.HashUtil.hash(password)
        user = User(email=email, uc_email=email.upper(), password=password, validated=False)
        key = user.put()

        if not key or not key.id():
            return {'status': 'UnknownError'}

        user._send_welcome_email()
        return {'status': 'UserCreated'}

    @staticmethod
    def authenticate(email, password):
        user = User._get_user_by_email(email)
        if not user:
            return {'status': 'InvalidCredentials'}
        elif not user._can_login():
            return {'status': 'UserPending'}
        elif user.password == utils.HashUtil.hash(password):
            return {'status': 'Authenticated', 'email': user.email}
        else:
            return {'status': 'InvalidCredentials'}

    @staticmethod
    def validate(token):
        try:
            dec_str = utils.EncUtil.decrypt(token)
            user_id = int(dec_str)
            user = User.get_by_id(user_id)
        except:
            user = None

        if not user:
            return {'status': 'ValidateFailed'}
        else:
            user.active = True
            user.put()
            return {'status': 'UserActivated'}
