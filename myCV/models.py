from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Proje Adı")
    description = models.TextField(verbose_name="Proje Açıklaması")
    image = models.ImageField(upload_to='portfolio/', null=True, blank=True, verbose_name="Proje Görseli")
    link = models.URLField(blank=True, verbose_name="Proje veya GitHub Linki")

    def __str__(self):
        return self.title