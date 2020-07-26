from django.shortcuts import render


def main(request):
    context = {
        'title': 'historical games',
    }
    return render(request, 'mainapp/index.html', context)


def contacts(request):
    context = {
        'title': 'contacts',
    }
    return render(request, 'mainapp/contacts.html', context)


def gallery(request):
    context = {
        'title': 'gallery',
    }
    return render(request, 'mainapp/gallery.html', context)


def ac_rouge(request):
    context = {
        'title': 'assassin\'s creed: rogue',
    }
    return render(request, 'mainapp/ac_rouge.html', context)
