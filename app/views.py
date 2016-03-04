from rest_framework.viewsets import ModelViewSet

from app.models import Drink
from app.serializer import DrinkSerializer


class DrinkViewSet(ModelViewSet):
    """
       **Example response**:

        **Response**:

            [
              {
                "name": "Morshinska",
                "volume": 1500,
                "proof": 0,
                "alcohol": 0
              },
              {
                "name": "Kefir",
                "volume": 500,
                "proof": 3,
                "alcohol": 15
              }
            ]

        """
    serializer_class = DrinkSerializer
    queryset = Drink.objects.all()
