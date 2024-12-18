from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        sort_by = self.request.query_params.get('sort_by', 'id')
        return Product.objects.all().order_by(sort_by)


@api_view(['POST'])
def select_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    product.selected = True
    product.save()
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)
