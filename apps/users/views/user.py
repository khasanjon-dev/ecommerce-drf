from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    @action(methods=['post'], detail=False, permission_classes=(AllowAny,), serializer_class=)
    def send_code(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()

