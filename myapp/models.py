from django.db import models

class Mahasiswa(models.Model):
    nim = models.CharField(max_length=10, unique=True)
    nama = models.CharField(max_length=100)
    jurusan = models.CharField(max_length=50)

class Jurusan(models.Model):
    kode = models.CharField(max_length=10, unique=True)
    nama_jurusan = models.CharField(max_length=100)



