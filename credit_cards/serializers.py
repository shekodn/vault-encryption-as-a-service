from rest_framework import serializers

from .models import CreditCard

from credit_cards.vault import get_ciphertext


class CreditCardSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data["pan"] = get_ciphertext(validated_data["pan"])

        return CreditCard.objects.create(**validated_data)

    class Meta:
        model = CreditCard
        fields = ("name", "pan")
