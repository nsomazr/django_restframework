from django.contrib import admin

# Register your models here.


from .models import HumanQuery, AIResponse

class HumanAdmin(admin.ModelAdmin):

    list = ('human_query', 'created_at')

    admin.site.register(HumanQuery)


class AIAdmin(admin.ModelAdmin):

    list = ('ai_response', 'created_at')

    admin.site.register(AIResponse)
