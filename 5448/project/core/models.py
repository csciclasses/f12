from google.appengine.ext import db


class RequestLog(db.Model):
    creation_date = db.DateTimeProperty(auto_now_add=True)
    request_id = db.StringProperty()

    @staticmethod
    def save(request_id):
        RequestLog(request_id=request_id).put()
