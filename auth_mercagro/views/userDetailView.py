from rest_framework                             import status, generics
from rest_framework.response                    import Response
from rest_framework_permissions                 import IsAuthenticated
from rest_framework_simplejwt.backends          import TokenBackend
from django.conf                                import settings

from auth_mercagro.models.user                  import User
from auth_mercagro.serializers.userSerializer   import UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *arg, **kwargs):
        token           = request.META.get('HTTP_AUTHORIZATION')[7:]
        token_backend   = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data      = token_backend.decode(token, verify=False)

        if valid_data['user_id'] != kwargs ['pk']:
            stringResponse = {'detail': "Acceso no autorizado."}
            return Response(string_response, status=status.HTTP_401_UNAUTHORIZED)
        
        return super().get(self, request, *arg, **kwargs)

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def update(self, request, *arg, **kwargs):
        token           = request.META.get('HTTP_AUTHORIZATION')[7:]
        token_backend   = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data      = token_backend.decode(token, verify=False)

        if valid_data['user_id'] != kwargs ['pk']:
            stringResponse = {'detail': "Acceso no autorizado."}
            return Response(string_response, status=status.HTTP_401_UNAUTHORIZED)
        
        return super().update(self, request, *arg, **kwargs)


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *arg, **kwargs):
        token           = request.META.get('HTTP_AUTHORIZATION')[7:]
        token_backend   = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data      = token_backend.decode(token, verify=False)

        if valid_data['user_id'] != kwargs ['pk']:
            stringResponse = {'detail': "Acceso no autorizado."}
            return Response(string_response, status=status.HTTP_401_UNAUTHORIZED)
        
        return super().destroy(self, request, *arg, **kwargs)
