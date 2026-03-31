from django.shortcuts import render
from .models import Dokumen

def dashboard(request):
    jml_surat_masuk = Dokumen.objects.filter(kategori='Surat Masuk').count()
    jml_surat_keluar = Dokumen.objects.filter(kategori='Surat Keluar').count()
    jml_proposal_lpj = Dokumen.objects.filter(kategori__in=['Proposal', 'LPJ']).count()
    
    # Mengambil 5 dokumen terbaru yang dimasukkan ke sistem
    dokumen_terbaru = Dokumen.objects.all().order_by('-tanggal_upload')[:5]

    context = {
        'jml_surat_masuk': jml_surat_masuk,
        'jml_surat_keluar': jml_surat_keluar,
        'jml_proposal_lpj': jml_proposal_lpj,
        'dokumen_terbaru': dokumen_terbaru, # Kirim paket data ini ke HTML
    }
    
    return render(request, 'arsip/dashboard.html', context)