from django.shortcuts import render

# Create your views here.
import os
import openai

from django.shortcuts import render
from .models import HumanQuery, AIResponse
from .serializers import HumanQuerySerializer, AIResponseSerializer
from rest_framework import viewsets
# Create your views here.

class HumanQueryViewSet(viewsets.ModelViewSet):
    serializer_class = HumanQuerySerializer # serializes the json data and save to database on send/post
    queryset = HumanQuery.objects.all() #return the queryset objects to json file on get


class AIResponseViewSet(viewsets.ModelViewSet):

    serializer_class = AIResponseSerializer

    queryset = AIResponse.objects.all()


# openai.api_key = os.getenv("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")

# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:",
#   temperature=0.9,
#   max_tokens=150,
#   top_p=1,
#   frequency_penalty=0.0,
#   presence_penalty=0.6,
#   stop=[" Human:", " AI:"]
# )