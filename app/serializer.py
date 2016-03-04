from rest_framework.serializers import ModelSerializer

from app.models import Drink


class DrinkSerializer(ModelSerializer):
    class Meta:
        model = Drink
        fields = ['name', 'volume', 'proof', 'alcohol']
