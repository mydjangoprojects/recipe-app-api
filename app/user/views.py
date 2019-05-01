from rest_framework import generics, authentication, permissions

from rest_auth.registration.views import RegisterView as BaseRegisterView,\
                                         LoginView as BaseLoginView

from .serializers import UserSerializer
from core.models import User


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user


# Rest-Auth Override
class RegisterView(BaseRegisterView):
    """Registers a new User in the system"""
    queryset = User.objects.all()


class LoginView(BaseLoginView):
    """Login with credentials in the system"""
    queryset = User.objects.all()
