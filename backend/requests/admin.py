from django.contrib import admin

from requests.models import Request, RequestStatus


@admin.register(RequestStatus)
class RequestStatusAdmin(admin.ModelAdmin):
    list_display = ('status',)


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = (
        'passenger', 'category', 'status', 'description', 'from_station', 'to_station', 'date', 'time_start',
        'time_end',
        'employee')
    list_filter = ('employee', )
