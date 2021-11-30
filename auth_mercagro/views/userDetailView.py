from rest_framework                             import status, generics
from django.conf                                import settings

from auth_mercagro.models.user                  import User
from auth_mercagro.serializers.userSerializer   import UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset            = User.objects.all()
    serializer_class    = UserSerializer
    
class UserUpdateView(generics.UpdateAPIView):
    queryset            = User.objects.all()
    serializer_class    = UserSerializer
    def update(self, request, *arg, **kwargs):
        return super().update(self, request, *arg, **kwargs)

class UserDeleteView(generics.DestroyAPIView):
    queryset            = User.objects.all()
    serializer_class    = UserSerializer
    def delete(self, request, *arg, **kwargs):
        return super().destroy(self, request, *arg, **kwargs)
