from django.db import models
from django.contrib.auth.models import User # Buat nyatet siapa sekre/admin yang upload

class Dokumen(models.Model):
    # Bikin opsi dropdown buat kategori
    KATEGORI_CHOICES = [
        ('Surat Masuk', 'Surat Masuk'),
        ('Surat Keluar', 'Surat Keluar'),
        ('Proposal', 'Proposal'),
        ('LPJ', 'Laporan Pertanggungjawaban'),
        ('Lainnya', 'Dokumen Lainnya'),
    ]

    judul = models.CharField(max_length=255, verbose_name="Judul Dokumen")
    kategori = models.CharField(max_length=50, choices=KATEGORI_CHOICES)
    
    # upload_to="%Y/%m/" bikin Django otomatis nyimpen file ke folder Tahun/Bulan biar rapi!
    file_dokumen = models.FileField(upload_to='dokumen/%Y/%m/') 
    
    keterangan = models.TextField(blank=True, null=True, help_text="Catatan tambahan (opsional)")
    tanggal_upload = models.DateTimeField(auto_now_add=True) # Otomatis nyatet waktu upload
    
    # Nyambungin dokumen ke akun user yang lagi login
    pengunggah = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.judul} ({self.kategori})"