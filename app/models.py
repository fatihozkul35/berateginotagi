from django.db import models

# Create your models here.

# Appconf Model
class Appconf(models.Model):
    logo = models.ImageField(upload_to='images/logo/')
    img = models.ImageField(upload_to='images/logo/')
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    adress = models.CharField(max_length=50, default='test')


    def __str__(self):
        return 'Genel Konfigurasyonları'
    
    class Meta:
        verbose_name = "Konfigurasyon"
        verbose_name_plural = "Site Konfigurasyonu"


# Category Model
class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    img = models.ImageField(upload_to='images/categorie/')
    position = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"


# Menu Model
class Menu(models.Model):
    category = models.ManyToManyField(Category, related_name='menus')
    title = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='images/menu/')
    descr = models.TextField(blank=True, null=True)
    position = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Menü"
        verbose_name_plural = "Menüler"


# Slider Model
class Slider(models.Model):
    title = models.CharField(max_length=25)
    img = models.ImageField(upload_to='static/images/slider/')
    descr = models.TextField(blank=True, null=True)
    position = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Slayt"
        verbose_name_plural = "Slaytlar"


# About Model
class About(models.Model):
    bulletpoint_1 = models.TextField()
    bulletpoint_2 = models.TextField()
    bulletpoint_3 = models.TextField()

    def __str__(self):
        return 'Hikayemiz'
    
    class Meta:
        verbose_name = "Hakkımızda"
        verbose_name_plural = "Hakkımızda"
