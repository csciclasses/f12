from google.appengine.ext import db
from auth.models import User


class ActivityType(db.Model):
    user = db.ReferenceProperty(User)
    name = db.StringProperty()
    uc_name = db.StringProperty()
    created_on = db.DateTimeProperty(auto_now_add=True)
    active = db.BooleanProperty(default=True)

    @staticmethod
    def _get_activity_type_by_name(name):
        if name is None or not name.strip():
            raise ValueError('Activity name cannot be empty')
        return ActivityType.all().filter('uc_name =', name.upper()).filter('active = ', True).get()

    @staticmethod
    def create_activity_type(email, name):
        activity = ActivityType._get_activity_type_by_name(name)
        if activity:
            return {'status': 'NameUsed'}

        user = User._get_user_by_email(email)
        if user:
            ActivityType(name=name, user=user, uc_name=name.upper()).put()
            return {'status': 'ActivityCreated'}
        else:
            return {'status': 'UserNotFound'}

    @staticmethod
    def get_user_activity_type_list(email):
        user = User._get_user_by_email(email)
        if user:
            query = ActivityType.all().filter('user =', user).filter('active =', True).order('-created_on')
            activity_list = list()
            for item in query.run():
                activity_list.append({
                    'id': item.key().id(),
                    'name': item.name,
                    'created_on': item.created_on
                    })
            return activity_list
        return None


class Activity(db.Model):
    user = db.ReferenceProperty(User)
    activity_type = db.ReferenceProperty(ActivityType)
    created_on = db.DateTimeProperty(auto_now_add=True)
    active = db.BooleanProperty(default=True)
    hours = db.IntegerProperty(default=0)
    minutes = db.IntegerProperty(default=0)
    seconds = db.IntegerProperty(default=0)

    @staticmethod
    def create_activity(email, data):
        user = User._get_user_by_email(email)
        activity_type = ActivityType.get_by_id(int(data['activity_type']))
        Activity(user=user, activity_type=activity_type, hours=data.get('hours', 0),
            minutes=data.get('minutes', 0), seconds=data.get('seconds', 0)).put()
        return {'status': 'ActivitySaved'}
