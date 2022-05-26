from django.shortcuts import render


def health_check(request):
    return render(request, 'hello.html')
