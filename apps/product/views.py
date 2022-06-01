from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .pagination import ProductPagination
from django_filters.rest_framework import DjangoFilterBackend

class ListCreateProductView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    permission_classes=(IsAuthenticatedOrReadOnly,)
    pagination_class=ProductPagination
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['is_published', 'title']


    # def get_serializer_context(self):
    #     return super().get_serializer_context()

    def get_queryset(self):
        return Product.objects.filter(is_published=True)

