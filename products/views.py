from django.db.models import Q
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    """
    get:
    List all products with optional search and sorting.

    post:
    Create a new product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        search_query = self.request.query_params.get('search', None)
        sort_by = self.request.query_params.get('sort_by', 'id')

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) | Q(description__icontains=search_query)
            )

        return queryset.order_by(sort_by)


@api_view(['POST'])
def toggle_product_selection(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    print('exact ', not product.selected)
    print('changed ', not product.selected)

    product.selected = not product.selected
    product.save()

    serializer = ProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)
