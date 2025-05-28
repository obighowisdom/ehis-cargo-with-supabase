from django.contrib import admin
from .models import cons
from .models import comment
from .models import location
from .models import location_two
from .models import TrackDatas

# Register your models here.

admin.site.register(cons)
admin.site.register(comment)
admin.site.register(location)
admin.site.register(location_two)
admin.site.register(TrackDatas)

