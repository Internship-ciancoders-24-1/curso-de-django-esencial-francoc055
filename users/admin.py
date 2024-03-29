from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as  BaseUserAdmin
from users.models import Profile
from django.contrib.auth.models import User

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'phone_number', 'website')
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number', 'website')
    

    fieldsets = (
        ('Profile', {
            'fields': ('user', 'picture'),
        }),
        ('Extra info', {
            'fields': ('website', 'phone_number'),
        }),
        ('Metadata', {
            'fields': ('created', 'modified'),
        }),
    )

    readonly_fields = ('created', 'modified')

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)



admin.site.unregister(User)
admin.site.register(User, UserAdmin)