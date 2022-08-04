from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
