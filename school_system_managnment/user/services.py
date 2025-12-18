from rest_framework_simplejwt.tokens import RefreshToken


class TokenService:

    def __init__(self , user):
        self.user = user

    def getToken(self):
        tokens = RefreshToken.for_user(self.user)
        access = str(tokens.access_token)
        refresh = str(access)

        JsonToken = {"access" :access , "refresh":refresh}
        return JsonToken