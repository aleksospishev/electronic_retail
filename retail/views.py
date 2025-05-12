from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .models import RetailNode
from .permissions import IsActiveEmployee
from .serializers import RetailNodeDetailSerializer, RetailNodeListSerializer


class RetailNodeViewSet(viewsets.ModelViewSet):
    queryset = RetailNode.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["country"]
    search_fields = ["contacts__city"]
    permission_classes = [IsActiveEmployee]

    def get_serializer_class(self):
        if self.action in ["list", "create", "update", "partial_update"]:
            return RetailNodeListSerializer
        return RetailNodeDetailSerializer
