from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Biodata, WebSetting
from django.contrib.auth import logout

def landing_page(request):
    biodata_list = Biodata.objects.all()
    setting, created = WebSetting.objects.get_or_create(id=1)
    
    # Cek apakah user login adalah anggota kelompok
    is_anggota = False
    if request.user.is_authenticated:
        try:
            is_anggota = request.user.userprofile.is_anggota_kelompok
        except:
            is_anggota = False

    return render(request, 'landing_page.html', {
        'biodata_list': biodata_list,
        'setting': setting,
        'user_is_anggota': is_anggota
    })

@login_required
def update_tampilan(request):
    if not request.user.userprofile.is_anggota_kelompok:
        raise PermissionDenied # Akun Google lain gak boleh masuk
        
    setting = WebSetting.objects.get(id=1)
    if request.method == 'POST':
        setting.warna_background = request.POST.get('warna_background')
        setting.font_utama = request.POST.get('font_utama')
        setting.diubah_oleh = request.user
        setting.save()
        return redirect('landing_page')
    return render(request, 'update_tampilan.html', {'setting': setting})

@login_required
def update_biodata(request, id):
    if not request.user.userprofile.is_anggota_kelompok:
        raise PermissionDenied
        
    biodata = get_object_or_404(Biodata, id=id)
    if request.method == 'POST':
        biodata.nama = request.POST.get('nama')
        biodata.npm = request.POST.get('npm')
        biodata.peran = request.POST.get('peran')
        biodata.deskripsi = request.POST.get('deskripsi')
        biodata.foto = request.POST.get('foto')
        biodata.save()
        return redirect('landing_page')
    return render(request, 'update_profil.html', {'biodata': biodata})

def logout_view(request):
    logout(request)  # Hapus session user
    return redirect('landing_page')