from django.contrib import admin
# Kendi Project modelinin yanına yenilerini de ekliyoruz:
from .models import Project, PersonalInfo, Skill, Experience, Education, Service, ContactMessage

admin.site.register(Project)
admin.site.register(PersonalInfo)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Service)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('created_at',)

admin.site.site_header = "CV Kontrol Paneli"
admin.site.site_title = "CV Yönetim Paneli"
admin.site.index_title = "CV Modülleri"