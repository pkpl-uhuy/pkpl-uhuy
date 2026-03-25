from django.shortcuts import render, redirect, get_object_or_404
from .models import Biodata, WebSetting

# Menampilkan biodata di landing page
def landing_page(request):
    biodata_kelompok = Biodata.objects.all()
    setting_web, created = WebSetting.objects.get_or_create(id=1) 
    
    context = {
        'biodata': biodata_kelompok,
        'setting': setting_web,
    }
    return render(request, 'landing_page.html', context)

# Implement fungsi update tampilan (pure database)
# note untuk tirah: tolong tambahkan @login_required dan logic cek role di sini yaa
def update_tampilan(request):
    setting_web = WebSetting.objects.get(id=1)

    if request.method == 'POST':
        setting_web.warna_background = request.POST.get('warna_background')
        setting_web.font_utama = request.POST.get('font_utama')
        # Tirah, nanti tolong tambahkan logic "diubah_oleh = request.user" ya
        setting_web.save()
        return redirect('landing_page')

    return render(request, 'edit_tampilan.html', {'setting': setting_web})

# Implement fungsi update biodata (pure database)
# note untuk tirah: ini juga belum dibatasi hak aksesnya, tolong ditambahin yaa
def update_biodata(request, id):
    biodata = get_object_or_404(Biodata, id=id)

    if request.method == 'POST':
        biodata.nama = request.POST.get('nama')
        biodata.npm = request.POST.get('npm')
        biodata.peran = request.POST.get('peran')
        biodata.deskripsi = request.POST.get('deskripsi')
        
        if request.FILES.get('foto'):
            biodata.foto = request.FILES.get('foto')

        if biodata.nama and biodata.npm:
            biodata.save()
            return redirect('landing_page')
        else:
            return render(request, 'edit_biodata.html', {
                'biodata': biodata, 
                'error': 'Nama dan NPM wajib diisi!'
            })

    return render(request, 'edit_biodata.html', {'biodata': biodata})