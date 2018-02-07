from django.contrib import admin

from .models import Document, CallRecord

admin.site.register(Document)
admin.site.register(CallRecord)