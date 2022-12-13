from django.shortcuts import render
from dashboard.forms import FromBarang
from dashboard.models import Barang
from dashboard.models import Aksesoris

# Create your views here.
def tambah_barang(request):
    form=FromBarang()
    konteks = {
        'form':form,
    }
    return render(request,'tambah_barang.html',konteks)

def produk(request):
    titelnya="Produk"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'produk.html',konteks)

def Barang_View(request):
    barangs=Barang.objects.all()

    konteks={
        'barangs':barangs,
    }
    return render(request, 'tampil_brg.html', konteks)

def Aksesoris_View(request):
    aksesoriss=Aksesoris.objects.all()

    konteks={
        'aksesoriss':aksesoriss,
    }
    return render(request, 'aksesoris.html', konteks)