from rest_framework import viewsets, permissions
from .models import Subscription
from .serializers import SubscriptionSerializer
from rest_framework.permissions import IsAuthenticated


class SubscriptionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
