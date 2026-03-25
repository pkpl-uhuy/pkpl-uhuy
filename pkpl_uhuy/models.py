from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Model Biodata (Dilihat tanpa login)
class Biodata(models.Model):
    nama = models.CharField(max_length=100)
    npm = models.CharField(max_length=20, unique=True)
    peran = models.CharField(max_length=50) 
    deskripsi = models.TextField()
    foto = models.ImageField(upload_to='foto_biodata/', null=True, blank=True)

    def __str__(self):
        return self.nama

# Model Setting Web (Syarat Otorisasi: Ubah Warna/Font)
class WebSetting(models.Model):
    warna_background = models.CharField(max_length=20, default="#FFFFFF")
    font_utama = models.CharField(max_length=50, default="Arial, sans-serif")
    diubah_oleh = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    waktu_ubah = models.DateTimeField(auto_now=True)

# Model Ekstensi User (Syarat Autentikasi: Membedakan Anggota vs Akun Lain)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_anggota_kelompok = models.BooleanField(default=False) # Set True hanya untuk email anggota kelompok

    def __str__(self):
        return self.user.email
    
# Model Signals yang secara otomatis membuat UserProfile setiap ada User baru dari Google OAuth
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # note for all: tolong update list email ini sesuai dengan email kalian yaa
        email_kelompok = ['tasyanasaragih@gmail.com', 'tasya.nabila41@ui.ac.id', 
                          'syifa@gmail.com', 
                          'elsa@gmail.com', 
                          'naila@gmail.com', 
                          'tirah@gmail.com']
        
        is_anggota = instance.email in email_kelompok
        UserProfile.objects.create(user=instance, is_anggota_kelompok=is_anggota)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()