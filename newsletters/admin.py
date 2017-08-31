from django.contrib import admin
from .models import Newsletter

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp"]

    class Meta:
        model = Newsletter

# Register your models here.
admin.site.register(Newsletter, NewsletterAdmin)
