from django.contrib import admin # noqa

from accounts.models import UserActions, Profile


class ProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'image')
    list_display = ('user', 'image')

class UserActionAdmin(admin.ModelAdmin):
    fields = ('user', 'action')
    readonly_fields = ('write_date', )
    list_display = ('user', 'write_date', 'action')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(UserActions, UserActionAdmin)
