from django.contrib import admin
from .models import Dokumen # Import sketsa lemari yang kita buat tadi

# Daftarin ke panel admin
admin.site.register(Dokumen)