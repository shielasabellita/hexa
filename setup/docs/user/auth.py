from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework import HTTP_HEADER_ENCODING, exceptions
from django.utils.translation import gettext_lazy as _

from multiprocessing import AuthenticationError
from xml.dom import InvalidAccessErr
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from setup.docs.user.user_serializer import UserSerializer
from hashlib import blake2b
from hmac import compare_digest
import datetime, jwt, os
from dotenv import load_dotenv
load_dotenv()

class CustomAuthentication(BaseAuthentication):

    keyword = 'Token'
    model = None

    def get_model(self):
        if self.model is not None:
            return self.model
        from rest_framework.authtoken.models import Token
        return Token


    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != b'bearer':
            return None

        
        if len(auth) == 1:
            msg = _('Invalid token header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid token header. Token string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = validate_jwt_token(auth[1])

        except UnicodeError:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        return (token.user, token)

    def authenticate_header(self, request):
        return self.keyword



## ============================== TOKEN VALIDATION =====================================================

# validate jwt token on login
def validate_jwt_token(token):
    if not token:
        raise Exception("Missing Token")

    try:
        data = jwt_decoder(token)
        user = User.objects.get(id=data['user'])
        if user:
            user_token = Token.objects.filter(user=user)
            if verify_hashed(user_token[0].key, data['key']):
                return user_token[0].key
            else:
                raise AuthenticationError("Password did not matched")

    except jwt.ExpiredSignatureError:
        raise Exception("Token Expired")
    except jwt.InvalidTokenError:
        raise Exception("Invalid Token")


#time_type = "Days, Minutes, Seconds, Hours, Weeks"
jwt_config = {
    "time_type": str(os.getenv('TIMETYPE')),
    "token_expiry": str(os.getenv('TOKENEXPIRY')),   ## 1 day expiration
    "secret_key": str(os.getenv('HexaSuitesv2')),
    "algo": "HS256"
}


def _set_token(user, key):
    try:
        payload = {
            "user": user.id,
            "exp": get_jwt_config_time(),
            "key": hashed_token(key)
        }
        jwt_token = jwt.encode(payload, jwt_config['secret_key'], algorithm=jwt_config['algo'])
        return jwt_token
    except AuthenticationError as e:
        raise Exception(str(e))


def get_jwt_config_time():
    now = datetime.datetime.now()
    times_types = {
        "Seconds" : now + datetime.timedelta(seconds=int(jwt_config["token_expiry"])),
        "Minutes" : now + datetime.timedelta(minutes=int(jwt_config["token_expiry"])),
        "Hours" : now + datetime.timedelta(hours=int(jwt_config["token_expiry"])),
        "Days" : now + datetime.timedelta(days=int(jwt_config["token_expiry"])),
        "Weeks" : now + datetime.timedelta(weeks=int(jwt_config["token_expiry"]))
    }
    return times_types[jwt_config["time_type"]].strftime('%s')


def hashed_token(cookie):
    h = blake2b(digest_size=16, key=b'HEXA-Suites.ph')
    h.update(bytes(cookie, 'utf-8'))
    hashed = h.hexdigest().encode('utf-8')
    return hashed.decode("utf-8")


def verify_hashed(cookie, key):
    cur_key = hashed_token(cookie)
    if compare_digest(cur_key, key):
        return True
    else:
        raise InvalidAccessErr("Invalid Token")

def jwt_decoder(token):
    decoded = jwt.decode(token, jwt_config['secret_key'], algorithms=[jwt_config['algo']])
    return decoded
