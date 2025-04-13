from django.shortcuts import render

from django.http import HttpResponse

from myapp.models import Mahasiswa

def mahasiswa_list(request):
    mahasiswa = Mahasiswa.objects.all()
    return render(request,'myapp/mahasiswa_list.html',{'mahasiswa':mahasiswa})

def index(request):
    return render(request, 'myapp/index.html')

from myapp.models import Jurusan

def jurusan_list(request):
    jurusan = Jurusan.objects.all()
    return render(request, 'myapp/jurusan_list.html', {'jurusan': jurusan})




