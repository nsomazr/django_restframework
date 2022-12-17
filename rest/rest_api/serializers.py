from .models import HumanQuery, AIResponse

from rest_framework import serializers


class HumanQuerySerializer(serializers.ModelSerializer):

    class Meta:

        model = HumanQuery

        read_only = 'human_query'

        fields = '__all__'


class AIResponseSerializer(serializers.ModelSerializer):

    class Meta:

        model = AIResponse

        read_only = 'ai_response'

        fields  = '__all__'