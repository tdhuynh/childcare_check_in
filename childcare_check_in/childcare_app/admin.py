from django.contrib import admin
from childcare_app.models import Child, Profile

admin.site.register([Child, Profile])
