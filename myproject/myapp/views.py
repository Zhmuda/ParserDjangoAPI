from rest_framework import viewsets
from .models import Cinema
from .serializers import CinemaSerializer
from .filters import CinemaFilter

class CinemaViewSet(viewsets.ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    filter_class = CinemaFilter  # Обратите внимание на изменение filter_class
