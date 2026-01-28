from django.contrib import admin
from .models import DownloadFile

@admin.register(DownloadFile)
class DownloadFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'views', 'downloads', 'uploaded_at')
    list_filter = ('category',)
