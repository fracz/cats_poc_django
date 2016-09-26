from django.contrib.auth.models import User
from ipware.ip import get_ip
from rest_framework_jwt.views import ObtainJSONWebToken

from api.models import UserInfo


class ObtainJWT(ObtainJSONWebToken):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        result = super(ObtainJWT, self).post(request, *args, **kwargs)
        if 'token' in result.data:
            self._update_user_info(request)
        return result

    @staticmethod
    def _update_user_info(request):
        user = User.objects.get(username=request.data['username'])
        try:
            user.userinfo.last_ip = get_ip(request)
            user.userinfo.save()
        except UserInfo.DoesNotExist:
            user.userinfo = UserInfo.objects.create(user=user, last_ip=get_ip(request))
