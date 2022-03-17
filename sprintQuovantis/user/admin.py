from django.contrib import admin
from user.models import User
from sprintParam.models import Sprint,Parameter

admin.site.register(User)
admin.site.register(Sprint)
admin.site.register(Parameter)
