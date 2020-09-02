from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .serializers import CreditCardSerializer
from .models import CreditCard
from django.conf import settings

from rest_framework.decorators import api_view


class CreditCardViewSet(viewsets.ModelViewSet):
    queryset = CreditCard.objects.all().order_by("name")
    serializer_class = CreditCardSerializer


@api_view(["GET", "POST"])
def get_post_credit_cards(request):
    if request.method == "GET":
        credit_cards = CreditCard.objects.all()
        serializer = CreditCardSerializer(credit_cards, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        data = {
            "name": request.data.get("name"),
            "pan": request.data.get("pan"),
        }
        serializer = CreditCardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
