from django.db import models
from django.contrib.auth.models import User

class Lahan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lahan')
    nama_lahan = models.CharField(max_length=100)
    lokasi = models.CharField(max_length=255)
    luas = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nama_lahan
