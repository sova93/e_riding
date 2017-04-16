from django.contrib import admin
from .models import Competition, DescriptionStep, CustomUser, Horse, Team, VetCard, Pair, Step

admin.site.register(Competition)
admin.site.register(DescriptionStep)
admin.site.register(CustomUser)
admin.site.register(Horse)
admin.site.register(Team)
admin.site.register(VetCard)
admin.site.register(Pair)
admin.site.register(Step)
