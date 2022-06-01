from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
from rest_framework.permissions import IsAdminUser
from .permissions import IsAdminOrAllowAny

class ListCreateCategoryView(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=(IsAdminOrAllowAny,) #is_staff=True

