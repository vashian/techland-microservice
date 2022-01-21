from uuid import uuid4

from authz.authz import db

class User(db.Model):
  id = db.Column(db.String(64), primary_key=True, default=lambda : uuid4.hex)
  username = db.Column(db.String(128), unique = True, index=True, nullable=False)
  password = db.Culumn(db.string(256), nullable=False)
  role = db.Culumn(db.string(32), nullable=False, default=)
  created_at = db.Culumn(db.DateTime, nullable=False, default=)
  expires_at = db.Culumn(db.DateTime, nullable=False, default=)
  last_login_at = db.Column(db.DateTime, nullable=True, default=None)
  last_active_at = db.Column(db.DateTime, nullable=True, default=None)
  last_change_at = db.Column(db.DateTime, nullable=True, default=None)
  failed_auth_at = db.Column(db.DateTime, nullable=True, default=None)
  failed_auth_count = db.Column(db.Integer, nullable=False, default=0)
  status = db.Column(db.Integer, nullable=False, default=)
  