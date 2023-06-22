from django.shortcuts import render


def index(request):
    return render(request,'personal/home.html')


def contact(request):
    return render(request, 'personal/basic.html', {'contactcontent': ['If you want to contact me, please mail me at', 'rajeshwari.adi2698@gmail.com']})


