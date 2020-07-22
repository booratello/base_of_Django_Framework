from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/index.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')


def gallery(request):
    return render(request, 'mainapp/gallery.html')


def ac_rouge(request):
    return render(request, 'mainapp/ac_rouge.html')
