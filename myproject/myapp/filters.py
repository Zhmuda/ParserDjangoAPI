import django_filters
from .models import Cinema

class CinemaFilter(django_filters.FilterSet):
    class Meta:
        model = Cinema
        fields = {
            'full_name': ['icontains'],  # Поиск по полному имени с учетом регистра
            'city': ['exact'],  # Поиск по городу точно
            'fo': ['exact'],    # Поиск по федеральному округу точно
            # Добавьте другие поля модели, по которым нужно выполнять поиск
        }
