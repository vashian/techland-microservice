from datetime import timedelta
from authz import config

from authz.config import Config
from authz.util import now

def user_expires_at():
  return now() + timedelta(days=Config.USER_DEFAULT_EXPIRY_TIME)