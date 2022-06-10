from django.contrib import admin

class DateTimeCustomAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_created',
                       'datetime_updated',
                       'datetime_deleted',
                       'is_deleted')
