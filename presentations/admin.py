from django.contrib import admin

from .models import Presentation, Status


@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    def approve(self):
        status.name="APPROVED"
        
    def reject(self):
        status.name="REJECTED"



@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass
