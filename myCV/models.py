from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Proje Adı")
    description = models.TextField(verbose_name="Proje Açıklaması")
    image = models.ImageField(upload_to='portfolio/', null=True, blank=True, verbose_name="Proje Görseli")
    link = models.URLField(blank=True, verbose_name="Proje veya GitHub Linki")

    class Meta:
        verbose_name = "Proje"
        verbose_name_plural = "Projeler"

    def __str__(self):
        return self.title

    # HAKKIMDA (Kişisel Bilgiler) TABLOSU


class PersonalInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ad Soyad")
    role = models.CharField(max_length=100, verbose_name="Meslek/Rol")
    bio = models.TextField(verbose_name="Hakkımda Yazısı")
    location = models.CharField(max_length=100, verbose_name="Konum")
    email = models.EmailField(verbose_name="E-Posta")
    phone = models.CharField(max_length=20, verbose_name="Telefon")

    class Meta:
        verbose_name = "Kişisel Bilgi"
        verbose_name_plural = "Kişisel Bilgiler"

    def __str__(self):
        return self.name


# YETENEKLER TABLOSU
class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="Yetenek Adı")
    percentage = models.IntegerField(verbose_name="Yüzde Derecesi (0-100)")

    class Meta:
        verbose_name = "Yetenek"
        verbose_name_plural = "Yetenekler"

    def __str__(self):
        return f"{self.name} - %{self.percentage}"


# DENEYİM TABLOSU
class Experience(models.Model):
    title = models.CharField(max_length=100, verbose_name="Pozisyon Adı")
    company = models.CharField(max_length=100, verbose_name="Şirket/Kurum")
    date_range = models.CharField(max_length=50, verbose_name="Tarih Aralığı (Örn: 2023-Günümüz)")
    description = models.TextField(verbose_name="Açıklama")

    class Meta:
        verbose_name = "Deneyim"
        verbose_name_plural = "Deneyimler"

    def __str__(self):
        return self.title


# EĞİTİM TABLOSU
class Education(models.Model):
    degree = models.CharField(max_length=100, verbose_name="Bölüm/Derece")
    school = models.CharField(max_length=100, verbose_name="Okul Adı")
    date_range = models.CharField(max_length=50, verbose_name="Tarih Aralığı (Örn: 2021-2025)")
    description = models.TextField(verbose_name="Açıklama")

    class Meta:
        verbose_name = "Eğitim"
        verbose_name_plural = "Eğitimler"

    def __str__(self):
        return self.degree


# HİZMETLER TABLOSU
class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Hizmet Adı")
    description = models.TextField(verbose_name="Açıklama")
    icon = models.CharField(max_length=50, verbose_name="İkon Kodu (Örn: fa-solid fa-code)")

    class Meta:
        verbose_name = "Hizmet"
        verbose_name_plural = "Hizmetler"

    def __str__(self):
        return self.title


# İLETİŞİM MESAJLARI TABLOSU
class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Gönderen Adı")
    email = models.EmailField(verbose_name="Gönderen E-Posta")
    subject = models.CharField(max_length=200, verbose_name="Konu")
    message = models.TextField(verbose_name="Mesaj")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Gönderilme Tarihi")

    class Meta:
        verbose_name = "İletişim Mesajı"
        verbose_name_plural = "İletişim Mesajları"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"
